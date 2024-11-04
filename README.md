# Pinterest Data Crawler
## Deskripsi Proyek
Proyek ini adalah skrip Python yang digunakan untuk mengambil data pin dari Pinterest berdasarkan kata kunci pencarian yang dimasukkan pengguna. Data yang diambil berupa tautan ke pin Pinterest, yang kemudian disimpan ke dalam file CSV.

## Prasyarat
Sebelum menjalankan proyek ini, pastikan telah menginstal perangkat lunak dan requirements berikut:
- **Python 3.x**
- **Paket Python**:
  - `requests`

## Instalasi

1. **Clone repository ini** (jika proyek ini di-host di repositori git):
   ```bash
   git clone https://github.com/DhaifinaAP/Tugas10-Crawling.git
   cd project-name
   ```

2. **Instal dependensi Python**:
   Gunakan `venv` untuk mengelola environment Python. Lalu, jalankan:
   ```bash
   pip install -r requirements.txt
   ```

3. **Membuat file `apikey.txt`**:
   - Buat file `apikey.txt` di direktori proyek.
   - Salin `apikey-example.txt` sebagai contoh, yang berisi format berikut:
     ```
     1234567890abcdef1234567890abcdef
     ```
   - Gantilah isi `apikey.txt` dengan API Key Anda sendiri yang valid dari [RapidAPI](https://rapidapi.com).

## Cara Menjalankan Proyek

1. **Jalankan skrip Python**:
   Pastikan Anda berada di direktori proyek, lalu jalankan skrip dengan perintah berikut:
   ```bash
   python crawling.py
   ```

2. **Input Pengguna**:
   Saat diminta, masukkan kata kunci pencarian dan jumlah data yang diinginkan:
   ```
   Masukkan kata kunci pencarian: [contoh: interior ideas]
   Masukkan jumlah data yang diinginkan: [contoh: 30]
   ```

3. **Output**:
   - Data yang diambil akan disimpan dalam file `url_printerest_data.csv` dengan kolom `Nomor` dan `Link`.

## Struktur File
- **crawling.py**: Skrip utama proyek.
- **apikey.txt**: File teks yang berisi API Key Anda (ikuti format dari `apikey-example.txt`).
- **apikey-example.txt**: Contoh format untuk `apikey.txt`.
- **url_printerest_data.csv**: File hasil pengumpulan data dari Pinterest.
