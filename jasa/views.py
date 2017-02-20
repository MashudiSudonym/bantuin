from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.conf import settings

from django.contrib.auth.models import User
from .models import Jasa
from kategori.models import Kategori
from profil.models import Profil

def index(request):
	
	getusrname = User.objects.filter(username=request.user)

	getkategori = Kategori.objects.all().order_by("kategori")

	getprofil = Profil.objects.filter(user__username=request.user)
		
	context = {
		"usrname_list": getusrname,
		"kategori_list": getkategori,
		"profil_list": getprofil,
	}

	return render(request, 'jasa/jasa.html', context)
