from django import forms
from django.forms import ModelForm, Textarea
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Textbook, Student

#Form structure for adding a textbook
class TextbookForm(ModelForm):
	class Meta:
		model = Textbook
		fields = ['title', 'author', 'isbn', 'course']

#Form structure for registering for an account
class StudentRegistration(UserCreationForm):
	password1 = forms.CharField(label = 'Password', widget = forms.PasswordInput)
	password2 = forms.CharField(label = 'Confirm Password', widget = forms.PasswordInput)
	
	class Meta:
		model = Student
		fields = ['username', 'email', 'password1', 'password2']

#Check if passwords match
	def clean_password2(self):
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("Passwords don't match")
		return password2

#Save user to database
	def save(self, commit = True):
		user = super().save(commit = False)
		user.set_password(self.cleaned_data['password1'])
		if commit:
			user.save()
		return user
		
#Form structure for logging in
class LoginForm(forms.Form):
	username = forms.CharField(label = "username")
	password = forms.CharField(label = "password", widget = forms.PasswordInput)
	class Meta:
		model= Student
		fields = ['username', 'password']
	
#User authentication
	def login(self):
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")
		user = authenticate(username=username, password=password)
		return user

