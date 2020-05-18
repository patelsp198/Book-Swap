from django.db import models
import django_tables2 as tables
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


#Defining the Textbook object
class Textbook(models.Model):
	title = models.CharField(max_length = 200)
	author = models.CharField(max_length = 200)
	isbn = models.IntegerField()
	course = models.CharField(max_length = 50)
	owner = models.CharField(max_length = 50)


#Defining the Course object || not finished/used
class Course(models.Model):
	name = models.CharField(max_length = 50)
	instructor = models.CharField(max_length = 50)
	dept = models.CharField(max_length=8)
	course_num = models.IntegerField()
	sect = models.IntegerField()

#Assists view with reading Textbooks
class TextbookTable(tables.Table):
	class Meta:
		model = Textbook
		fields=('title','author','isbn','course')


#Creates user object
class StudentManager(BaseUserManager):
	def create_user(self, email, username, password = None):
		user.selfmodel(email = email, username = username)
		user.set_password(password)
		user.save(using=self._db)
		return user

#Defining the user object
class Student(AbstractBaseUser):
	email = models.EmailField(unique = True)
	username = models.CharField(max_length=16, unique = True)

	objects = StudentManager()
	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email']

#Assists view with reading Users
class UserTable(tables.Table):
	class Meta:
		model = Student
		fields=('username','email')