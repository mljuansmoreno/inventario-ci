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
        cuerpo = json.dumps(salud()).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(cuerpo)))
        self.end_headers()
        self.wfile.write(cuerpo)
