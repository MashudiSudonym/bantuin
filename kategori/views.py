from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.conf import settings

from django.contrib.auth.models import User
from .models import Kategori
from jasa.models import Jasa
from profil.models import Profil

def index(request):
	getusrname = User.objects.filter(username=request.user)

	getkategori = Kategori.objects.all().order_by("kategori")

	getprofil = Profil.objects.filter(user__username=request.user)

	# hitung jumlah jasa dari setiap bantuan untuk menampilkannya di view
	count_acara = Jasa.objects.filter(kategori__kategori='acara').count()

	count_bangunan = Jasa.objects.filter(kategori__kategori='bangunan').count()

	count_kesehatan = Jasa.objects.filter(kategori__kategori='kesehatan').count()

	count_makanan = Jasa.objects.filter(kategori__kategori='makanan').count()

	count_pakaian = Jasa.objects.filter(kategori__kategori='pakaian').count()

	count_pendidikan = Jasa.objects.filter(kategori__kategori='pendidikan').count()

	count_reparasi = Jasa.objects.filter(kategori__kategori='reparasi').count()

	count_rumahtangga = Jasa.objects.filter(kategori__kategori='rumah-tangga').count()

	count_transportasi = Jasa.objects.filter(kategori__kategori='transportasi').count()
		
	context = {
		"usrname_list": getusrname,
		"kategori_list": getkategori,
		"profil_list": getprofil,
		"count_acara": count_acara,
		"count_bangunan": count_bangunan,
		"count_kesehatan": count_kesehatan,
		"count_makanan": count_makanan,
		"count_pakaian": count_pakaian,
		"count_pendidikan": count_pendidikan,
		"count_reparasi": count_reparasi,
		"count_rumahtangga": count_rumahtangga,
		"count_transportasi": count_transportasi,
	}

	return render(request, 'kategori/kategori.html', context)

def daftar(request, k_slug):
	judulhalaman = get_object_or_404(Kategori, k_slug=k_slug)

	getusrname = User.objects.filter(username=request.user)

	getkategori = Kategori.objects.all().order_by("kategori")

	getprofil = Profil.objects.filter(user__username=request.user)

	getjasa = Jasa.objects.filter(kategori__kategori=k_slug)
		
	context = {
		"judulhalaman": judulhalaman,
		"usrname_list": getusrname,
		"kategori_list": getkategori,
		"profil_list": getprofil,
		"jasa_list": getjasa,
	}

	return render(request, 'kategori/daftar-jasa.html', context)