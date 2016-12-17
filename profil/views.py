from django.shortcuts import render

def index(request):
	return render(request, 'profil/profil.html')
