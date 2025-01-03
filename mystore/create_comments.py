# traemos los paquetes genericos que no tengan que ver con Django
from faker import Faker

# Creamos la funcion para crear los comentarios 
def main():
    fake = Faker()
    for _ in range(5):
        comment = Comment.objects.create(
            text = fake.text()
            # se puede colocar la fecha 
            # elementos segun nuestra base
            )
    # Obtener los registros e imprimirlos
    comments = Comment.objects.all()
    print(f"Comentarios en el BD {comments.count()}")

# Cuando ejecutamos el script desde el interprete de python se corre if __name__ == '__main__':
if __name__ == '__main__':
    import os # variable de entorno 
    from django.core.wsgi import get_wsgi_application # 
    # varibale de entorno para indicar las configuraciones, nombre del proyecto y nombre del archivo
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mystore.settings')
    #establecer la funcion 
    application = get_wsgi_application()
    # ya se puede importar los elemtos de Django 
    from commets.models import Comment
    # llamamos la funcion main() para crear los comentarios
    main()