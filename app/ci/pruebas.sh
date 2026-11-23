#!/bin/sh
set -eu
cd "$(dirname "$0")/.."
mkdir -p reportes
rm -f reportes/junit.xml
contenedor=$(docker create -w /curso python:3.12-slim sh -ec '
    pip install --disable-pip-version-check -r requirements-test.txt
    python -m pytest -q --junitxml=/curso/reportes/junit.xml
')
trap 'docker rm -f "$contenedor" >/dev/null' EXIT
for entrada in src tests pytest.ini requirements-test.txt; do
    docker cp "$entrada" "$contenedor:/curso/"
done
docker start -a "$contenedor" || true
resultado=$(docker inspect -f '{{.State.ExitCode}}' "$contenedor")
docker cp "$contenedor:/curso/reportes/junit.xml" reportes/junit.xml
exit "$resultado"
