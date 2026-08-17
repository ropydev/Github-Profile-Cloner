#!/bin/python3

# Built with Love.
# Web version
# python -m src.web.app
# http://localhost:8000/

from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
import os
from ..lib import GithubProfileCloner

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open(os.path.abspath("src/web/static/index.html"), 'r') as f:
                content = f.read()
            self.wfile.write(content.encode())
        elif self.path == "/img/github-logo-G.png":
            self.send_response(200)
            self.send_header("Content-type", "image/png")
            self.end_headers()
            with open(os.path.abspath("src/web/img/github-logo-G.png"), 'rb') as f:
                content = f.read()
            self.wfile.write(content)

    def do_POST(self):
        if self.path == "/submit":
            style = """<style>
    * {
        background-color: rgb(22, 22, 22);
        color: #12da00;
        font-family: monospace;
    }
</style"""
            length = int(self.headers.get('Content-Length'))
            data = self.rfile.read(length).decode("utf-8")
            params = urllib.parse.parse_qs(data)
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            if params.get("owner", [""])[0] and params.get("token", [""])[0] and params.get("user", [""])[0] and params.get("email", [""])[0]:
                self.wfile.write("<h2>~$ Clonando usuario...</h2>".encode())
                clone = GithubProfileCloner.cloneProfile(params.get("owner", [""])[0], GithubProfileCloner.clonePath, params.get("token", [""])[0], params.get("user", [""])[0], params.get("email", [""])[0])
                if clone.get("error") == "false":
                    self.wfile.write("<h2>~$ Usuario clonado correctamente.</h2>".encode())
                elif clone.get("error") == "true":
                    self.wfile.write(f"<h2>~$ Ocurrio un error: {clone.get('msg')}</h2>".encode())
                else:
                    self.wfile.write("<h2>~$ Parece que mi codigo fue cambiado u ocurrio un error irreconocible en el codigo</h2>".encode())
            else:
                self.wfile.write(f"<h2>~$ Porfavor rellene todos los campos de texto.</h2>".encode())
            self.wfile.write(style.encode())

if __name__ == "__main__":
    server = HTTPServer(("localhost", 8000), MyHandler)
    print("Servidor corriendo en http://localhost:8000")
    server.serve_forever()
