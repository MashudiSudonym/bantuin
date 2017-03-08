from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='kategori'),
    url(r'^(?P<k_slug>[\w.@+-]+)/$', views.daftar, name='daftar'),
]