from __future__ import unicode_literals

from django.db import models
from kategori.models import Kategori
from django.contrib.auth.models import User

# model untuk jasa memiliki kesamaan dengan model untuk profil,
# contohnya alamat, namun alamat pada profil tidak sama dengan alamat jasa,
# kemungkinan alamat jasa berbeda dengan alamat pengguna (profil)

class Jasa(models.Model):
	# data dasar
	nama_jasa = models.CharField(max_length=150)
	user = models.ForeignKey(User)
	kategori = models.ManyToManyField(Kategori)

	# alamat
	alamat = models.CharField(max_length=200)
	kode_pos = models.CharField(max_length=6)
	desa = models.CharField(max_length=150)
	kecamatan = models.CharField(max_length=150)
	kabupaten = models.CharField(max_length=150)
	provinsi = models.CharField(max_length=150)
	negara = models.CharField(max_length=150)

	# Kontak
	phone = models.CharField(max_length=150)
	website = models.URLField(blank=True)
	fb = models.URLField(blank=True)
	twitter = models.URLField(blank=True)
	googleplus = models.URLField(blank=True)

	# lain-lain
	TERIMA_PANGGILAN = (
			('tidak', 'Tidak'),
			('ya', 'Ya'),
		)
	terima_panggilan = models.CharField(max_length=15, choices=TERIMA_PANGGILAN, default="tidak", blank=True)


	# biar bisa muncul kolom isi untuk kategori di admin.py
	def kategories(self):
		return ",".join([str(k) for k in self.kategori.all()])

	# for python 3
	def __unicode__(self):
		return self.nama_jasa

	# for python 2
	def __str__(self):
		return self.nama_jasa