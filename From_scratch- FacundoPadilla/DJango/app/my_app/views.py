from django.shortcuts import render
from .models import Person

# Create your views here.
def index(request):
    return render(request, "app/base.html", {"personas" : Person.objects.all()}) # acqa se vincula el html con la vista

def greet(request, name):
    return render(request, "app/greet.html", {
        "name": name.capitalize()
    })