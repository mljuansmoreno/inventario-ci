#!/bin/sh
set -eu
cd "$(dirname "$0")/.."
mkdir -p reportes
rm -f reportes/junit.xml
