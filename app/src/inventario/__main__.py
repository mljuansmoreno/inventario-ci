import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from . import __version__


def salud():
    return {"estado": "ok", "version": __version__}
