from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^(?P<username>[\w.@+-]+)/$', views.index, name='profilhome'),
]
