from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404 
from django.urls import reverse

from django.contrib.auth.models import User

def index(request, username):
	
	usrdata = get_object_or_404(User, username=username)

	context = {
		"usrdata": usrdata,
	}

	return render(request, 'profil/profil.html', context)
