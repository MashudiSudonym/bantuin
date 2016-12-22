from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404 

from django.contrib.auth.models import User

def index(request, username):
	
	usrname = get_object_or_404(User, username=username)

	context = {
		"usrdata": usrname,
	}

	return render(request, 'profil/profil.html', context)
