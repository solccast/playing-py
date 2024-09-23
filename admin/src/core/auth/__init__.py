from src.core.database import db
from src.core.auth.user import User
from src.core.bcrypt import bcrypt

def list_users():
    users = User.query.all()
    
    return users 



def create_user(**kwargs):
    '''
        Crea un usuario. Si incluye el parámetro password, lo hashea.
    '''

    #Encriptar antes de guardar 
    hash = bcrypt.generate_password_hash(kwargs["password"].encode("utf-8"))
    kwargs["password"] = hash.decode("utf-8")

    user = User(**kwargs)
    db.session.add(user)
    db.session.commit()
    return user 


def find_user_by_email(email):
    
    user = User.query.filter_by(email=email).first()
    
    return user


def check_user(email, password):
    user = find_user_by_email(email)

    if user and bcrypt.check_password_hash(user.password, password):
        return user
    
    return None