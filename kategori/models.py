from __future__ import unicode_literals

from django.db import models

class Kategori(models.Model):
	kategori = models.CharField(max_length=254)

	# for python 3
	def __unicode__(self):
		return self.kategori

	# for python 2
	def __str__(self):
		return self.kategori