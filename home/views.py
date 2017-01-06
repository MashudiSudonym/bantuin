from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.conf import settings

from django.contrib.auth.models import User
from profil.models import Profil

def index(request):
	if request.user.is_authenticated():

		getusrname = User.objects.filter(username=request.user)
		getprofil = Profil.objects.filter(user__username=request.user)
		
		context = {
			"usrname_list": getusrname,
			"profil_list": getprofil,
		}

		return render(request, 'dashboard/dashboard.html', context)
	else :
		return render(request, 'home/home.html')

def handler404(request):
    response = render(request, 'errors/404.html')
    response.status_code = 404
    return response

def handler500(request):
    response = render(request, 'errors/500.html')
    response.status_code = 500
    return response