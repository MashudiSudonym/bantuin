from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# memberi nama folder atau lokasi unggah avatar berdasarkan username yang menunggah
def upload_location(instance, filename):
	return "%s/%s" %(instance.user, filename)

# table database Profil untuk Profil App
class Profil(models.Model):
	# profil dasar
	user = models.ForeignKey(User, related_name='user')
	avatar = models.ImageField(upload_to=upload_location, blank=True)
	tgl_lahir = models.DateField()
	JENIS_KELAMIN = (
			('Pria', 'Pria'),
			('Wanita', 'Wanita'),
		)
	jenis_kelamin = models.CharField(max_length=12, choices=JENIS_KELAMIN)
	self_introduction = models.TextField()

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
	STATUS_PEKERJA = (
			('Bukan Pekerja', 'Bukan Pekerja'),
			('Pekerja', 'Pekerja'),
		)
	statuspekerja = models.CharField(max_length=24, choices=STATUS_PEKERJA, default='Bukan Pekerja', blank=True)
	BAHASA = (
			('Bahasa Indonesia', 'Bahasa Indonesia'),
			('English', 'English'),
			('Other', 'Other'),
		)
	bahasa = models.CharField(max_length=150, choices=BAHASA)
