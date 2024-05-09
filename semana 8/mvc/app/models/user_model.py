from database import db

class User(db.Model):
    __tablename__ = 'users'
    
    id= db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    contrasena = db.Column(db.String(50), nullable=False)
    fecha_nacimiento = db.Column(db.Date(), nullable=False)

    #Inicializa clase User
    def __init__(self, first_name, last_name, email, contrasena,fecha_nacimiento):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.contrasena=contrasena
        self.fecha_nacimiento=fecha_nacimiento

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return User.query.all()
    
    @staticmethod
    def get_by_id(id):
        return User.query.get(id)
    
    def update(self):
        db.session.commit()