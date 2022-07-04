from django.shortcuts import render

from .forms import myform
from .models import Image

# Create your views here.

def index(request):
    form = myform()
    return render(request,"index.html",{'fm':form})