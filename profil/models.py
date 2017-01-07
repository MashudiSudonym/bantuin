from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

def upload_location(instance, filename):
	return "%s/%s" %(instance.user, filename)

class Profil(models.Model):
	user = models.ForeignKey(User, related_name='user')
	avatar = models.ImageField(upload_to=upload_location, blank=True)
	tgl_lahir = models.DateField()
	JENIS_KELAMIN = (
			('Pria', 'Pria'),
			('Wanita', 'Wanita'),
		)
	jenis_kelamin = models.CharField(max_length=12, choices=JENIS_KELAMIN)
	alamat = models.CharField(max_length=200)
	kode_pos = models.CharField(max_length=6)
	desa = models.CharField(max_length=150)
	kecamatan = models.CharField(max_length=150)
	kabupaten = models.CharField(max_length=150)
	provinsi = models.CharField(max_length=150)
	negara = models.CharField(max_length=150)
	phone = models.CharField(max_length=150)
	self_introduction = models.TextField()
	website = models.URLField(blank=True)
	bahasa = models.CharField(max_length=150, blank=True)
	keahlian = models.TextField(blank=True)