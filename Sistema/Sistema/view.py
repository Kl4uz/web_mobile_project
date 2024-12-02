from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views import View


def authuser(request):
    if request.method == 'GET':
        return render(request, 'auth.html')
    else:
        log = request.POST.get('login')
        cadastro = request.POST.get('cadastro')
        
        if log:
            return redirect('login')
        if cadastro:
            return redirect('cadastro')
    
    return render(request, 'auth.html')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    
    else:
        name = request.POST.get('username')
        senha = request.POST.get('password')

        user = authenticate(username = name, password = senha)

        # login(user)

        if user is not None:
            if user.is_active:
                return redirect('events-home')
                
        else:
            return render(request, 'login.html', {'erro':'Credenciais inválidas'})
    
    return render(request, 'login.html')
    

def cadastro(request):

    if request.method == 'GET':
        return render(request, 'cadastro.html')
        
    else:
        username = request.POST.get('name')
        password = request.POST.get('password')
        email = request.POST.get('email')

        user = User.objects.create_user(username, email, password)
        user.save()

        return redirect('login')




        
    
    

    