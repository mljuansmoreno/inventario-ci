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
