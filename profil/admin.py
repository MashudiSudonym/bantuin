from django.contrib import admin

from .models import *

class ProfilModelAdmin(admin.ModelAdmin):
	# list display yang ditampilkan
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
		]

	# link yang bisa di klik adalah user
	list_display_links = ["user"]

	# pilihan filter pencarian, memudahkan pencarian berdasarkan objek
	list_filter = [
		"jenis_kelamin",
		"bahasa",
		]

	# pencarian diatur berdasarkan username
	search_fields = ["user__username"]
	
	class Meta:
		model = Profil

admin.site.register(Profil, ProfilModelAdmin)
