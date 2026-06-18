"""
Chatbot - Sistema de Gestión de Vacaciones
============================================

Implementa una Máquina de Estados Finitos (FSM) para manejar el flujo
de la conversación, manteniendo "memoria" del punto del proceso en el
que se encuentra el usuario.

Estados posibles:
    INICIO                  -> Carga el archivo de empleados.
    PIDIENDO_LEGAJO          -> Solicita y valida el número de legajo.
    PIDIENDO_DIAS            -> Solicita y valida la cantidad de días.
    PROCESANDO_SOLICITUD     -> Aprueba o rechaza según el saldo.
    PREGUNTANDO_REPETIR      -> Pregunta si desea hacer otra operación.
    ERROR_FATAL              -> Se excedieron los reintentos permitidos.
    FIN                      -> Cierra el programa.
"""

import pandas as pd

ARCHIVO = "empleados.xlsx"
MAX_REINTENTOS = 3


# ─────────────────────────────────────────
#  ESTADO COMPARTIDO DE LA CONVERSACIÓN
# ─────────────────────────────────────────
# Se usa un diccionario en vez de variables sueltas para que cada
# función de estado pueda leer y escribir el "contexto" de la sesión.
contexto = {
    "empleados": None,
    "legajo": None,
    "empleado": None,
    "dias": None,
}


# ─────────────────────────────────────────
#  FUNCIONES DE ESTADO
# ─────────────────────────────────────────

def estado_inicio():
    """Carga el archivo Excel con los datos de empleados.

    Returns:
        str: Próximo estado ("PIDIENDO_LEGAJO" o "ERROR_FATAL").
    """
    print("=" * 40)
    print("  SISTEMA DE GESTIÓN DE VACACIONES")
    print("=" * 40)
    print("¡Hola! Soy el asistente virtual de vacaciones.\n")

    try:
        contexto["empleados"] = pd.read_excel(ARCHIVO)
    except FileNotFoundError:
        print(f"Error: no se encontró el archivo {ARCHIVO}")
        return "ERROR_FATAL"
    except Exception as e:
        # Camino infeliz: el archivo existe pero está corrupto,
        # vacío, en un formato no soportado, etc.
        print(f"Error: no se pudo leer el archivo ({e})")
        return "ERROR_FATAL"

    # Camino infeliz: el archivo existe pero le faltan columnas clave
    columnas_necesarias = {"Legajo", "Nombre", "DiasDisponibles"}
    columnas_presentes = set(contexto["empleados"].columns)
    if not columnas_necesarias.issubset(columnas_presentes):
        faltantes = columnas_necesarias - columnas_presentes
        print(f"Error: el archivo no tiene las columnas requeridas: {faltantes}")
        return "ERROR_FATAL"

    # Camino infeliz: el archivo existe pero no tiene filas
    if contexto["empleados"].empty:
        print("Error: el archivo de empleados está vacío.")
        return "ERROR_FATAL"

    return "PIDIENDO_LEGAJO"


def estado_pidiendo_legajo():
    """Solicita y valida el número de legajo, con reintentos.

    Returns:
        str: Próximo estado ("PIDIENDO_DIAS" o "ERROR_FATAL").
    """
    intentos = 0

    while intentos < MAX_REINTENTOS:
        valor = input("Ingrese su número de legajo: ").strip()

        # Camino infeliz: campo vacío
        if valor == "":
            intentos += 1
            print("Error: el campo no puede estar vacío.")
            print(f"Intentos restantes: {MAX_REINTENTOS - intentos}\n")
            continue

        # Camino infeliz: no es un número (letras, símbolos, decimales, negativos)
        if not valor.isdigit():
            intentos += 1
            print("Error: debe ingresar solamente números.")
            print(f"Intentos restantes: {MAX_REINTENTOS - intentos}\n")
            continue

        legajo = int(valor)

        # Camino infeliz: el legajo no existe en la base
        empleado = contexto["empleados"][contexto["empleados"]["Legajo"] == legajo]
        if empleado.empty:
            intentos += 1
            print("Error: el legajo no existe.")
            print(f"Intentos restantes: {MAX_REINTENTOS - intentos}\n")
            continue

        # Éxito: guardamos en el contexto y avanzamos de estado
        contexto["legajo"] = legajo
        contexto["empleado"] = empleado.iloc[0]

        nombre = contexto["empleado"]["Nombre"]
        saldo = int(contexto["empleado"]["DiasDisponibles"])
        print(f"\nEmpleado        : {nombre}")
        print(f"Días disponibles: {saldo}\n")

        return "PIDIENDO_DIAS"

    # Se agotaron los reintentos
    print("\nSe alcanzó el número máximo de intentos permitidos.")
    return "ERROR_FATAL"


def estado_pidiendo_dias():
    """Solicita y valida la cantidad de días a solicitar, con reintentos.

    Returns:
        str: Próximo estado ("PROCESANDO_SOLICITUD" o "ERROR_FATAL").
    """
    intentos = 0

    while intentos < MAX_REINTENTOS:
        valor = input("¿Cuántos días desea solicitar?: ").strip()

        # Camino infeliz: campo vacío
        if valor == "":
            intentos += 1
            print("Error: el campo no puede estar vacío.")
            print(f"Intentos restantes: {MAX_REINTENTOS - intentos}\n")
            continue

        # Camino infeliz: no es un número válido
        if not valor.isdigit():
            intentos += 1
            print("Error: debe ingresar solamente números.")
            print(f"Intentos restantes: {MAX_REINTENTOS - intentos}\n")
            continue

        dias = int(valor)

        # Camino infeliz: cero días
        if dias == 0:
            intentos += 1
            print("Error: la cantidad debe ser mayor que cero.")
            print(f"Intentos restantes: {MAX_REINTENTOS - intentos}\n")
            continue

        # Camino infeliz: una cantidad irrealmente alta (regla de negocio)
        if dias > 365:
            intentos += 1
            print("Error: no se pueden solicitar más de 365 días.")
            print(f"Intentos restantes: {MAX_REINTENTOS - intentos}\n")
            continue

        contexto["dias"] = dias
        return "PROCESANDO_SOLICITUD"

    print("\nSe alcanzó el número máximo de intentos permitidos.")
    return "ERROR_FATAL"


def estado_procesando_solicitud():
    """Evalúa la solicitud contra el saldo y persiste los cambios si corresponde.

    Returns:
        str: Próximo estado ("PREGUNTANDO_REPETIR").
    """
    saldo = int(contexto["empleado"]["DiasDisponibles"])
    dias = contexto["dias"]
    legajo = contexto["legajo"]
    empleados = contexto["empleados"]

    if dias > saldo:
        print("\nSolicitud RECHAZADA")
        print("   No posee días suficientes.")
        return "PREGUNTANDO_REPETIR"

    nuevo_saldo = saldo - dias

    # Actualiza la tabla en memoria
    empleados.loc[empleados["Legajo"] == legajo, "DiasDisponibles"] = nuevo_saldo

    # Persiste los cambios en el archivo (regla de negocio + persistencia real)
    try:
        empleados.to_excel(ARCHIVO, index=False)
    except PermissionError:
        # Camino infeliz: el archivo está abierto en Excel y bloqueado
        print("\nError: no se pudo guardar. Cierre el archivo Excel e intente de nuevo.")
        return "PREGUNTANDO_REPETIR"

    print("\nSolicitud APROBADA")
    print(f"   Días descontados : {dias}")
    print(f"   Nuevo saldo      : {nuevo_saldo}")

    return "PREGUNTANDO_REPETIR"


def estado_preguntando_repetir():
    """Pregunta si el usuario desea realizar otra operación.

    Returns:
        str: Próximo estado ("PIDIENDO_LEGAJO" o "FIN").
    """
    intentos = 0

    while intentos < MAX_REINTENTOS:
        respuesta = input("\n¿Desea realizar otra operación? (s/n): ").strip().lower()

        if respuesta in ("s", "si", "sí"):
            # Reinicia el contexto de la operación anterior
            contexto["legajo"] = None
            contexto["empleado"] = None
            contexto["dias"] = None
            return "PIDIENDO_LEGAJO"

        if respuesta in ("n", "no"):
            return "FIN"

        # Camino infeliz: respuesta no reconocida
        intentos += 1
        print("Error: responda 's' para sí o 'n' para no.")
        print(f"Intentos restantes: {MAX_REINTENTOS - intentos}")

    # Si agota los intentos, se asume que no quiere continuar
    print("\nNo se reconoció una respuesta válida. Finalizando.")
    return "FIN"


def estado_error_fatal():
    """Estado terminal cuando ocurre un error irrecuperable.

    Returns:
        str: Próximo estado ("FIN").
    """
    print("\nNo fue posible continuar con la operación.")
    return "FIN"


def estado_fin():
    """Estado terminal normal: despide al usuario.

    Returns:
        None: No hay próximo estado, el bucle principal corta acá.
    """
    print("\nGracias por usar el sistema. ¡Hasta luego!")
    return None


# ─────────────────────────────────────────
#  TABLA DE TRANSICIÓN DE ESTADOS
# ─────────────────────────────────────────
# Diccionario de funciones: cada estado es una clave, y su valor es
# la función que se ejecuta al entrar a ese estado. Cada función
# devuelve el nombre (string) del próximo estado.
ESTADOS = {
    "INICIO": estado_inicio,
    "PIDIENDO_LEGAJO": estado_pidiendo_legajo,
    "PIDIENDO_DIAS": estado_pidiendo_dias,
    "PROCESANDO_SOLICITUD": estado_procesando_solicitud,
    "PREGUNTANDO_REPETIR": estado_preguntando_repetir,
    "ERROR_FATAL": estado_error_fatal,
    "FIN": estado_fin,
}


# ─────────────────────────────────────────
#  MOTOR DE LA MÁQUINA DE ESTADOS
# ─────────────────────────────────────────

def main():
    """Punto de entrada: ejecuta la máquina de estados hasta llegar a FIN."""
    estado_actual = "INICIO"

    while estado_actual is not None:
        funcion_estado = ESTADOS[estado_actual]
        estado_actual = funcion_estado()


if __name__ == "__main__":
    main()