from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.conf import settings

from django.contrib.auth.models import User
from .models import Profil
from .forms import ProfilForm, EmailForm, FullnameForm, UsernameForm

# index view profil
def index(request, username):
	
	getusrname = get_object_or_404(User, username=username)

	getprofil = Profil.objects.filter(user__username=username).first()

	getavatarusr = Profil.objects.filter(user__username=request.user.username).first()
	
	context = {
		"getusrname": getusrname,
		"getprofil": getprofil,
		"getavatarusr": getavatarusr,
	}

	return render(request, 'profil/profil.html', context)

# view edit profil
@login_required(login_url=settings.LOGIN_URL)
def edit(request, username):
	
	getusrname = get_object_or_404(User, username=username)

	getprofil = Profil.objects.filter(user__username=username).first()

	getavatarusr = Profil.objects.filter(user__username=request.user.username).first()

	if request.method == 'POST':
		form = ProfilForm(request.POST or None, request.FILES or None, instance=getprofil)
		if form.is_valid():
			profil = form.save(commit = False)
			profil.save()
			return HttpResponseRedirect('../../../profil/'+getusrname.username) # << redirect pakai url macam apa ini -_-
	else:
		form = ProfilForm(instance=getprofil)

	context = {
		"getusrname": getusrname,
		"getprofil": getprofil,
		"getavatarusr": getavatarusr,	
		"form": form,
	}

	return render(request, 'profil/edit_profil.html', context)

# view edit username
@login_required(login_url=settings.LOGIN_URL)
def usernameedit(request, username):
	
	getusrname = get_object_or_404(User, username=username)

	getavatarusr = Profil.objects.filter(user__username=request.user.username).first()

	if request.method == 'POST':
		form = UsernameForm(request.POST or None, instance=getusrname)
		if form.is_valid():
			username = form.save(commit = False)
			username.save()
			return HttpResponseRedirect('../../../profil/'+getusrname.username) # << redirect pakai url macam apa ini -_-
	else:
		form = UsernameForm(instance=getusrname)

	context = {
		"getusrname": getusrname,
		"getavatarusr": getavatarusr,
		"form": form,
	}

	return render(request, 'profil/username_edit.html', context)

# view edit email
@login_required(login_url=settings.LOGIN_URL)
def emailedit(request, username):
	
	getusrname = get_object_or_404(User, username=username)

	getavatarusr = Profil.objects.filter(user__username=request.user.username).first()

	if request.method == 'POST':
		form = EmailForm(request.POST or None, instance=getusrname)
		if form.is_valid():
			email = form.save(commit = False)
			email.save()
			return HttpResponseRedirect('../../../profil/'+getusrname.username) # << redirect pakai url macam apa ini -_-
	else:
		form = EmailForm(instance=getusrname)

	context = {
		"getusrname": getusrname,
		"getavatarusr": getavatarusr,
		"form": form,
	}

	return render(request, 'profil/email_edit.html', context)

# view edit nama depan dan belakang
@login_required(login_url=settings.LOGIN_URL)
def namaedit(request, username):
	
	getusrname = get_object_or_404(User, username=username)

	getavatarusr = Profil.objects.filter(user__username=request.user.username).first()

	if request.method == 'POST':
		form = FullnameForm(request.POST or None, instance=getusrname)
		if form.is_valid():
			fullname = form.save(commit = False)
			fullname.save()
			return HttpResponseRedirect('../../../profil/'+getusrname.username) # << redirect pakai url macam apa ini -_-
	else:
		form = FullnameForm(instance=getusrname)

	context = {
		"getusrname": getusrname,
		"getavatarusr": getavatarusr,
		"form": form,
	}

	return render(request, 'profil/fullname_edit.html', context)