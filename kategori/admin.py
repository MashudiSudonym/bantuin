from django.contrib import admin

from .models import *

class KategoriModelAdmin(admin.ModelAdmin):
	list_display = ["kategori", "k_slug"]
	list_display_links = ["kategori"]
	list_filter = ["kategori"]
	search_fields = ["kategori"]

	class Meta:
		model = Kategori

admin.site.register(Kategori, KategoriModelAdmin)
