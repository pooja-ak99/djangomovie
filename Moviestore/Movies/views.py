from django.shortcuts import render
from Movies.models import movie
from Movies.forms import movieform

def home(request):
    m = movie.objects.all()
    return render(request, 'home.html', {"films":m})

def add(request):
    form = movieform()
    if (request.method == "POST"):
        form = movieform(request.POST, request.FILES)
        if (form.is_valid()):
            form.save()
        return home(request)
    return render(request, 'add.html', {"form":form})

def more(request, q):
    m = movie.objects.get(id=q)
    return render(request, 'more.html', {"films":m})

def delete(request,q):
    m = movie.objects.get(id=q)
    m.delete()
    return render(request,'home.html')

def edit(request,q):
    m = movie.objects.get(id=q)
    form = movieform(instance=m)
    if(request.method=="POST"):
        form = movieform(request.POST,request.FILES,instance=m)
        if form.is_valid():
            form.save()
            return home(request)
    return render(request, 'add.html', {"form":form})
