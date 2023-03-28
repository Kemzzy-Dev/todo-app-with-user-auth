from django.urls import path
from . import views
from django.urls import include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.todoView, name='view'),
    path('add/', views.addTask, name='add'),
    path('delete/<str:pk>', views.deleteTask, name='delete'),
    path('update/<str:pk>', views.updateTask, name='update'),
    
    # authentication
    path('login/', views.SignInUser, name='login'),
    path('logout/', views.SignOutUser, name='signout'),
    path('register/', views.registerUser, name='register'),

    #forgotten password
    path("password_reset", views.password_reset, name="password_reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="app/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'), name='password_reset_complete'),     
    
]