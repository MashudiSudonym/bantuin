from django.forms import ModelForm
from django import forms
# from django.contrib.auth.models import User
from .models import Profil

class ProfilForm(ModelForm):
	class Meta:
		model = Profil
		fields = [
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
			"status_pekerja",
			"bahasa",
			"keahlian",
			]
		labels = {
			'avatar': "Avatar",
			'tgl_lahir': "Tanggal Lahir",
			'jenis_kelamin': "Jenis Kelamin",
			'alamat': "Alamat",
			'kode_pos': "Kode Pos",
			'desa': "Desa",
			'kecamatan': "Kecamatan",
			'kabupaten': "Kabupaten",
			'provinsi': "Provinsi",
			'negara': "Negara",
			'phone': "Nomor Telefon / HP",
			'self_introduction': "Tentang Saya",
			'website': "Website",
			'status_pekerja': "Anda bisa memberi Bantuan ? ",
			'bahasa': "Bahasa Utama",
			'keahlian': "Keahlian",
		}
		# error_messages = {
		# 	"alamat": {
		# 		'required': "Alamat wajib diisi"
		# 	}
		# }
		widget = {
			'self_introduction': forms.Textarea(attrs={ 'cols': 50, 'rows': 10 }),
			'keahlian': forms.Textarea(attrs={ 'cols': 50, 'rows': 10 }),
		}