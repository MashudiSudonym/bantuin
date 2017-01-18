from django.contrib import admin

from .models import *

class HobiModelAdmin(admin.TabularInline):
	model = Hobi
	extra = 1

class ProfilModelAdmin(admin.ModelAdmin):
	inlines = [HobiModelAdmin]
	list_display = [
		"user",
		"avatar",
		"tgl_lahir", 
		"jenis_kelamin",
		"_hobi",
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

	def _hobi(self, obj):
		return ','.join([o.namahobi for o in obj.hobi.all()])

	_hobi.short_description = "hobi"

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
