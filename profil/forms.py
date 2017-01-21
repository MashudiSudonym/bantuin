from django.forms import ModelForm
from django import forms

from .models import Profil
from django.contrib.auth.models import User

class UsernameForm(ModelForm):
	class Meta:
		model = User

		fields = [
			"username",
			"first_name",
			"last_name",
			"email",
		]

		labels = {
			'username': "Username",
			'first_name': "Nama Depan",
			'last_name': "Nama Belakang",
			'email': "Email",
		}

class ProfilForm(ModelForm):
	class Meta:
		model = Profil

		fields = [
			# profil dasar
			"avatar",
			"tgl_lahir",
			"jenis_kelamin",
			"self_introduction",

			# alamat
			"alamat",
			"kode_pos",
			"desa",
			"kecamatan",
			"kabupaten",
			"provinsi",
			"negara",

			# kontak
			"phone",
			"website",
			"fb",
			"twitter",
			"googleplus",

			# lain-lain
			"status_pekerja",
			"bahasa",
			"keahlian",
			]

		labels = {
			# profil dasar
			'avatar': "Avatar",
			'tgl_lahir': "Tanggal Lahir",
			'jenis_kelamin': "Jenis Kelamin",
			'self_introduction': "Tentang Saya",

			# alamat
			'alamat': "Alamat",
			'kode_pos': "Kode Pos",
			'desa': "Desa",
			'kecamatan': "Kecamatan",
			'kabupaten': "Kabupaten",
			'provinsi': "Provinsi",
			'negara': "Negara",

			# kontak
			'phone': "Nomor Telefon / HP",
			'website': "Website",
			'fb': "Facebook",
			'twitter': "Twitter",
			'googleplus': "G+",

			# lain-lain
			'status_pekerja': "Anda bisa memberi Bantuan ? ",
			'bahasa': "Bahasa Utama",
			'keahlian': "Keahlian",
		}

		widget = {
			'self_introduction': forms.Textarea(attrs={ 'cols': 50, 'rows': 10 }),
			'keahlian': forms.Textarea(attrs={ 'cols': 50, 'rows': 10 }),
			'tgl_lahir': forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'}),
		}