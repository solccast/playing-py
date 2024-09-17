from src.core.database import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True)
    print(db.Model)
    def __repr__(self):
        return f"<#{self.id}, email= {self.email}>"
    
