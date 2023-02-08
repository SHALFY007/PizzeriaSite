from django.shortcuts import render
from .models import Pizza
# Create your views here.
def index(request):
    # Home page
    return render(request, 'pizzerias/index.html')

def pizzas(request):
    # Pizzas page
    pizzas = Pizza.objects.filter()
    context = {'pizzas': pizzas}
    return render(request, 'pizzerias/pizzas.html', context)

def pizza(request, pizza_id):
    #Pizza page
    pizza = Pizza.objects.get(id=pizza_id)
    topics = pizza.topping_set.filter()
    context = {'pizza': pizza, 'topics': topics}
    return render(request, 'pizzerias/pizza.html', context)