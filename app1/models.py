from django.db import models
import datetime
import re

class UserManager (models.Manager):
    def basic_validator_signup(self, postdata):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postdata['firstname']) <= 5:  
            errors["firstname"] = "First name should be at least 5 characters"
        if len(postdata['lastname']) < 10:
            errors["lastname"] = "Lastname should be at least 10 characters"  
        if not EMAIL_REGEX.match(postdata['email']):  
            errors["email"] = "It is not an email"
        return errors

class User(models.Model):
    firstname = models.CharField(max_length=45)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=65)
    phonenumber = models.CharField(max_length=10)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)  
    objects = UserManager()  
    #appointments
    #movies
    #movies = models.ManyToManyField( Movie,  related_name="users")

class Appointments(models.Model):
    Taskname = models.TextField(max_length=255)
    Taskdate = models.DateTimeField(blank=True, null=True)    
    Taskuser = models.ForeignKey(User, related_name="appointments", default=1,on_delete = models.DO_NOTHING)

class Movie(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField()
    release_date = models.DateTimeField()
    duration = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ManyToManyField(User,  related_name="movies")

class Films(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField()
    release_date = models.DateTimeField()
    duration = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ManyToManyField(User,  related_name="films")



def get_all_users(request):
    #movies = Movie.objects.get(id = 1)
    return Movie.objects.all()

def create_new_user(request):
        firstname = request.POST['firstname']
       
        email = request.POST['email']
        password = request.POST['password']
        description = request.POST['description']
        phonenumber = request.POST['phonenumber']
        User.objects.create(firstname = firstname,email=email,password=password,description=description,phonenumber=phonenumber )


def insertnewtask(request):
    TaskName = request.POST['taskname']
    TaskDate = datetime.datetime.now()
    UserId = 3

    
    #Movie.objects.create(title="Inception",description="Test123", release_date= TaskDate, duration= 300 )
   
    TaskUser = User.objects.get(id=UserId)
    movie_ = Movie.objects.get(id=3)
    
   

    #TaskUser.movies.add(movie_)
    movie_.user.add(TaskUser)
    Appointments.objects.create( Taskname=TaskName,Taskdate=TaskDate , Taskuser = TaskUser )

def getusername():
    User_ = User.objects.get(id = 3)
    return User_.email