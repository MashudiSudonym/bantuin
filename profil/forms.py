from django.forms import ModelForm
from django import forms

from .models import Profil
from django.contrib.auth.models import User

class FullnameForm(ModelForm):
	first_name = forms.CharField(
		required = True,
		label = 'Nama Depan',
		widget = forms.TextInput(
			attrs = {'placeholder': 'Nama Depan'}
			)
		)

	last_name = forms.CharField(
		required = True,
		label = 'Nama Belakang',
		widget = forms.TextInput(
			attrs = {'placeholder': 'Nama Belakang'}
			)
		)

	class Meta:
		model = User
		fields = []

class UsernameForm(ModelForm):
	username = forms.CharField(
		required = True,
		label = 'Username',
		max_length = 50,
		widget = forms.TextInput(
			attrs = {'placeholder': 'Your Username'}
			)
		)

	class Meta:
		model = User
		fields = []

class EmailForm(ModelForm):
	email = forms.EmailField(
		required = True,
		label = 'Email',
		widget = forms.TextInput(
			attrs = {'placeholder': 'Email'}
			)
		)

	class Meta:
		model = User
		fields = []

class DateInput(forms.DateInput):
	input_type = 'date'

class ProfilForm(ModelForm):
	class Meta:
		model = Profil

		fields = [
			# profil dasar
			"user",
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
			'phone': "Phone",
			'website': "Website",
			'fb': "Facebook",
			'twitter': "Twitter",
			'googleplus': "Google Plus",

			# lain-lain
			'status_pekerja': "Status Pekerja",
			'bahasa': "Bahasa",
		}

		widgets = {
			'tgl_lahir': DateInput(),
		}