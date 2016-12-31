from django.shortcuts import render
from django.contrib.auth.models import User

def index(request):
	getusrname = User.objects.filter(username=request.user)
		
	context = {
		"usrname_list": getusrname,
	}
	
	return render(request, 'about/about.html', context)
