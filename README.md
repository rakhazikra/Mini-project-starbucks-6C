# Analisis Nutrisi dan Rekomendasi Menu Makanan Starbucks Berdasarkan Kalori

Program berbasis **Command Line Interface (CLI)** menggunakan bahasa pemrograman Python untuk mengolah, menganalisis kandungan nutrisi, membandingkan produk, mengklasifikasikan tingkat kalori, serta memberikan rekomendasi menu makanan Starbucks sesuai kebutuhan kalori pengguna.

Proyek ini disusun sebagai tugas **Mini Project Praktikum Pemrograman Komputer** pada **Laboratorium Sistem Informasi dan Keputusan (LSIK), Departemen Teknik Industri, Fakultas Teknik, Universitas Andalas (2026)**.

---

## 📋 Daftar Isi
- [Tentang Proyek](#-tentang-proyek)
- [Fitur Utama](#-fitur-utama)
- [Struktur Direktori](#-struktur-direktori)
- [Sumber Dataset](#-sumber-dataset)
- [Alur Logika & Klasifikasi](#-alur-logika--klasifikasi)
- [Prasyarat & Instalasi](#-prasyarat--instalasi)
- [Cara Menjalankan Program](#-cara-menjalankan-program)
- [Batasan Program](#-batasan-program)
- [Status Pengembangan](#-status-pengembangan)
- [Tim Penyusun](#-tim-penyusun)

---

## 🎯 Tentang Proyek
Banyaknya variasi produk makanan Starbucks dengan jenis dan kandungan nutrisi yang beragam sering kali menyulitkan konsumen dalam membandingkan jumlah kalori secara cepat dan praktis. Program ini dirancang menggunakan konsep **Input, Process, dan Output (IPO)** dengan menerapkan struktur percabangan, perulangan, dan fungsi (*function*) untuk membaca dataset CSV menggunakan `csv.DictReader`, melakukan validasi data, hingga menyajikan informasi nutrisi yang terstruktur.

---

## ✨ Fitur Utama
Program menyediakan 6 menu layanan interaktif di terminal:
1. **Pencarian Menu**: Mencari informasi nutrisi lengkap (`calories`, `fat`, `carb`, `fiber`, `protein`) berdasarkan kata kunci nama produk.
2. **Statistik Deskriptif Nutrisi**: Menampilkan jumlah total menu valid beserta nilai **rata-rata**, **maksimum**, dan **minimum** dari setiap atribut nutrisi.
3. **Perbandingan Antarproduk**: Membandingkan kandungan nutrisi antara dua produk pilihan (**Menu A** vs **Menu B**) serta menghitung selisih kalorinya.
4. **Klasifikasi Tingkat Kalori**: Mengelompokkan seluruh menu ke dalam kategori **Rendah**, **Sedang**, dan **Tinggi**, lalu menyimpan hasil klasifikasi ke dalam file CSV baru.
5. **Rekomendasi Menu Berdasarkan Target Kalori**: Menyaring dan merekomendasikan menu makanan yang sesuai dengan batas target kalori pengguna (termasuk opsi tambahan *topping*).
6. **Kalkulator Total Kalori dengan Topping**: Menghitung total akumulasi kalori dari kombinasi menu makanan dan *topping* tambahan beserta kategori kalorinya.

---

## 📁 Struktur Direktori
```text
├── src/                                    # Source code program
│   └── main.py                             # Skrip utama program CLI Python
├── dataset/                                # Dataset proyek
│   └── starbucks.csv                       # Dataset nutrisi makanan Starbucks (Kaggle)
├── output/                                 # Keluaran program
│   └── hasil_klasifikasi_kalori.csv        # File CSV hasil klasifikasi tingkat kalori
├── docs/                                   # Berkas pendukung
│   ├── Laporan_Mini_Project_Kelompok_6C.pdf # Laporan lengkap Mini Project
│   └── Flowchart/                          # Diagram alur (Main & Sub-Flowchart)
└── README.md                               # Dokumentasi utama repository
```
*(Catatan: Sesuaikan nama file skrip dan direktori dengan struktur aktual pada repositori Anda)*

---

## 📊 Sumber Dataset
Dataset yang digunakan dalam proyek ini bersumber dari Kaggle:
* **Judul**: Starbucks Nutrition
* **Penulis**: Utkarsh Singh (2023)
* **Tautan**: [Kaggle - Starbucks Nutrition](https://www.kaggle.com/datasets/utkarshx27/starbucks-nutrition)

---

## ⚙️ Alur Logika & Klasifikasi

### 1. Validasi & Pembersihan Data
Saat memuat file dataset CSV, program memvalidasi setiap baris secara otomatis dengan aturan:
* Memastikan kolom nama menu tidak kosong.
* Mengonversi nilai nutrisi (`calories`, `fat`, `carb`, `fiber`, dan `protein`) ke tipe numerik, menangani karakter strip (`-`), serta menolak data yang bukan angka atau bernilai negatif.

### 2. Ambang Batas Klasifikasi Kalori
Pengelompokan tingkat kalori menu didasarkan pada ambang batas berikut:

| Kategori Kalori | Rentang Nilai Kalori |
| :--- | :--- |
| **Rendah** | `< 220 kkal` |
| **Sedang** | `220 kkal <= Kalori < 360 kkal` |
| **Tinggi** | `>= 360 kkal` |

---

## 🛠️ Prasyarat & Instalasi
* **Python 3.x** (menggunakan modul bawaan Python seperti `csv`, tanpa dependensi pustaka eksternal tambahan).

1. **Clone repositori ini:**
   ```bash
   git clone [https://github.com/](https://github.com/)<username-anda>/<nama-repository>.git
   cd <nama-repository>
   ```
2. **Pastikan file dataset `.csv` tersedia** di dalam direktori proyek sesuai lokasi yang diatur dalam variabel `file_csv`.

---

## 🚀 Cara Menjalankan Program
Jalankan program melalui terminal atau *command prompt*:
```bash
python main.py
```
Pilih angka `1` hingga `6` pada menu utama untuk mengakses fitur yang tersedia, atau masukkan `0` untuk keluar dari program.

---

## ⚠️ Batasan Program
* Program berjalan melalui antarmuka teks (*Command Line Interface* / terminal) tanpa tampilan grafis (GUI).
* Sumber data berasal dari satu file dataset CSV statis.
* Penambahan *topping* hanya berlaku untuk kategori produk makanan sesuai daftar *topping* yang didefinisikan dalam program.
* Hasil analisis dan klasifikasi bertujuan sebagai sumber informasi dan pertimbangan pemilihan menu, bukan sebagai acuan kebutuhan kalori harian personal maupun rekomendasi medis.

---

## 📌 Status Pengembangan
Berdasarkan laporan progres terakhir:
- [x] **Bab I**: Identifikasi masalah, rumusan masalah, tujuan, manfaat, dan batasan program.
- [x] **Bab II (2.1 – 2.5)**: Deskripsi pengguna, sumber dataset, perancangan variabel, rancangan IPO, serta *Main Flowchart* & *Sub-Flowchart*.
- [ ] **Bab II (2.6 – 2.8)**: Finalisasi rancangan fungsi, implementasi kode penuh, dan dokumentasi tampilan output.
- [ ] **Bab III**: Analisis program secara menyeluruh.

---

## 👥 Tim Penyusun

**Kelompok 6C**

| Nama Mahasiswa | NIM |
| :--- | :--- |
| Rakha Zikra Syafdan | 2610931019 |
| Wan Aulia Ramadhani | 2610933008 |
| Rayyan Jeva | 2610937002 |
| Queena Shareefa Yandri | 2610933020 |

* **Dosen Pengampu**: Asmuliardi Muluk, S.T., M.T.
* **Asisten Pembimbing**: Intan Permata Mustika
* **Institusi**: Laboratorium Sistem Informasi dan Keputusan (LSIK), Departemen Teknik Industri, Fakultas Teknik, Universitas Andalas (2026)
