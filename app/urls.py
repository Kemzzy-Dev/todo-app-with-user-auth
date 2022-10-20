from django.urls import path
from . import views

urlpatterns = [
    path('', views.todoView, name='view'),
    path('add/', views.addTask, name='add'),
    path('delete/<str:pk>', views.deleteTask, name='delete'),
    path('update/<str:pk>', views.updateTask, name='update'),
    # authentication
    path('login/', views.SignInUser, name='login'),
    path('logout/', views.SignOutUser, name='signout'),
    path('register/', views.registerUser, name='register')

]