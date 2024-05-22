from flask import Blueprint, request, jsonify
from models.dulce_model import Dulce
from views.dulce_view import render_dulce_list, render_dulce_detail
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from functools import wraps
from utils.decorators import jwt_required, roles_required

# Crear un blueprint para el controlador de animales
dulce_bp = Blueprint("dulce", __name__)

# Ruta para obtener la lista de animales
@dulce_bp.route("/dulces", methods=["GET"])
@jwt_required
@roles_required(roles=["admin","user"])
def get_dulces():
    dulces = Dulce.get_all()
    return jsonify(render_dulce_list(dulces))


# Ruta para obtener un animal específico por su ID
@dulce_bp.route("/dulces/<int:id>", methods=["GET"])
@jwt_required
@roles_required(roles=["admin"])
def get_dulce(id):
    dulce = Dulce.get_by_id(id)
    if dulce:
        return jsonify(render_dulce_detail(dulce))
    return jsonify({"error": "dulce no encontrado"}), 404


# Ruta para crear un nuevo animal
@dulce_bp.route("/dulces", methods=["POST"])
@jwt_required
@roles_required(roles=["admin"])
def create_animal():
    data = request.json
    marca = data.get("marca")
    peso= data.get("peso")
    origen = data.get("origen")
    sabor = data.get("sabor")

    # Validación simple de datos de entrada
    if not marca or not peso or not origen or not sabor is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    # Crear un nuevo animal y guardarlo en la base de datos
    dulce = Dulce(marca=marca, peso=peso, origen=origen, sabor=sabor)
    dulce.save()

    return jsonify(render_dulce_detail(dulce)), 201


# Ruta para actualizar un animal existente
@dulce_bp.route("/dulces/<int:id>", methods=["PUT"])
@jwt_required
def update_dulce(id):
    animal = Dulce.get_by_id(id)

    if not animal:
        return jsonify({"error": "dulce no encontrado"}), 404

    data = request.json
    marca = data.get("marca")
    peso= data.get("peso")
    origen = data.get("origen")
    sabor = data.get("sabor")

    # Actualizar los datos del animal
    animal.update(marca=marca, peso=peso, origen=origen, sabor=sabor)

    return jsonify(render_dulce_detail(animal))


# Ruta para eliminar un animal existente
@dulce_bp.route("/dulces/<int:id>", methods=["DELETE"])
@jwt_required
def delete_dulce(id):
    animal = Dulce.get_by_id(id)

    if not animal:
        return jsonify({"error": "Dulce no encontrado"}), 404

    # Eliminar el animal de la base de datos
    animal.delete()

    # Respuesta vacía con código de estado 204 (sin contenido)
    return "", 204