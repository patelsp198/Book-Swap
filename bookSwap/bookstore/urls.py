from django.urls import path, include
from . import views

urlpatterns = [
	path(r'home/', views.index, name='index'),
	path(r'add/', views.add, name='add')
	path(r'list/', views.list, name='list'),
	path(r'registration/', views.register, name = 'register'),
	path(r'login/', views.UserLogin, name = 'login'),
	path(r'logout/', views.UserLogout, name = 'logout'),
	path(r'users/', views.DisplayUser, name = 'display'),
	path(r'my_books/', views.myBooks, name = 'my_books'),
	path(r'delete_book/(?P<pk>\d+)/', views.delete_book, name = 'delete_book'),
	path(r'delete_user/(?P<pk>\d+)/', views.delete_user, name = 'delete_user'),
]