from django.contrib import admin

from .models import *

class JasaModelAdmin(admin.ModelAdmin):
	# list display yang ditampilkan
	list_display = [
		"nama_jasa",
		"user",
		"kategories",
		"alamat",
		"kode_pos",
		"desa",
		"kecamatan",
		"kabupaten",
		"provinsi",
		"negara",
		"phone",
		"website",
		"fb",
		"twitter",
		"googleplus",
		"terima_panggilan",
		]

	# pilihan filter pencarian, memudahkan pencarian berdasarkan objek
	list_filter = [
		"nama_jasa",
		"user",
		"terima_panggilan",
		]

	# pencarian diatur berdasarkan nama_jasa
	search_fields = [
		"nama_jasa",
		"user",
		]

	class Meta:
		model = Jasa

admin.site.register(Jasa, JasaModelAdmin)