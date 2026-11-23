# Un pipeline, dos motores

Laboratorio de inventario del escenario 4. Jenkins y GitHub Actions verifican el mismo código Python.

## Dónde está cada pieza

El paquete, sus siete pruebas y la imagen viven en `app/`. El controlador de Jenkins se construye desde `jenkins/`.

Jenkins carga [app/Jenkinsfile](app/Jenkinsfile). GitHub descubre el flujo en [.github/workflows/ci.yml](.github/workflows/ci.yml), en la raíz del repositorio.

## Preparar el laboratorio

Usa Git y Docker con contenedores Linux. Reserva unos 4 GB de memoria y al menos 2 GB de disco. El primer build descarga imágenes y plugins.

Puedes adelantar la descarga de la imagen común con `docker pull python:3.12-slim`.

Desde `jenkins/`, copia `.env.example` a `.env` y define una clave para `estudiante`. Git ignora ese archivo.

Arranca el controlador con `docker compose up -d --build`. Sigue el inicio con `docker compose logs -f jenkins` hasta leer `Jenkins is fully up and running`.

Abre [Jenkins local](http://localhost:8080) e ingresa como `estudiante` con la clave del entorno. El valor de clase por defecto es `cambiar-esta-clave`.

JCasC establece el mensaje del curso y Job DSL crea **inventario**. El job lee `app/Jenkinsfile` desde Git en la rama `main`.

Abre **inventario → Construir ahora**. La vista de etapas muestra **Pruebas unitarias**, **Construir imagen** y **Prueba de humo**.

Para usar tu copia de Git, ejecuta desde `jenkins/` el comando `docker compose -f docker-compose.yml -f compose.local.yml up -d --build`. El job construye la última revisión confirmada de `main`.

## Qué valida el pipeline

El script de pruebas crea un contenedor Python 3.12, copia la aplicación, instala pytest y arranca el proceso. Recupera el XML de JUnit antes de eliminar el contenedor.

El humo arranca la imagen y consulta `GET /salud` por HTTP dentro del contenedor. Comprueba el estado y la versión y escribe `{"estado": "ok", "version": "1.0.0"}` en la consola.

En `app/src/inventario/core.py`, cambiar la resta de `retirar` por una suma deja 11 unidades al retirar 3 de 8. La prueba `test_retirar_descuenta` espera 5. La construcción de la imagen y el humo quedan omitidos.

Restaurar `-=` recupera el descuento. Confirma la corrección, publica en `main` y vuelve a construir el job para ver los dos resultados en el historial.
