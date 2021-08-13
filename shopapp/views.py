from django.shortcuts import render
from main.models import Shop, Point

# Create your views here.
def shop(request):
    return render(request, 'shopapp/shop.html')