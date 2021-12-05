
from django.urls import path
from .views import *
urlpatterns = [
    path('',landingPageView, name='landingPage'),
    path('register/',registerUser, name='register'),
    path('login/',loginUser, name='loginuser'),
    path('todo/',todoView, name='todoPage'),
    path('logoutuser/',logoutUser, name='logoutuser'),
    path('addtodo/',addTodo, name='addTodo'),
    path('delete/<int:pk>/',deleteTodo, name='deleteTodo'),
]