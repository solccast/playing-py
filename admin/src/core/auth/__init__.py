from src.core.database import db
from src.core.auth.user import User

def list_users():
    users = User.query.all()
    
    return users 



def create_user(**kwargs):
    '''
        Crea un usuario. Si incluye el parámetro password, lo hashea.
    '''

    user = User(**kwargs)
    db.session.add(user)
    db.session.commit()
    return user