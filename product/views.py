from django.shortcuts import render
from .models import Category, Drink

# Create your views here.

def main(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        return render(request, 'main.html', {'categories':categories})
    elif request.method == 'POST':

        return render(request, 'main.html')
