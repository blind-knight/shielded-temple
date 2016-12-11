from django.shortcuts import render
from django.contrib.auth.models import User


def mainpg(request):
    return render(request, 'indexpage/index.html', {})

def register(request):
    return render(request, 'indexpage/register.html', {})

def signin(request):
	if request.user.is_authenticated():
		loggedUser = User.objects.filter(email=request.user.email)[0]
		print loggedUser.email
		if loggedUser.email and loggedUser.email is not None:
			print "user exists"
			return render(request, 'dashboard/dashboard.html', {})
		else:
			print "user doesnt exists"
			return render(request, 'indexpage/register.html', {'email':request.user.email})
	else:
		return render(request, 'indexpage/signin.html', {})