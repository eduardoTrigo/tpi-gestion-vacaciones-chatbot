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



Eduardo Trigo
Tomas Ignacio Acevedo Peña
