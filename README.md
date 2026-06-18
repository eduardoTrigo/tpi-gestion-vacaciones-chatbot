# TPI - ORGANIZACIÓN EMPRESARIAL

## Automatización del Proceso de Gestión de Vacaciones mediante Chatbot

### Integrantes

* Eduardo Trigo
* Tomas Ignacio Acevedo Peña

---

## Descripción del Proyecto

Este Trabajo Práctico Integrador tiene como objetivo automatizar el proceso administrativo de gestión de vacaciones de una organización mediante un chatbot.

La solución fue diseñada utilizando BPMN 2.0 para modelar el proceso de negocio y posteriormente implementar una simulación funcional en Python que permite:

* Validar empleados mediante número de legajo.
* Consultar saldo de vacaciones disponible.
* Solicitar días de vacaciones.
* Aprobar o rechazar solicitudes automáticamente.
* Actualizar el saldo disponible.
* Gestionar errores de entrada del usuario.

---

## Objetivos

* Analizar un proceso administrativo real.
* Modelar el proceso utilizando BPMN 2.0.
* Implementar una solución automatizada.
* Aplicar conceptos de programación, bases de datos y gestión de procesos.
* Integrar conocimientos adquiridos durante la cursada.

---

## Tecnologías Utilizadas

* Python 3
* Pandas
* OpenPyXL
* Excel (Base de datos simulada)
* GitHub
* BPMN 2.0

---

## Estructura del Proyecto

tpi-gestion-vacaciones-chatbot/

├── datos/

│ └── empleados.xlsx

├── src/

│ └── chatbot_vacaciones.py

├── README.md

├── requirements.txt

├── DiagramasBPMN

└── .gitignore

---

## Base de Datos Simulada

El sistema utiliza un archivo Excel para representar la base de datos de empleados.

Campos utilizados:

* Legajo
* Nombre
* DiasDisponibles

---

## Flujo General

1. El usuario inicia la conversación.
2. Ingresa su número de legajo.
3. El sistema valida la existencia del empleado.
4. Se consulta el saldo disponible.
5. El usuario indica la cantidad de días solicitados.
6. El sistema evalúa la disponibilidad.
7. La solicitud es aprobada o rechazada.
8. Se informa el resultado final.

---

## Instalación

Clonar repositorio:

git clone tpi-gestion-vacaciones-chatbot

Ingresar al proyecto:

cd tpi-gestion-vacaciones-chatbot

Instalar dependencias:

pip install -r requirements.txt

---

## Ejecución

Ejecutar:

python src/chatbot_vacaciones.py

---

MANUAL DE USUARIO

Objetivo: Permitir a los empleados realizar solicitudes de vacaciones mediante un chatbot de forma rápida y sencilla.
Inicio del sistema
    1. Abrir la conversación con el chatbot.
    2. Ingresar el número de legajo solicitado.
    3. Verificar la cantidad de días disponibles informados por el sistema.
    4. Ingresar la cantidad de días de vacaciones deseados.
    5. Esperar la validación automática de la solicitud.

Posibles resultados

Solicitud aprobada:
    • El sistema registra la operación.
    • Se actualiza el saldo disponible.
    • Se informa la aprobación al empleado.

Solicitud rechazada:
    • El sistema informa el motivo del rechazo.
    • El saldo permanece sin modificaciones.

Recomendaciones
    • Ingresar únicamente valores numéricos.
    • Verificar el número de legajo antes de enviarlo.
    • Solicitar una cantidad de días igual o inferior al saldo disponible.

Mensajes de error contemplados
    • Legajo inexistente.
    • Cantidad de días inválida.
    • Saldo insuficiente.
    • Datos ingresados incorrectamente.

## Casos Contemplados

### Camino Feliz

* Legajo válido.
* Saldo suficiente.
* Solicitud aprobada.

### Camino Infeliz

* Legajo inexistente.
* Datos inválidos.
* Cantidad negativa.
* Saldo insuficiente.

---

## BPMN

El proyecto incluye:

* Modelo AS-IS (proceso actual).
* Modelo TO-BE (proceso automatizado).

---

## Materia

Organización Empresarial

Tecnicatura Universitaria en Programación

Universidad Tecnológica Nacional

---

## Autores



- Eduardo Trigo
- Tomas Ignacio Acevedo Peña
