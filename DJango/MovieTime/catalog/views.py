from django.shortcuts import render
from .models import Movies

# Create your views here.
def index(request):
    items = Movies.objects.all()
    context = {'items':items}
    return render(request, 'catalog/index.html', context)