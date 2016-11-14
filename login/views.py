from django.shortcuts import render

def index(request):
	return render(request, 'login/login.html')

def register(request):
	return render(request, 'login/register.html')

def forgot(request):
	return render(request, 'login/forgot.html')

