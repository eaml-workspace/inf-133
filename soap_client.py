from zeep import Client

client = Client('http://localhost:8000')

result = client.service.Saludar(nombre="Emanuel")
print(result)

result = client.service.CadenaPalindromo(cadena="Emanuel")
print(result)

result = client.service.SumaDosNumeros(numero1=1, numero2=2)
print(result)
