from django.contrib import admin

from .models import *

class ProfilModelAdmin(admin.ModelAdmin):
	list_display = [
		"user",
		"avatar",
		"tgl_lahir", 
		"jenis_kelamin",
		"alamat",
		"kode_pos",
		"desa",
		"kecamatan",
		"kabupaten",
		"provinsi",
		"negara",
		"phone",
		"self_introduction",
		"website",
		"fb",
		"twitter",
		"googleplus",
		"status_pekerja",
		"bahasa",
		"keahlian",
		]
	list_display_links = ["user"]
	list_filter = [
		"tgl_lahir", 
		"jenis_kelamin",
		"alamat",
		"kode_pos",
		"desa",
		"kecamatan",
		"kabupaten",
		"provinsi",
		"negara",
		]
	search_fields = ["user__username"]
	class Meta:
		model = Profil

admin.site.register(Profil, ProfilModelAdmin)
