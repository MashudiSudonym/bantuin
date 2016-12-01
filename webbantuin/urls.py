"""webbantuin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^', include('home.urls')),
    url(r'^about/', include('about.urls')),
    # url(r'^login/', include('login.login_urls')),
    # url(r'^register/', include('login.register_urls')),
    url(r'^forgot/', include('login.forgot_urls')),
    url(r'^404/', include('home.urls')),
    url(r'^500/', include('home.urls')),
    url(r'^accounts/', include('registration.backends.hmac.urls')), 
#    url(r'^accounts/login/', include('home.urls')), 
]

#handler404 = include('home.urls')
#handler500 = include('home.urls')
