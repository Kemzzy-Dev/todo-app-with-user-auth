from django.shortcuts import render, redirect
from .forms import TodoForm
from .models import Todo, User

from .forms import CreateUserForm, LoginUserForm
from django.contrib.auth import authenticate, login, logout
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib import messages


#forgot password import
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
import socket


# User authentication 

@login_required(login_url='login')
def SignOutUser(request):
    logout(request)
    return redirect('login')

def SignInUser(request):
    form = LoginUserForm()

    if request.user.is_authenticated:
        return redirect ('view')
    else:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(email=email, password=password)
            
            if user != None:
                login(request, user)
                return redirect('view')
            else:
                messages.error(request, 'Email or Password is Incorrect!')

    return render(request, 'app/login.html', {'form':form})

def registerUser(request):
    form = CreateUserForm()

    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            form = CreateUserForm(request.POST)

            if form.is_valid():
                form.save()
                messages.success(request, 'Account created successfully!')
                return redirect('login')
        
    return render(request, 'app/registerPage.html', {'form':form})


# Adding, editing and deleting tasks from the todos
# Redirects here to display the list of todos
@login_required(login_url='login')
def todoView(request):
    form = TodoForm()
    todo = Todo.objects.filter(user=request.user)
    context = {
        'form':form,
        'todos':todo
    }
    return render(request, 'app/index.html', context)

@login_required(login_url='login')
def addTask(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('view')
    else:
        form = TodoForm()

    return redirect('view')

login_required(login_url='view')
def deleteTask(request, pk):
    try:
        todo = Todo.objects.get(id=pk)
    except:
        return render(request, 'app/404.html')#Create a template for this
    
    todo.delete()
    return redirect('view')

login_required(login_url='view')
def updateTask(request, pk):
    try:
        todo = Todo.objects.get(id=pk)
    except:
        return render(request, 'app/404.html')#create a template for this

    if request.method == 'POST':
        #get the form from the template
        update_task = request.POST.get('updatetask')
        todo.task = update_task
        todo.save()

        return redirect('view')
    
    return render(request, 'app/update.html', {'todo':todo})

def password_reset(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "app/password_reset_subject.txt"
                    c = {
                    "email":user.email,
                    'domain':'127.0.0.1:8000',
                    'site_name': 'Website',
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    "user": user,
                    'token': default_token_generator.make_token(user),
                    'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect ("/password_reset/done/")
        else:
            return HttpResponse('Invalid Email')
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="app/password_reset_form.html", context={"password_reset_form":password_reset_form})