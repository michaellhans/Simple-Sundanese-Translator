# Simple Sundanese Translator
Simple Sundanese to Bahasa Indonesia translator using Pattern Matching

## Latar Belakang
Pada suatu hari, ada mahasiswa bernama Riyugan yang baru pindah ke Bandung. Pada awalnya dia mengalami kesulitan untuk bersosialisai dengan lingkungan sekitar karena orang-orang di lingkungannya yang baru hanya berbicara dalam bahasa Sunda. Beruntungnya Riyugan punya teman dari kampung halamannya, yaitu Anda, untuk diminta membuat penerjemah sederhana dari Bahasa Sunda ke Bahasa Indonesia begitu pula sebaliknya untuk memudahkan dirinya bersosialisasi dengan lingkungan barunya di Bandung.

## Getting Started
Instruksi-instruksi berikut ini akan membimbing Anda dalam tahap instalasi aplikasi dan cara menjalankannya.

### Prerequisites
Berikut ini adalah persiapan environment yang dibutuhkan untuk menjalankan aplikasi.
```
- Flask Framework for Integration
- HTML and CSS for Front End
- Regular Expression Library
- Python 3.x.x for Back End
```

### Installing
Berikut ini adalah langkah-langkah dalam penginstallan aplikasi:
1. Install library Flask terlebih dahulu menggunakan command sebagai berikut.
```
pip install Flask
```
2. Lakukan penginstalan Regular Expression dengan command sebagai berikut pada terminal biasa.
```
pip install regex
```
3. Semua prerequisites sudah disiapkan dengan baik.

## How to Run Program
1. Untuk menjalankan program, pastikan command sudah berada dalam directory `./src`, lalu jalankan command sebagai berikut.
```
python WebTranslator.py
```
2. Tunggu kira-kira 5-15 detik. Localhost Flask akan dijalankan. Untuk menampilkan aplikasi web, buka browser kemudian masuk ke laman berikut ini.
```
localhost:5000
```
3. Bila muncul tampilan tanpa adanya error message, maka program berhasil dijalankan.

## Guideline: How To Use
1. Browse vocabulary file untuk Indonesia-Sunda dan Sunda-Indonesia
2. Pastikan bahwa file-file tersebut bertipe text dan berada pada directory ./test. Format umum untuk penulisan vocabulary adalah sebagai berikut.
```
kata = words
sebelum = before
sesudah = after
```
3. Pilih mode terjemahan yang diinginkan. Terdapat dua mode terjemahan yang bisa dilakukan, yaitu:
- Sunda-Indonesia
- Indonesia-Sunda
4. Pilih salah satu dari tiga metode pattern matching yang disediakan, yaitu:
- Algoritma Boyers-Moore
- Algoritma Knutt-Morris-Pratt
- Regular Expression
5. Masukkan text yang ingin diterjemahkan sesuai dengan pilihan terjemahan yang diinginkan
6. Tekan tombol Translate untuk memulai penerjemahan
7. Untuk melakukan penerjemahan kembali, tekan tombol Home untuk kembali ke Menu Awal

## Built With
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - Integrasi Backend dan FrontEnd
* HTML - Front End dari Aplikasi
* CSS - Front End dari Aplikasi
* [Python](https://www.python.org/) - Back End dari Aplikasi

## Beberapa Kasus Uji
```
Sunda - Indonesia
Sunda : nami abdi Riyugan
Indonesia : nama saya Riyugan
```

```
Sunda - Indonesia
Sunda : abdi teh sanes jalma Bandung
Indonesia : saya bukan orang Bandung
```

```
Sunda - Indonesia
Sunda : anjeun sumping ti mana?
Indonesia : kamu tiba dari mana?
```

```
Indonesia - Sunda
Indonesia : mau kamu apa?
Sunda : kersa maneh mah naon?
```

```
Indonesia - Sunda
Indonesia : nama adik kamu siapa?
Sunda : nami rai anjeun teh saha?
```

```
Indonesia - Sunda
Indonesia : saya tidak bisa bahasa Sunda
Sunda : abdi henteu tiasa bahasa Sunda
```

## Video Demo Simple Sundanese Translator
Anda dapat menonton video penggunaan aplikasi ini pada laman berikut ini.
[Simple Sundanese Translator - Demo Aplikasi](https://youtu.be/uu_j1l-vfLo)

## Testing
Untuk menjalankan testing pada web-app penerjemah ini, dapat dijalankan program secara command line interface sebagai berikut.
1. Untuk menjalankan program, pastikan command sudah berada dalam directory `./src`, lalu jalankan command sebagai berikut.
```
python BackEndTest.py
```
2. Masukkan input-input yang bersesuaian sesuai dengan yang diminta oleh program.

## Catatan
Tidak semua kalimat dapat diterjemahkan tepat sasaran mengingat keterbatasan vocabulary yang ada dalam file vocabulary.

## Authors
**13518056 - Michael Hans** - *Designer, Programmer, and Tester*

## Acknowledgments
* Asisten IRK, Ricky Yuliawan