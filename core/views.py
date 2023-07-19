from django.shortcuts import render

# Create your views here.

# vista de la pagina de inicio
def indexView(request):
    return render(request, 'index.html', {})