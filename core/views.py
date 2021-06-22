from django.shortcuts import render

# Create your views here.
def home(request):
    contexto = {
        'nombre': 'Israel Acuña',
        'edad': 33
    }
    return render(request,'core/home.html', contexto)
