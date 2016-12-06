# Bantuin
Bantuin adalah projek mata kuliah RPL 2.

Konsep bantuin adalah guna memudahkan masyarakat mencari bantuan terhadap masalah teknis yang sedang dialami semisal saat membutuhkan bantuan untuk servis peralatan elektronik, menjahit baju, sampai menjari jasa tukang pijat.

## Tim Bantuin

* Muhamad Mashudi Ardi Winata 
* Akhi Syabab Ahmad
* Muhammad Alfian Saputra

# Memasang Bantuin

## Lingkungan Development / packages

### Requirement 

* Django 1.10.3
* django-registration 2.1.2
* django-crispy-forms 1.6.1
* gunicorn 19.6.0
* whitenoise 3.2.2
# django-jet 1.0.4

# Pasang Bantuin ke localhost

Copy source code

> git clone https://github.com/MashudiSudonym/bantuin.git

Install paket yang dibutuhkan

> pip install -r requirements.txt

catatan : buka dan edit file requirements.txt, hapus paket psycopg2==2.6.2 kemudian simpan dan lakukan installasi seperti panduan di atas.

Menjalankan Bantuin di localhost

* buat file bernama local.py di folder webbantuin/settings dan copas isinya dari file production.py yang ada di folder yg sama
* setelah copas ke local.py, pada file local.py cari DEBUG = False dan ganti dengan DEBUG = True
* tetap pada file local.py, ganti ALLOWED_HOSTS = ['*'] dengan ALLOWED_HOSTS = []
* simpan dan jalankan pada local server dengan perintah :

> python manage.py runserver

