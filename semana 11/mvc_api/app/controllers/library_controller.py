from flask import Blueprint, request, redirect, url_for, flash, jsonify
#url_for, flash, jsonify son para el request
from flask_login import login_required, current_user
#flask_login es la autenticación más básica que se aloja en el navegador (COOKIES) para tokens debemos importar JWS
from models.library_model import Library
from views import library_view

# Importamos el decorador de roles
from utils.decorators import role_required

library_bp = Blueprint("library", __name__)

#Ambas clases de usuarios pueden acceder a la tabla de animales, solo deben estar logueados @login_required
@library_bp.route("/librarys")
@login_required
def list_library():
    librarys = Library.get_all()
    return library_view.list_librarys(librarys)

#Solo el admin puede crear animales @role_required("admin")
@library_bp.route("/librarys/create", methods=["GET", "POST"])
@login_required
@role_required("admin")
def create_library():
    if request.method == "POST":
        titulo = request.form["titulo"]
        autor = request.form["autor"]
        edicion = int(request.form["edicion"])
        disponibilidad = int(request.form["disponibilidad"])
        library = Library(titulo=titulo, autor=autor, edicion=edicion, disponibilidad=disponibilidad)
        library.save()
        flash("Libro creado exitosamente", "success")
        return redirect(url_for("library.list_librarys"))
    return library_view.create_library()


@library_bp.route("/libraryls/<int:id>/update", methods=["GET", "POST"])
@login_required
@role_required("admin")
def update_library(id):
    library = Library.get_by_id(id)
    if not library:
        return "Libro no encontrado", 404
    if request.method == "POST":
        if current_user.has_role("admin"):
            titulo = request.form["titulo"]
            autor = request.form["autor"]
            edicion = int(request.form["edicion"])
            disponibilidad = int(request.form["disponibilidad"])
            library.update(titulo=titulo, autor=autor, edicion=edicion, disponibilidad=disponibilidad)
            flash("Libro actualizado exitosamente", "success")
            return redirect(url_for("library.list_librarys"))
        else:
            return jsonify({"message": "Unauthorized"}), 403
    return library_view.update_library(library)


@library_bp.route("/librarys/<int:id>/delete")
@login_required
@role_required("admin")
def delete_library(id):
    library = Library.get_by_id(id)
    if not library:
        return "Libro no encontrado", 404
    library.delete()
    flash("Libro eliminado exitosamente", "success")
    return redirect(url_for("library.list_librarys"))#animal
    