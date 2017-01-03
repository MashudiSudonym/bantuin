from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404 
from django.urls import reverse

from django.contrib.auth.models import User
from .models import Profil

def index(request, username):
	
	getusrname = get_object_or_404(User, username=username)

	getprofil = Profil.objects.filter(user__username=username).first()

	context = {
		"getusrname": getusrname,
		"getprofil": getprofil,
	}

	return render(request, 'profil/profil.html', context)
