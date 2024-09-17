from src.core.database import db 

class Cat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    weight = db.Column(db.Integer)

    def __repr__(self):
        return f"<Cat #{self.id}, Nombre: {self.name}>"