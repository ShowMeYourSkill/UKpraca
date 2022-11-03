from django.shortcuts import render, redirect

from django.http import HttpResponse, HttpRequest
from .models import User
from .forms import UserForm


# def index(response):
#     return HttpResponse("<h1>Witaj, pomożemy Ci znaleźć  pracę, </h1>")


def list_view(request):
    return render(request, 'UKpracaApp/index.html')

def base_view(request: HttpRequest):
    return render(request, 'UKpracaApp/base.html')          # do testów basea

def homepage(request):
    return render(request, 'UKpracaApp/home.html')

def contact_view(request):
    return render(request, 'UKpracaApp/contact.html')





def insert_praca_user(request: HttpRequest):
    goahead = User(name=request.POST['name'])
    #goahead = User(surname=request.POST['surname'])
    #goahead = User(experience=request.POST['experience'])
    #goahead = User(preferences=request.POST['preferences'])
    goahead.save()

    return redirect('list/')

def createUser(request):
    form = UserForm()

    context = {'form': form}
    return render(request, 'UKpraca/index.html', context)





    #goahead = User(request.POST['name'])
    #goahead.save()
    #return redirect('/first/list/')

# return render(request, 'UKpracaApp/index.html)
