from django.shortcuts import render
from django.contrib.auth.views import login as contrib_login, logout as contrib_logout
from django.shortcuts import redirect
from django.conf import settings

from dashboard import *

def index(request):
	if request.user.is_authenticated():
		return render(request, 'dashboard/dashboard.html')
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