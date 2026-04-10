# PyTask Manager

## Integrantes
* Viviana Polanco
* Junior Querales
* Josser Moreno

## Descripción breve
PyTask Manager es una aplicación de consola desarrollada en Python para la gestión eficiente de tareas personales.

## Instrucciones para ejecutar el programa
Para poner en marcha el sistema, siga estos pasos:

1. **Requisitos previos:** Asegúrese de tener instalado Python 3.x en su equipo.
2. **Descarga:** Clone este repositorio o descargue los archivos en una carpeta local.
3. **Ejecución:** Abra una terminal o consola de comandos dentro de la carpeta del proyecto y ejecute:
   ```bash
   python main.py

## Estructura general del sistema

* **`main.py`**: Es el punto de entrada de la aplicación. Se encarga de coordinar la carga de datos, iniciar el ciclo principal del menú y asegurar el guardado de la información al finalizar.
* **`modules/`**: Esta carpeta contiene la lógica de negocio dividida por funcionalidades:
    * `menu.py`: Gestiona la interfaz de usuario en consola y la navegación entre las distintas opciones.
    * `operaciones.py`: Contiene las funciones del CRUD (Registro, Listado, Búsqueda, Edición y Eliminación).
    * `validaciones.py`: Implementa el control de errores para asegurar que los datos ingresados por el usuario sean válidos.
    * `reportes.py`: Encargado de procesar los datos para mostrar resúmenes y estadísticas de las tareas.
* **`utils/`**: Funciones de utilidad técnica.
    * `archivos.py`: Contiene la lógica necesaria para la persistencia de datos (Lectura y Escritura del archivo JSON).
* **`data/`**: Directorio destinado al almacenamiento de información.
    * `tareas.json`: Archivo donde se guardan los registros de forma persistente.