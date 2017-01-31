# Bantuin

Bantuin berawal dari projek mata kuliah RPL 2, yang kemudian tetap kami kembangkan menjadi kode sumber untuk jenis aplikasi Market Place berbasis Django.

Kami berharap dengan kode sumber ini dapat membantu teman-teman untuk belajar tentang Django, dan mengembangkan produk yang memiliki konsep yang sama.

Konsep bantuin adalah guna memudahkan masyarakat mencari bantuan terhadap masalah teknis yang sedang dialami semisal saat membutuhkan bantuan untuk servis peralatan elektronik, menjahit baju, sampai menjari jasa tukang pijat.

## Tim Bantuin

* Muhamad Mashudi Ardi Winata 
* Akhi Syabab Ahmad
* Muhammad Alfian Saputra

# Memasang Bantuin

## Lingkungan Development / packages

Kami asumsikan kita sudah mengetahui tentang virtualenv.

### Requirement 

* python-3.5.2
* Django 1.10.3
* django-registration 2.1.2

Selebihnya baca requirements.txt

# Pasang Bantuin ke localhost

catatan : buka dan edit file requirements.txt, hapus paket psycopg2==2.6.2 kemudian simpan dan lakukan installasi seperti panduan ini, jika ingin deploy ke heroku kembalikan lagi psycopg2==2.6.2 setelah install paket agar tidak mengalami masalah saat mencoba deploy ke heroku.

Copy source code

> git clone https://github.com/MashudiSudonym/bantuin.git

Install paket yang dibutuhkan

> pip install -r requirements.txt

Migrasi Database

> python manage.py makemigrations

> python manage.py migrate

Buatlah akun Admin Django

> python manage.py createsuperuser


# Menjalankan Bantuin di localhost

* Buka folder webbantuin/settings
* Rename bak.local.py menjadi local.py
* Jalankan pada local server dengan perintah :

> python manage.py runserver

