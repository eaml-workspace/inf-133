from flask import Blueprint, request, redirect, url_for, flash, jsonify
#url_for, flash, jsonify son para el request
from flask_login import login_required, current_user
#flask_login es la autenticación más básica que se aloja en el navegador (COOKIES) para tokens debemos importar JWS
from models.animal_model import Animal
from views import animal_view

# Importamos el decorador de roles
from utils.decorators import role_required

animal_bp = Blueprint("animal", __name__)

#Ambas clases de usuarios pueden acceder a la tabla de animales, solo deben estar logueados @login_required
@animal_bp.route("/animals")
@login_required
def list_animals():
    animals = Animal.get_all()
    return animal_view.list_animals(animals)

#Solo el admin puede crear animales @role_required("admin")
@animal_bp.route("/animals/create", methods=["GET", "POST"])
@login_required
@role_required("admin")
def create_animal():
    if request.method == "POST":
        name = request.form["name"]
        species = request.form["species"]
        age = int(request.form["age"])
        animal = Animal(name=name, species=species, age=age)
        animal.save()
        flash("Animal creado exitosamente", "success")
        return redirect(url_for("animal.list_animals"))
    return animal_view.create_animal()


@animal_bp.route("/animals/<int:id>/update", methods=["GET", "POST"])
@login_required
@role_required("admin")
def update_animal(id):
    animal = Animal.get_by_id(id)
    if not animal:
        return "Animal no encontrado", 404
    if request.method == "POST":
        if current_user.has_role("admin"):
            name = request.form["name"]
            species = request.form["species"]
            age = int(request.form["age"])
            animal.update(name=name, species=species, age=age)
            flash("Animal actualizado exitosamente", "success")
            return redirect(url_for("animal.list_animals"))
        else:
            return jsonify({"message": "Unauthorized"}), 403
    return animal_view.update_animal(animal)


@animal_bp.route("/animals/<int:id>/delete")
@login_required
@role_required("admin")
def delete_animal(id):
    animal = Animal.get_by_id(id)
    if not animal:
        return "Animal no encontrado", 404
    if current_user.has_role("admin"):#No es necesario este if
        animal.delete()
        flash("Animal eliminado exitosamente", "success")
        return redirect(url_for("animal.list_animals"))
    else:
        return jsonify({"message": "Unauthorized"}), 403