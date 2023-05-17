from django.shortcuts import render
from django.template import loader
from .models import student
from .models import login
from .forms import LoginForm


# Create your views here.
def list_view(request):
    context = {}
    context["dataset"] = student.objects.all()
    return render (request, "students/list_view.html", context)  



#def login(request):
    """
    username = request.POST.get('u_name')
    pwd = request.POST.get('password')
    data = login(username = username, password = pwd)
    """
    
def home_view(request):

    form = LoginForm(request.POST)
    if form.is_valid():
        pass
        
    context ={}
    context['form']= LoginForm()
    return render(request, "students/login.html", context)

    #return render(request, "students/login.html", {'lf:LoginForm'})