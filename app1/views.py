from django.shortcuts import render, redirect
from . import models  # import model is important 
from django.contrib import messages
from .models import User

# Create your views here.

def index(request):
    return render(request, "index.html")

def createuser(request, id):
    context = {
        'id' : id,
        'users' : ['Mohammad Abdulhafiz', "Eman" , "Hadeel", "Ahmad Jabari" , "Aqeed"]
    }
    return render(request, "create.html",context)


def submituser(request):
    if request.method == "POST": 
        name = request.POST["username"]
        email = request.POST["password"]
        context = {
            'username':name ,
            'password' : email
        }
        request.session["loggedin"] = True
    return render(request, "submituser.html",context)


def logout(request):
    print("hello")
    if 'loggedin' in request.session:
        del request.session['loggedin']
    return redirect('/')

def home(request):
    if 'loggedin' in request.session:
        context = {
    	    "get_all_users": models.get_all_users(request),
        }  
        return render(request, "home.html", context)
    else:
        print("Not logged in") 
        return redirect('/')    


def signup(request):
       return render(request, "signup.html")


def createuser(request):
    errors = User.objects.basic_validator_signup(request.POST)
    if len(errors) > 0:
        print("Errors")   
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/signup')
    else:  #if we do not have any errors  
        print("Passed form")   
        models.create_new_user(request)
        return redirect("/myaccount")


def MyAccount(request):
    return render(request, "myaccount.html")


def createtask(request):
    return render(request, "task.html")


def createusertask(request):
    print("Test1")
    if request.method == "POST": 
        print("Test2")
        models.insertnewtask(request)
        return redirect("/myaccount")
    else:
        return redirect("/")


