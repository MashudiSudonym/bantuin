from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^(?P<username>[\w.@+-]+)/$', views.index, name='profilhome'),
	url(r'^edit/(?P<username>[\w.@+-]+)/$', views.edit, name='editprofil'),
	url(r'^usernameedit/(?P<username>[\w.@+-]+)/$', views.usernameedit, name='usernameedit'),
	url(r'^emailedit/(?P<username>[\w.@+-]+)/$', views.emailedit, name='emailedit'),
	url(r'^namaedit/(?P<username>[\w.@+-]+)/$', views.namaedit, name='namaedit'),
]
