from http.server import HTTPServer, BaseHTTPRequestHandler
import json

estudiantes=[
    {
        "id":1,
        "nombre":"Pepe",
        "apellido":"Domingo"
        "carrera":"Informatica",
    }
]

class RESTRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/lista.estudiantes":
            self
            #...
            
def run_server(port=8000):
    try:
        server_adress =('', port)
        