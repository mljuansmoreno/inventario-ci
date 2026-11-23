#!/bin/sh
set -eu
cd "$(dirname "$0")"
contenedor=$(docker run -d "${1:?Indique la imagen}")
