# Proyecto Python: Taxímetro Digital

<img src="./assets/taxi-7433597_1280.jpg" alt="drawing" style="width:100%; max-height:300px; object-fit:cover;" />

## Descripción del Proyecto
Este proyecto consiste en desarrollar un prototipo de taxímetro digital utilizando Python. El objetivo es modernizar el sistema de facturación de los taxis y crear un sistema que calcule las tarifas a cobrar a los clientes de manera precisa y eficiente.

## Niveles de Implementación

### Nivel Esencial
- Desarrollar un programa CLI (Interfaz de Línea de Comandos) en Python.
- Al iniciar, el programa debe dar la bienvenida y explicar su funcionamiento.
- Implementar las siguientes funcionalidades básicas:
  - Iniciar un trayecto
  - Calcular tarifa mientras el taxi está parado (2 céntimos por segundo)
  - Calcular tarifa mientras el taxi está en movimiento (5 céntimos por segundo)
  - Finalizar un trayecto y mostrar el total en euros
  - Permitir iniciar un nuevo trayecto sin cerrar el programa

### Nivel Medio

- Implementar un sistema de logs para la trazabilidad del código.
- Agregar tests unitarios para asegurar el correcto funcionamiento del programa.
- Crear un registro histórico de trayectos pasados en un archivo de texto plano.
- Permitir la configuración de precios para adaptarse a la demanda actual.


### Nivel Avanzado

- Refactorizar el código utilizando un enfoque orientado a objetos (OOP).
- Implementar un sistema de autenticación con contraseñas para proteger el acceso al programa.
- Desarrollar una interfaz gráfica de usuario (GUI) para hacer el programa más amigable.


### Nivel Experto

- Integrar una base de datos para almacenar los registros de trayectos pasados.
- Dockerizar la aplicación para facilitar su despliegue y portabilidad.
- Desarrollar una versión web de la aplicación accesible a través de internet.


## Tecnologías a Utilizar

- Python
- Git y GitHub para control de versiones
- Trello o Jira para la gestión del proyecto
- Bibliotecas adicionales según el nivel de implementación (por ejemplo, logging, unittest, tkinter para GUI, SQLite para base de datos)
- Docker para containerización (nivel experto)
- Framework web como Flask o Django para la versión web (nivel experto)


## Entregables

1. Repositorio de GitHub con el código fuente del proyecto
2. Demostración del CLI desarrollado
3. Presentación para público no técnico
4. Presentación técnica del código, destacando fortalezas y debilidades
5. Enlace al tablero Kanban utilizado para la organización del proyecto


## Plazo de Entrega

Una semana a partir de la fecha de inicio del proyecto.

## Consejos para el Desarrollo

- Comienza con el nivel esencial y ve agregando funcionalidades gradualmente.
- Utiliza control de versiones desde el inicio del proyecto.
- Realiza pruebas frecuentes para asegurar el correcto funcionamiento en cada etapa.
- Documenta tu código y mantén un registro de los cambios y decisiones de diseño.
- Considera la usabilidad y la experiencia del usuario, incluso en la versión CLI.