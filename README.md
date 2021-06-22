# miBlog2021

Proyecto de Programación Web PGY3121 Duoc UC 2021

Para usar este repositorio
    Descargar o clonar, luego ejecutar la instalación de los paquetes de requirements.txt con:
    pip install -r requirements.txt

Para crear el archivo requirements.txt
    Antes de enviar su propio proyecto, en la raíz del proyecto debe ejecutar:
    pip freeze > requirements.txt

Crear proyecto django
    Por consola
        django-admin startproject miBlog
    Desde este punto en adelante siempre se debe trabajar dentro de la carpeta del proyecto
                miBlog
        │   manage.py      
        │   .gitignore     
        │
        └───miBlog
        │   │   settings.py
        │   │   urls.py
        │ (..y mas)

Agregar archivo .gitignore
    En la raíz del proyecto, antes de subir al repositorio por primera vez.
    Se puede usar de ejemplo: https://djangowaves.com/tips-tricks/gitignore-for-a-django-project/

1.- Configuración mínima de settings del proyecto
    En el archivo settings del proyecto configuro a español
        LANGUAGE_CODE = 'es'

    Primer migrate
    Para crear las bases de datos básicas propias de django
        python manage.py migrate

    Levantar el servidor
        python manage.py runserver

2.- Crear la app de django principal (core)
        python manage.py startapp core

    Agregar la app core a settings en la lista:
        INSTALLED_APPS = [
            ...
            'core',
        ]

3.- Templates
    Dentro de la app core, crear la carpeta templates y dentro de la carpeta templates crear una carpata core
        miBlog    
        └───core
        │   └───templates
        │       └───core
    
    Siempre en todas las app de django, se debe respetar esta estructura nombreApp/templates/nombreApp

    1) Creo el template
        Por ejemplo home.html dentro de core/templates/core
            └───core
            │   │   views.py 
            │   └───templates
            │       └───core
            │           │   home.html 
    
    2) Agrego función en views.py
        Que esta en la app core, agrego la función:
            def home(request):
                return render(request, 'core/home.html')

    3) Agrear Urls
        Agregar el archivo urls.py a la carpeta core
            └───core
            │   │   urls.py
            │   │   views.py 
            │   └───templates
            │       └───core
            │           │   home.html 

        Con el código:
            from django.urls import path
            from .views import home

            urlpatterns = [
                path('', home, name="home"),
            ]
        
        Archivo urls.py general
            Donde están los settings del proyecto, también está el archivo central de urls, se debe agregar:
                path('', include('core.urls')),
            
            Al listado de urlpatterns Recuerden importar include, en la misma linea de path

4.- Archivos Estáticos
        Se debe crear una carpeta con la lógica similar a templates nombreApp/static/nombreApp. Dentro de esta carpeta crear una estructura ordenda con una carpeta css, otra js y otra img. También se puede agregar otra lib para librerías externas, etc.

            └───core
            │   │   urls.py
            │   │   views.py 
            │   │
            │   └───templates
            │   │   └───core
            │   │       │   home.html 
            │   │       
            │   └───static
            │       └───core
            │           └───css
            │           └───img
            │           └───js

        Cargar archivos static en el template
            En el html del template de django, primero se debe indicar  
                {% load static %}

        Luego llamar al recurso usando
            {% static 'nombreApp/rut/del/recurso' %}

5.- Envío de variables
    Se utiliza desde el views.py en el tercer parámetro del render, llamado contexto, que es de tipo diccionario
        contexto = {
                'atributo': 'valor'
            }
            return render(request, 'core/home.html', contexto)

    Y para llamarlas en el template se utiliza {{ atributo }}
