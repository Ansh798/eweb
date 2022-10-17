from django.shortcuts import render, HttpResponse
from .models import *
# Create your views here.
def index(request):
    rec = Product.objects.all()
    return render(request, 'index.html', {'rec': rec})

def product_info(request,d):
    n = Product.objects.get(id =d)
    return render(request, 'product_info.html', {'n': n})
