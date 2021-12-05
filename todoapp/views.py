from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from todoapp.models import TodoModel

# Create your views here.
def landingPageView(request):
    return render(request, 'todoapp/landingpage.html')

def registerUser(request):
    username = request.POST['username']
    password = request.POST['password']
    repassword = request.POST['repassword']

    if password != repassword:
        messages.error(request, 'Passwords do not match')
        return redirect(request.META['HTTP_REFERER'])
    # if user already exists
    if User.objects.filter(username=username).exists():
        messages.error(request, 'User already exists')
        return redirect(request.META['HTTP_REFERER'])
    
    User.objects.create_user(username=username, password=password)
    messages.success(request, 'User created successfully')
    return redirect(request.META['HTTP_REFERER'])
    
def loginUser(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('todoPage')
    else:
        messages.error(request, 'Invalid Credentials')
        return redirect(request.META['HTTP_REFERER'])

def logoutUser(request):
    logout(request)
    return redirect('landingPage')

def todoView(request):
    user = request.user
    todos = TodoModel.objects.filter(user=user)
    return render(request, 'todoapp/todopage.html', {'todos': todos})

def addTodo(request):
    todo =request.POST['todo']
    user = request.user
    TodoModel(title = todo, user = user).save()
    return redirect('todoPage')

def deleteTodo(request, pk):
    todo = TodoModel.objects.get(id=pk)
    todo.delete()
    return redirect(request.META['HTTP_REFERER'])