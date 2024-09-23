from src.core import auth
from src.core import cats

def run():
    """
        La idea de este metodo es crear datos prefijados en la base de datos de modo que no haya que 
        crearlos de cero a mano ;)
    """
    test_user = auth.create_user(
        id=4,
        name="Giovanni",
        email="giovanni.giorgio@gmail.com",
        password="123456"
    )

    test_cat = cats.create_cat(
        id=1,
        name="Napoleon",
        weight=7
    )


    print("User creado y catito creado")
