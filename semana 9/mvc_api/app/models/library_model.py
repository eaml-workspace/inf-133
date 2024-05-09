from database import db

class Library(db.Model):
    __tablename__="library"
    
    id= db.Column(db.Integer, primary_key=True)
    titulo=db.Column(db.String(100), nullable=False)
    autor=db.Column(db.String(100), nullable=False)
    edicion = db.Column(db.Integer, nullable=False)
    edicion = db.Column(db.Integer, nullable=False)
    disponibilidad = db.Column(db.Integer, nullable=False)
    
    def __init__(self, titulo,autor,edicion,disponibilidad):
        self.titulo=titulo
        self.autor=autor
        self.edicion=edicion
        self.disponibilidad=disponibilidad
    
    def save(self):
        db.session.add(self)
        db.session.commit()