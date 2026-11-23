#!/bin/sh
set -eu
cd "$(dirname "$0")"
contenedor=$(docker run -d "${1:?Indique la imagen}")
trap 'docker rm -f "$contenedor" >/dev/null' EXIT
docker exec -i "$contenedor" python - < salud.py
