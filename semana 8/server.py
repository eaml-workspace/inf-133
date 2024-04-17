from flask import Flask, request, jsonify
##en app vive el servidor
app = Flask(__name__)
##@es un decorador, en este caso @ asocia una ruta a una función
@app.route('/saludar', methods=['GET'])
def saludar():
    nombre = request.args.get('nombre')
    if not nombre:
        return(
            jsonify({'error':'Se requiere un nombre en los parámetros de la URL.'}),
            400,
        )
    return jsonify({'mensaje':f'¡Hola, {nombre}!'})

@app.route('/sumar')
def sumar():
    num1= request.args.get('num1')
    num2= request.args.get('num2')
    if not num1 or not num2:
        return(
            jsonify({'error':'Se requiere un numeros en los parámetros de la URL.'}),
            400,
        )
    return jsonify({'mensaje':f'¡Resultado: {int(num1)+int(num2)}!'})

@app.route('/palindromo')
def palindromo():
    cadena= request.args.get("cadena")
    if not cadena:
        return(
            jsonify({'error':'Se requiere un cadena en los parámetros de la URL.'}),
            400,
        )
    cadena=cadena.lower()
    if cadena==cadena[::-1]:
        return jsonify({'mensaje':f'¡{cadena} es palindromo!'})
    else:
        return jsonify({'mensaje':f'¡{cadena} NO es palindromo!'})

@app.route('/contar',methods=['GET'])
def contar():
    cadena= request.args.get('cadena')
    vocal= request.args.get('vocal')
    if not cadena or not vocal:
        return(
            jsonify({'error':'Se requiere un cadena o vocal en los parámetros de la URL.'}),
            400,
        )
    s=cadena.count(vocal)
    return jsonify({"mensaje": f"El número de {vocal} en {cadena} es {s}"})

if __name__ == '__main__':
    app.run()