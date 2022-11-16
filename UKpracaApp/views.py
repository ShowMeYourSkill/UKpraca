from django.shortcuts import render, redirect

from django.http import HttpResponse, HttpRequest
from .models import User
from .forms import UserForm
from django.http import HttpResponse


# def index(response):
#     return HttpResponse("<h1>Witaj, pomożemy Ci znaleźć  pracę, </h1>")


def list_view(request):
    return render(request, 'UKpracaApp/index.html')


def base_view(request: HttpRequest):
    return render(request, 'UKpracaApp/base.html')  # do testów basea


def homepage(request):
    return render(request, 'UKpracaApp/home.html')


def contact_view(request):
    return render(request, 'UKpracaApp/contact.html')


def insert_praca_user(request: HttpRequest):
    goahead = User(userName=request.POST['userName'])
    goahead = User(userSurname=request.POST['userSurname'])
    # goahead = User(experience=request.POST['experience'])
    # goahead = User(preferences=request.POST['preferences'])
    goahead.save()

    return redirect('list/')


def createUser(request):
    form = UserForm()

    context = {'form': form}
    return render(request, 'UKpracaApp/index.html', context)

    # goahead = User(request.POST['name'])
    # goahead.save()
    # return redirect('/first/list/')


# return render(request, 'UKpracaApp/index.html)


# def get_user_name(request):
#     if request.method == "POST":
#         name = request.POST.get("userName")  # jeśli nie ma, to None
#         surname = request.POST.get("userSurname")  # jeśli nie ma to None
#         if name and surname:
#             html = "<html><body>Zalogowany {} {}</body></html>".format(name,
#                                                                        surname)
#         else:
#             html = "<html><body>Błąd!</body></html>"
#         return HttpResponse(html)
#     else:
#         return render(request, 'UKpracaApp/index.html')

def get_user_name(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/list")
            except:
                pass
    else:
        form = UserForm()
    return render(request, "UKpracaApp/index.html")