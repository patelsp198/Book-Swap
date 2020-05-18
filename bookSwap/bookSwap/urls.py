"""bookSwap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import include, path
from django.views.generic.base import RedirectView
from bookstore import views
from bookstore.views import BookListView

urlpatterns = [
	path(r'home/', views.index, name='index'),
    path(r'admin/', admin.site.urls),
    path(r'add/' , views.add , name='add'),
    path(r'list/', views.list , name = 'list'),
    path(r'registration/', views.register, name = 'register'),
    path(r'login/', views.UserLogin, name = 'login'),
    path(r'logout', views.UserLogout, name = 'logout'),
    path(r'users/', views.DisplayUser, name = 'display'),
    path(r'my_books/', views.myBooks, name = 'my_books'),
    path(r'delete_book/(?P<pk>\d+)/', views.delete_book, name = 'delete_book'),
    path(r'delete_user/(?P<pk>\d+)/', views.delete_user, name = 'delete_user'),
    path('', RedirectView.as_view(url='/home')),
]
