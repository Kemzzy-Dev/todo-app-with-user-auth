from django.shortcuts import render, redirect
from .forms import TodoForm
from .models import Todo

from .forms import CreateUserForm, LoginUserForm
from django.contrib.auth import authenticate, login, logout
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib import messages


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
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            
            if user != None:
                login(request, user)
                return redirect('view')
            else:
                messages.error(request, 'Username or password is incorrect!')

    return render(request, 'app/loginPage.html', {'form':form})

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
            else:
                messages.error(request, 'Registration was unsuccessful!')
        
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