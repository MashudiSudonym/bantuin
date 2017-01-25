from django.forms import ModelForm
from django import forms

from .models import Profil
from django.contrib.auth.models import User

# forms Nama depan dan Nama belakang
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
		fields = [
			"first_name",
			"last_name",
		]

# forms Username
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
		fields = [
			"username",
		]

# forms Email
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
		fields = [
			"email",
		]

# tipe tanggal untuk tgl_lahir
class DateInput(forms.DateInput):
	input_type = 'date'

# forms Profil
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
			"statuspekerja",
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
			'kabupaten': "Kabupaten/Kota",
			'provinsi': "Provinsi",
			'negara': "Negara",

			# kontak
			'phone': "Phone",
			'website': "Website",
			'fb': "Facebook",
			'twitter': "Twitter",
			'googleplus': "Google Plus",

			# lain-lain
			'statuspekerja': "Status Pekerja",
			'bahasa': "Bahasa",
		}

		widgets = {
			# profil dasar
			'self_introduction': forms.Textarea(attrs= {'placeholder': 'Deskripsikan tentang diri anda'}),
			'tgl_lahir': DateInput(),

			# alamat
			'alamat': forms.TextInput(attrs= {'placeholder': 'Alamat Lengkap'}),
			'kode_pos': forms.TextInput(attrs= {'placeholder': 'Kode Pos', 'type': 'number', 'min': '0'}),
			'desa': forms.TextInput(attrs= {'placeholder': 'Desa'}),
			'kecamatan': forms.TextInput(attrs= {'placeholder': 'Kecamatan'}),
			'kabupaten': forms.TextInput(attrs= {'placeholder': 'Kabupaten/Kota'}),
			'provinsi': forms.TextInput(attrs= {'placeholder': 'Provinsi'}),
			'negara': forms.TextInput(attrs= {'placeholder': 'Negara'}),

			#kontak
			'phone': forms.TextInput(attrs= {'placeholder': 'Nomor Telepon', 'type': 'number', 'min': '0'}),
			'website': forms.TextInput(attrs= {'placeholder': 'http://websiteanda.domain'}),
			'fb': forms.TextInput(attrs= {'placeholder': 'http://facebook.com/namaprofil'}),
			'twitter': forms.TextInput(attrs= {'placeholder': 'http://twitter.com/namaprofil'}),
			'googleplus': forms.TextInput(attrs= {'placeholder': 'http://plus.google.com/+namaprofil'}),
		}