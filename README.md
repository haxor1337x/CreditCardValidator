Validasi Credit Card Menggunakan Stripe
=======================================

Program ini adalah sebuah script Python yang digunakan untuk memvalidasi credit card menggunakan Stripe. Anda dapat menguji sejumlah credit card untuk mengetahui apakah credit card tersebut valid atau tidak. Script ini akan membaca daftar credit card yang akan divalidasi dari file `cclist.txt` dan akan menyimpan credit card yang valid ke dalam file `ccvalid.txt`. Selain itu, proses validasi setiap credit card juga akan ditampilkan di konsol.

Persyaratan
-----------

*   Python 3.6 atau lebih baru
*   Paket Stripe dan Termcolor

Instalasi
---------

1.  Clone repository ini ke dalam direktori lokal Anda:
    
    bashCopy code
    
    `git clone https://github.com/username/repo.git`
    
2.  Instal paket Stripe dan Termcolor:
    
    Copy code
    
    `pip install stripe termcolor`
    

Penggunaan
----------

1.  Masuk ke direktori tempat Anda meng-clone repository ini.
    
2.  Buat file `key.txt` dan isi dengan Stripe secret key Anda.
    
3.  Buat file `cclist.txt` dan isi dengan daftar credit card yang akan divalidasi. Setiap baris dalam file harus berisi nomor kartu kredit, bulan kedaluwarsa, tahun kedaluwarsa, dan kode CVC, dipisahkan oleh tanda `|`.
    
4.  Jalankan script dengan perintah berikut:
    
    Copy code
    
    `python check.py`
    
5.  Script akan membaca setiap baris dari `cclist.txt` dan memvalidasi credit card sesuai dengan format yang ditentukan. Setiap credit card yang valid akan disimpan ke dalam file `ccvalid.txt` dan akan ditampilkan di konsol dengan warna hijau. Setiap credit card yang tidak valid akan ditampilkan di konsol dengan warna merah.
    
6.  Setelah selesai, Anda dapat membuka file `ccvalid.txt` untuk melihat daftar credit card yang valid.
    

Catatan
-------

*   Pastikan untuk tidak membagikan secret key Stripe Anda kepada siapa pun.
*   Pastikan format credit card yang dimasukkan ke dalam file `cclist.txt` benar. Jika tidak, program akan menghasilkan output yang tidak akurat.
*   Pastikan untuk menggunakan file `key.txt` dan `cclist.txt` yang benar saat menjalankan program. Jika tidak, program akan gagal bekerja dengan benar.
