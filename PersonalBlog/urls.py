"""PersonalBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,re_path
from blog.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('^$',index),
    re_path('details/(\w+)/',details),
    path('login/',login),
    path('register/',register),
    path('logout/',logout),
    re_path('booklist/(\w+)/(\d+)/',book_list),
    re_path('home/(\d+)',prefack_home),
    path('ajax_data',ajax_data),
    re_path('search/(\w+)',search)
]
