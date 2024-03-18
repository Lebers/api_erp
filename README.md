# Sistema de Gestión de Cajas y Carpetas

Este proyecto es un sistema de gestión de cajas y carpetas, construido con FastAPI, que permite realizar operaciones CRUD (Crear, Leer, Actualizar, Borrar) en cajas y carpetas, así como generar reportes basados en rangos de fechas.

## Configuración del Proyecto

Para ejecutar este proyecto localmente, necesitas tener Python instalado en tu máquina. Además, debes instalar las dependencias necesarias, que incluyen FastAPI y un conector para MySQL.

1. Clona el repositorio:
git clone <url-del-repositorio>

2. Instala las dependencias:
pip install -r requirements.txt

3. Configura tu base de datos MySQL y asegúrate de actualizar el archivo de configuración de la base de datos en `functions/db.py` con las credenciales correctas.

4. Ejecuta el servidor FastAPI:
uvicorn main:app --reload


## Uso del API

Una vez que el servidor esté ejecutando, puedes acceder a la documentación interactiva de la API en `http://localhost:8000/docs`.

### Endpoints de Reportes

Los endpoints para generar reportes son:

- **Reporte de Cajas**

`GET /reportes/cajas?fecha_inicio=AAAA-MM-DD&fecha_fin=AAAA-MM-DD`

Genera un reporte de cajas creadas entre las fechas especificadas.

- **Reporte de Carpetas**

`GET /reportes/carpetas?fecha_inicio=AAAA-MM-DD&fecha_fin=AAAA-MM-DD`

Genera un reporte de carpetas creadas entre las fechas especificadas.

### Ejemplo de Uso con Postman

Para generar un reporte de cajas entre el 17 de marzo de 2024 y el 18 de marzo de 2024:

1. Abre Postman y configura un request GET a `http://localhost:8000/reportes/cajas?fecha_inicio=2024-03-17&fecha_fin=2024-03-18`.

2. Envía el request y recibe la respuesta con los datos del reporte.

### Nota

Asegúrate de que las fechas se envíen en el formato `AAAA-MM-DD` para garantizar que la API procese correctamente la solicitud.

## Contribución

Si deseas contribuir a este proyecto, por favor haz un fork del repositorio y envía tus pull requests para revisión.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` en este repositorio para obtener más información.
