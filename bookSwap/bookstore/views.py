from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django_tables2 import SingleTableView, SingleTableMixin
from django_filters.views import FilterView
from .models import Textbook, TextbookTable, Student, 	UserTable
from .forms import TextbookForm, StudentRegistration, LoginForm
import django_filters

# Create your views here.

#View for homepage.
def index(request):
	return render(request, 'homepage.html')

#View for listing a book.
@login_required(login_url='login')
def add(request):
	if request.method == 'POST':
		form = TextbookForm(request.POST)
		if form.is_valid():
			obj = form.save(request.POST)
			obj.owner = request.user.username
			obj.save()
			return redirect('my_books')

	form = TextbookForm()
	return render(request, 'add_book.html', {'form':form})

#Creating a filter for when viewing listings.
class TextbookFilter(django_filters.FilterSet):
	class Meta:
		model = Textbook
		fields = {
			'title': ['contains'],
			'author': ['contains'],
			'isbn': ['exact'],
			'course': ['contains'],
		}

#Template for table of books.
class BookListView(SingleTableMixin, FilterView):
	model= Textbook
	table_class = TextbookTable
	template_name = 'book_list.html'
	filterset_class = TextbookFilter

#Request book listing page
def list(request):
	books = TextbookTable(Textbook.objects.all())
	students = Student.objects.all()
	filter = TextbookFilter(request.GET, queryset=Textbook.objects.all())
	
	models= {
		'books':books,
		'filter':filter,
		'students':students,
	}	
	return render(request, 'book_list.html', models)

#Request register page
def register(request):
	form = StudentRegistration(request.POST or None)
	if form.is_valid():
		form.clean_password2()
		user = form.save()
		login(request, user)
		return render(request, 'homepage.html')
	form = StudentRegistration()
	return render(request, 'register.html', {'form':form})

#Request login page
def UserLogin(request):

#Pull given username and password
	form = LoginForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			username = form.cleaned_data.get("username")
			password = form.cleaned_data.get("password")
			user = authenticate(username=username, password=password)

		#Check if user exists
			if user is not None:
				login(request, user)
				return render(request, 'homepage.html')

		#Error if user does not exist
			else:
				messages.error(request, 'Username or password incorrect.')
	return render(request, 'login.html', {'form':form})

#Request to logout
def UserLogout(request):
	logout(request)
	return redirect('index')


#Request to view list of books owned by current user
#Must be logged in
@login_required(login_url='login')
def myBooks(request):
	books = Textbook.objects.filter(owner=request.user.username)
	return render(request, 'my_books.html', {'books':books})


#Request Display Users page to list registered users
#must be logged in and must be my own account otherwise
#error and redirect to homepage
@login_required(login_url='login')
def DisplayUser(request):
	students = Student.objects.all()
	user = request.user.username
	if user == 'patelsp198':
		return render(request, 'user_list.html', {'students':students})
	else: 
		messages.error(request, "You do not have permission to access this page.")
		return redirect('index')

#Helper function to delete books
def delete_book(request, pk):
	entry = get_object_or_404(Textbook, pk=pk)
	entry.delete()
	return redirect('my_books')

#Helper function to delete users
def delete_user(request, pk):
	entry = get_object_or_404(Student, pk=pk)
	books = Textbook.objects.filter(owner=entry.username)
	for book in books:
		book.delete()
	entry.delete()
	return redirect('display')
