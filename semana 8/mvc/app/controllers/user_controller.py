from flask import Blueprint, request, redirect, url_for
from views import user_view
from models.user_model import User

user_bp= Blueprint('user', __name__)
@user_bp.route('/')
def usuarios():
    users = User.get_all()
    return user_view.usuarios(users)

@user_bp.route('/users', methods=['GET','POST'])
def registro():
    if request.method == 'POST':
        # Obtenemos los datos del formulario
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        contrasena = request.form['contrasena']
        fecha_nacimiento = request.form['fecha_nacimiento']
        # Creamos un nuevo usuario
        user = User(first_name, last_name, email, contrasena, fecha_nacimiento)
        # Guardamos el usuario
        user.save()
        # Redirigimos a la vista de usuarios
        return redirect(url_for('user.usuarios'))
    # Llamamos a la vista de registro
    return user_view.registro()