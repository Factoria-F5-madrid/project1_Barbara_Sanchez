# 🚕 Taxímetro Digital

## Descripción

El **Taxímetro Digital** es una innovadora aplicación diseñada para transformar la experiencia de los trayectos en taxi. Esta herramienta calcula automáticamente la tarifa de un trayecto en función del tiempo transcurrido y el estado del vehículo, ofreciendo una interfaz intuitiva y fácil de usar. Con características como tarifas dinámicas y un historial detallado de viajes, el Taxímetro Digital se posiciona como una solución moderna para conductores y pasajeros.

## Características Principales

- **Cálculo Automático de Tarifas**: Basado en el tiempo de movimiento y parada del vehículo.
- **Tarifas Dinámicas**: Ajuste de precios según la hora del día para reflejar la demanda.
- **Interfaz de Usuario Intuitiva**: Cambia dinámicamente entre mensajes de bienvenida y despedida.
- **Historial de Viajes**: Almacenamiento y visualización de trayectos pasados para un fácil seguimiento.
- **Autenticación de Usuarios**: Seguridad mejorada mediante un sistema de inicio de sesión.

## Instalación y Uso Local

Para comenzar a utilizar el Taxímetro Digital en tu máquina local, sigue estos pasos:

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/Barbarasanchez11/taximeter_Barbara_Sanchez
   cd taximetro-digital
   ```

2. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecutar la aplicación**:
   ```bash
   streamlit run app.py
   ```
   
   Alternativamente, puedes ejecutar la aplicación desde la línea de comandos:
   ```bash
   python main.py
   ```

## Arquitectura del Proyecto

El proyecto está desarrollado principalmente en **Python**, utilizando **Streamlit** para la interfaz web y **SQLite** para la gestión de la base de datos. La estructura del proyecto está organizada en módulos para facilitar el mantenimiento y la escalabilidad:

- **app/**: Contiene la lógica principal de la aplicación, incluyendo la interfaz de usuario y la gestión de trayectos.
- **data/**: Almacena los archivos de datos y registros.
- **test/**: Incluye pruebas unitarias para asegurar la calidad del código.
- **assets/**: Recursos estáticos como imágenes.

## Presentaciones y Recursos

- [Video de la Presentación](https://drive.google.com/file/d/1PUEliao7GZgfDvu9xkDh_rseVvrtWO0e/view?usp=sharing)
- [Presentación Técnica](https://drive.google.com/file/d/1DBk5mtKim1hqhitJlRqkehqHjVwTSxUV/view?usp=sharing)
- [Presentación No Técnica](https://drive.google.com/file/d/1u8R5Ey7MErLo8Z9vR2ZeW2RuzOdO8G4m/view?usp=sharing)
- [Tablero de Trello](https://trello.com/b/ZAkd0zvG/taximetro)
- [Aplicación Desplegada](https://barbarasanchez11-taximeter-project-appapp-s2mysf.streamlit.app/)

## Contribuciones

Las contribuciones son bienvenidas. Si deseas colaborar, por favor sigue estos pasos:

1. Haz un fork del proyecto.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -am 'Añadir nueva funcionalidad'`).
4. Sube tus cambios a la rama (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.

## Licencia

Este proyecto está bajo la Licencia MIT. Para más detalles, consulta el archivo `LICENSE`.

## Autor

- **Bárbara Sánchez**: [GitHub](https://github.com/Barbarasanchez11)

## Documentación y Fuentes

- [Documentación oficial de Python](https://docs.python.org/3/)
- [PEP 8 – Guía de estilo de Python](https://peps.python.org/pep-0008/)
- [Streamlit](https://docs.streamlit.io/)

## Dockerización

Debido a limitaciones técnicas específicas del entorno local, no fue posible ejecutar Docker correctamente en este sistema. El entorno de desarrollo cuenta con:

- macOS 12 (versión fuera del soporte oficial de Homebrew, "Tier 3")
- Python 3.13 (versión muy reciente con incompatibilidades en scripts de construcción de QEMU)

Durante la instalación del entorno necesario para ejecutar Docker (Colima + QEMU), ocurrió el siguiente error al llegar a QEMU:

```
AttributeError: module 'pip._vendor.distlib' has no attribute 'scripts'
ERROR: python venv creation failed
```

Este error es conocido y ha sido reportado en múltiples foros, ya que QEMU no soporta correctamente la creación de entornos virtuales con Python 3.13 aún.

Si el sistema hubiera estado basado en Python 3.10 o 3.11 y un macOS más reciente (13+), el entorno Docker podría haberse ejecutado sin inconvenientes.

### Instrucciones para ejecutar con Docker en otro entorno compatible

Una vez clonado el repositorio:

```bash
docker build -t taximeter-app .
docker run -p 8501:8501 taximeter-app
```

Y acceder a la aplicación desde el navegador en:

[http://localhost:8501](http://localhost:8501)



