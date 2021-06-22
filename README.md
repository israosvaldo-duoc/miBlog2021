# miBlog2021

Proyecto de Programación Web PGY3121 Duoc UC 2021

1. Crear Proyecto Django 
    django-admin startproject miBlog
    cd miBlog

2. Configuración mínima de settings del proyecto
    En el archivo settings configuro a español
    LANGUAGE_CODE = 'es'

    * AGREGAR ARCHIVO .gitignore en la raíz del proyecto.
      Se puede usar de ejemplo: djangowaves.com/tips-tricks/gitignore-for-a-django-project

3. Crear la app de django principal (core)
    python manage.py startapp core
    Agregar la app core al archivo settings en INSTALLED_APPS

4. Templates
    Dentro de la app core crear la carpeta templates y dentro de ella
    crear una carpeta core.
    Siempre en todas las app de django, 
    se debe respetar esta estructura: nombreApp/templates/nombreApp 
    - Creo el template home.html dentro de core/templates/core
    - En el archivo views.py que está en la app core, 
      agrego la función: 
        def home(request):
            return render(request,'core/home.html')

5. Agregar Urls
    Agregar el archivo urls.py a la carpeta core con el código:

    from django.urls import path
    from .views import home

    urlpatterns = [
        path('', home, name="home"),
    ]

    En el archivo urls.py general del proyecto agregar
    path('', include('core.urls')),
    al urlpatterns
    Recordar importar include junto con path

6. Archivos Estáticos
    Se debe crear una carpeta con la lógica similar a templates: nombreApp/static/nombreApp

    Dentro de esta carpeta crear una estructura ordenada con una carpeta css, js, img. 
    También se puede agregar otra lib para librerías externas.

    En el html del template de django, primero se debe cargar los archivos statics de la app
    {% load static %}
    
    Luego llamar al recurso usando {% static 'nombreApp/rut/recurso' %}
