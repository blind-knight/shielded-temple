from django.shortcuts import render

def mainpg(request):
    return render(request, 'indexpage/index.html', {})

def register(request):
    return render(request, 'indexpage/register.html', {})

def signin(request):
    return render(request, 'indexpage/signin.html', {})