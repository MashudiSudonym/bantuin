from django.shortcuts import render
from django.contrib.auth.models import User

def index(request):

	# gw ga tau caranya biar ga direpeat :( maksudnya biar bisa ambil dari home, biarin gini aja yang penting lebar
	getusrname = User.objects.filter(username=request.user)
		
	context = {
		"usrname_list": getusrname,
	}

	return render(request, 'about/about.html', context)
