from dotenv import load_dotenv
import os
load_dotenv()

class Config(object):
    """Base configuration"""
    
    SECRET_KEY = "secret"
    TESTING = False
    SESSION_TYPE = "filesystem" #Esto es lo que indica el backend que usará para guardar la sesión
    
    
class ProductionConfig(Config):
    """Production configuration."""
    #SQLALCHEMY_DATABASE_URI = None
    #Acá hay que hacer lo mismo que con development config pero tomando el nombre de las variables de vault
    pass


class DevelopmentConfig(Config):
    """Production configuration."""
    
    DB_USER= os.getenv("db_user")
    DB_HOST= os.getenv("db_host")
    DB_PASSWORD= os.getenv("db_password")
    DB_NAME=os.getenv("db_name")
    DB_PORT=os.getenv("db_port")
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )



class TestingConfig(Config):
    """Production configuration."""
    
    TESTING = True
    
    
config  = {
    "production": ProductionConfig,
    "development": DevelopmentConfig,
    "test": TestingConfig,
}

