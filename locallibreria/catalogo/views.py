from django.shortcuts import render
from . models import  Cliente
from django.views import generic

# Create your views here.
def index(request):
    num_clientes = Cliente.objects.count()

    return render(
        request,
        'index.html',
        context={ 'num_clientes': num_clientes},
    )