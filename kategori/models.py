from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify

class Kategori(models.Model):
	kategori = models.CharField(max_length=254)

	# Slugify
	k_slug = models.SlugField(blank=True)

	# otomasis simpan slugify dengan nama kategori
	def save(self, *args, **kwargs):
		if not self.id:
			self.k_slug = slugify(self.kategori)

		super(Kategori, self).save(*args, **kwargs)

	# for python 3
	def __unicode__(self):
		return self.kategori

	# for python 2
	def __str__(self):
		return self.kategori