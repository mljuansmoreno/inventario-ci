# Un pipeline, dos motores

Laboratorio de inventario del escenario 4. Jenkins y GitHub Actions verifican el mismo código Python.

## Dónde está cada pieza

El paquete, sus siete pruebas y la imagen viven en `app/`. El controlador de Jenkins se construye desde `jenkins/`.

Jenkins carga [app/Jenkinsfile](app/Jenkinsfile). GitHub descubre el flujo en [.github/workflows/ci.yml](.github/workflows/ci.yml), en la raíz del repositorio.
