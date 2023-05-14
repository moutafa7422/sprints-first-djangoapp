from django.shortcuts import render
from django.template import loader
from .models import Course

# Create your views here.
def cours_list(request):
    context = {}
    context["data"] = Course.objects.all()
    return render (request, "courses/courses.html", context)