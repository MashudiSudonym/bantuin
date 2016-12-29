from django.shortcuts import render
from django.contrib.auth.views import login as contrib_login, logout as contrib_logout
from django.shortcuts import redirect
from django.conf import settings

from home import *

def index(request):
	if request.user.is_authenticated():
		return render(request, 'dashboard/dashboard.html')
	else :
		return render(request, 'home/home.html')
