import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from . import __version__


def salud():
    return {"estado": "ok", "version": __version__}


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != "/salud":
            self.send_error(404)
            return
