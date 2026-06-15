import pandas as pd

# Cargar base de datos simulada
archivo = "datos/empleados.xlsx"

try:
    empleados = pd.read_excel(archivo)
except FileNotFoundError:
    print("Error: no se encontró el archivo empleados.xlsx")
    exit()

print("=" * 40)
print("SISTEMA DE GESTIÓN DE VACACIONES")
print("=" * 40)

# Solicitar legajo
legajo = input("Ingrese su número de legajo: ")

# Validar que sean números
if not legajo.isdigit():
    print("Error: debe ingresar solamente números.")
    exit()

legajo = int(legajo)

# Buscar empleado
empleado = empleados[empleados["Legajo"] == legajo]

# Validar existencia
if empleado.empty:
    print("Error: el legajo no existe.")
    exit()

# Obtener datos
nombre = empleado.iloc[0]["Nombre"]
saldo = empleado.iloc[0]["DiasDisponibles"]

print(f"\nEmpleado: {nombre}")
print(f"Días disponibles: {saldo}")

# Solicitar días
dias = input("¿Cuántos días desea solicitar?: ")

if not dias.isdigit():
    print("Error: debe ingresar un número válido.")
    exit()

dias = int(dias)

if dias <= 0:
    print("Error: la cantidad debe ser mayor que cero.")
    exit()

# Gateway BPMN
if dias <= saldo:

    nuevo_saldo = saldo - dias

    empleados.loc[
        empleados["Legajo"] == legajo,
        "DiasDisponibles"
    ] = nuevo_saldo

    empleados.to_excel(
        archivo,
        index=False
    )

    print("\nSolicitud APROBADA")
    print(f"Nuevo saldo disponible: {nuevo_saldo}")

else:

    print("\nSolicitud RECHAZADA")
    print("No posee días suficientes.")