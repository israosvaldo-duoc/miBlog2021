from django.shortcuts import render

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        super().__init__()

# Create your views here.
def home(request):

    lista_heroes = ['Batman', 'Captain America', 'Loki']

    villano = Persona('Thanos', '45')

    contexto = {
        'nombre': 'Israel Acuña',
        'edad': 33,
        'heroes':lista_heroes,
        'villano': villano
    }

    return render(request,'core/home.html', contexto)
