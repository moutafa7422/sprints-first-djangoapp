from django.shortcuts import render
from django.template import loader
from .models import student
from django.views.generic import CreateView, UpdateView, DeleteView

# Create your views here.
def list_view(request):
    context = {}
    context["dataset"] = student.objects.all()
    return render (request, "students/list_view.html", context)