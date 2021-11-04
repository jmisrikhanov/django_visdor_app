from django.shortcuts import render
from django.http import HttpResponse

from home.models import Teacher
from .forms import ContactForm
from django.contrib import messages


# Create your views here.

def home(request):
    
    teachers = Teacher.objects.all()
    

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Form has been sent")
    
    else:
        form = ContactForm()
        
    context = {
        "form":form,
        "teachers":teachers
    }
        
    return render(request, "home/index.html",context )

def about(request):
    return render(request, "home/about.html")

def teacher(request):
    
    teachers = Teacher.objects.all()
    
    contex = {
        
        "teachers":teachers
    }
    
    return render(request, "home/teacher.html", contex)

