from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='kategori'),
    url(r'^(?P<kategori>[\w.@+-]+)/$', views.daftar, name='daftar'),
]