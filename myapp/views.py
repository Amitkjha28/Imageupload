from django.shortcuts import render

from .forms import myform
from .models import Image

# Create your views here.

def index(request):
    if request.method =="POST":
        form = myform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    form = myform()
    pic = Image.objects.all()
    return render(request,"index.html",{'fm':form,'pic':pic})