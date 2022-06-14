from django.shortcuts import render
from .models import Familiar

def index(request):
    familiares = Familiar.objects.all()
    ctx = {"familiares" : familiares}
    return render(request,"aplicacion/index.html", ctx)