from django.shortcuts import render

# Create your views here.
def home(request):

    lista_heroes = ['Batman', 'Captain America', 'Loki']

    contexto = {
        'nombre': 'Israel Acuña',
        'edad': 33,
        'heroes':lista_heroes
    }
    return render(request,'core/home.html', contexto)
