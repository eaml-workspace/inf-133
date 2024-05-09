##Set-ExecutionPolicy Unrestricted -Scope Process
from http.server import HTTPServer
from pysimplesoap.server import SoapDispatcher, SOAPHandler

def saludar(nombre):
    return "¡Hola, {}!".format(nombre)

def suma(numero1,numero2):
    c=numero1+numero2
    return c

def palindromo(cadena):
    cadena = cadena.lower().replace(" ","")
    if cadena==cadena[::-1]:
        return True
    else:
        return False

dispatcher = SoapDispatcher(
    "ejemplo-soap-server",
    location="http://localhost:8000/",
    action= "http://localhost:8000/",
    namespace="http://localhost:8000/",
    trace=True,
    ns=True,
)

dispatcher.register_function(
    "Saludar",
    saludar,
    returns= {"saludo": str},
    args={"nombre": str},
)

dispatcher.register_function(
    "SumaDosNumeros",
    suma,
    returns= {"suma": int},
    args={"numero1": int, "numero2": int},
)

dispatcher.register_function(
    "CadenaPalindromo",
    palindromo,
    returns= {"palindromo": bool},
    args={"cadena": str},
)

server = HTTPServer(("0.0.0.0", 8000), SOAPHandler)
server.dispatcher = dispatcher
print("Servidor SOAP Iniciando en http://localhost:8000/")
server.serve_forever()