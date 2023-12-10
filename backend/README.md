# Servicios Backend para S4: S4: Shamir Secret Sharing Scheme

Para ejecutar el backend siga los siguientes pasos:

## Instalar [Python-3.12](https://www.python.org/downloads/)

## Activar entorno virtual main_env

Para activar el entorno virtual main_env abra una consola en el folder `backend` e ingrese el siguiente comando:

Si su equipo es Windows:

`.\main_env\Scripts\Activate.ps1`

Si su equipo es Linux/Mac: 

`source main_env/Scripts/Activate.bat` o `source main_env/Scripts/Activate`

## Instalar dependencias

una vez activado el entorno virtual para instalar dependencias desde una consola en el folder `backend` introduzca el siguiente comando:

`pip install -r requirements.txt`

## Ejecutar servidor en local

Ya instaladas las dependencias para ejecutar el servicio en local introduzca desde una consola en el folder `backend`: 

`flask --app app run`

Y el servicio iniciará en la consola. Es vital para la carpeta de `frontend` que el servicio esté escuchando en `http://127.0.0.1:5000` mientras el servicio de frontend esté activo para que la aplicación funcione con normalidad.

Si el proyecto de la carpeta `frontend` no está siendo ejecutado en consola, ir a las instrucciones de la carpeta `frontend` y siga los pasos para ejecutarlo.