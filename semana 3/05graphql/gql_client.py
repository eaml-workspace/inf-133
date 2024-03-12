import requests
# Definir la URL del servidor GraphQL
url = 'http://localhost:8000/graphql'

# Definir la consulta GraphQL para crear nuevo estudiante
query_crear = """
mutation {
        crearEstudiante(nombre: "Angel", apellido: "Gomez", carrera: "Arquitenctura") {
            estudiante {
                id
                nombre
                apellido
                carrera
            }
        }
    }
"""

response_mutation = requests.post(url, json={'query': query_crear})
print(response_mutation.text)

query_crear1 = """
mutation {
        crearEstudiante(nombre: "Angelo", apellido: "Perex", carrera: "Arquitenctura") {
            estudiante {
                id
                nombre
                apellido
                carrera
            }
        }
    }
"""

response_mutation = requests.post(url, json={'query': query_crear1})
print(response_mutation.text)

query_crear2 = """
mutation {
        crearEstudiante(nombre: "Angela", apellido: "Go", carrera: "Arquitenctura") {
            estudiante {
                id
                nombre
                apellido
                carrera
            }
        }
    }
"""

response_mutation = requests.post(url, json={'query': query_crear2})
print(response_mutation.text)

# Definir la consulta GraphQL con parametros
query = """
    {
        estudiantePorCarrera(carrera: "Arquitectura"){
            id
            nombre
            apellido
        }
    }
"""


url = 'http://localhost:8000/graphql'

# Solicitud POST al servidor GraphQL
response = requests.post(url, json={'query': query})
print(response.text)

# Definir la consulta GraphQL para eliminar un estudiante
query_eliminar = """
mutation {
        deleteEstudiante(id: 3) {
            estudiante {
                id
                nombre
                apellido
                carrera
            }
        }
    }
"""

response_mutation = requests.post(url, json={'query': query_eliminar})
print(response_mutation.text)

query_actualizar="""
mutation{
        actualizarEstudiante(id: 1, carrera: "Antropologia"){
            estudiante{
                id
                nombre
                apellido
                carrera
            }
        }
    }
"""

response_mutation = requests.post(url, json={'query': query_actualizar})
print(response_mutation.text)