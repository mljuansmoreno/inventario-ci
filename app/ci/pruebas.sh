#!/bin/sh
set -eu
cd "$(dirname "$0")/.."
mkdir -p reportes
rm -f reportes/junit.xml
contenedor=$(docker create -w /curso python:3.12-slim sh -ec '
    pip install --disable-pip-version-check -r requirements-test.txt
    python -m pytest -q --junitxml=/curso/reportes/junit.xml
')
