"""UKpraca URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from UKpracaApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('first/', include('UKpracaApp.urls')),
    path('', views.homepage, name="homepage"),
    path('base/', views.base_view),
    path('list/', views.get_user_name, name='insert_praca_user'),
    path('home/', views.homepage),
    path('contact/', views.contact_view),
    path('create-user/', views.createUser, name="create-user"),




]


# OLD URLS
#
# urlpatterns = [
#     path('list/', views.list_workers_items),
#     path('insert_praca/',views.insert_praca_user, name='insert_praca_user'),