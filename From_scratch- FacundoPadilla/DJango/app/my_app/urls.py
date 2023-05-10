from django.urls import path
from .views import index, greet

urlpatterns = [
    path('', index),
    path('<str:name>', greet)# en el path se pone el nombre de la variable que se va a recibir en la vista y luego se pone el nombre de la vista que se va a llamar
]
