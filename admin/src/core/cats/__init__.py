from src.core.cats.cat import Cat
from src.core.database import db

def create_cat(**kwargs): 
    new_cat = Cat(**kwargs)
    db.session.add(new_cat)
    db.session.commit()

    return new_cat