from flask import render_template
from flask_login import current_user


# La función `list_animals` recibe una lista de library
# animales y renderiza el template `animales.html`
def list_librarys(librarys):
    return render_template(
        "librarys.html",
        librarys=librarys,
        title="Lista de libros",
        current_user=current_user,
    )


# La función `create_animal` renderiza el
# template `create_animal.html` o devuelve un JSON
# según la solicitud
def create_library():
    return render_template(
        "create_library.html", title="Crear Libro", current_user=current_user
    )


# La función `update_animal` recibe un animal
# y renderiza el template `update_animal.html`
def update_library(library):
    return render_template(
        "update_library.html",
        title="Editar Libro",
        library=library,
        current_user=current_user,
    )