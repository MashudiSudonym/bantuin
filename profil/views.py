from django.shortcuts import render

def index(request):
	if request.user.is_authenticated() :
		context = {
			"username": request.user.username,
			"email": request.user.email,
			"firstname": request.user.first_name,
			"lastname": request.user.last_name,
		}
	else :
		context = {}
	return render(request, 'profil/profil.html', context)
