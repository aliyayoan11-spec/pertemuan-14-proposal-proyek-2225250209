# Proposal Proyek Akhir: Program Rekap dan Analisis Nilai Matematika Kelas

## 1. Judul Proyek
Program Rekap dan Analisis Nilai Matematika Kelas

## 2. Latar Belakang
Guru sering kali membutuhkan waktu yang tidak sedikit untuk menghitung rata-rata nilai kelas, mencari nilai tertinggi dan terendah, serta menentukan jumlah siswa yang tuntas maupun belum tuntas berdasarkan Kriteria Ketuntasan Minimal (KKM). Oleh karena itu, diperlukan program berbasis Python yang otomatis membaca data, memvalidasi nilai, melakukan analisis statistik, dan menghasilkan laporan rekapitulasi secara efisien.

## 3. Pengguna dan Tujuan
- **Pengguna:** Guru mata pelajaran atau wali kelas.
- **Tujuan:** Mempermudah rekapitulasi nilai siswa secara akurat, cepat, dan terstruktur menggunakan pemrograman modular.

## 4. Ruang Lingkup
- **Fitur Wajib:**
  1. Membaca data nilai dari file eksternal (`data/nilai_contoh.txt`).
  2. Memvalidasi rentang nilai (hanya menerima angka 0–100).
  3. Menghitung statistik dasar (rata-rata, nilai minimum, nilai maksimum).
  4. Menghitung jumlah siswa tuntas dan belum tuntas berdasarkan KKM (KKM = 60).
  5. Menyimpan laporan hasil analisis ke dalam file teks di folder `output/`.
- **Batasan:** Program beroperasi secara *command-line interface* (CLI) menggunakan file teks lokal.

## 5. Kebutuhan Fungsional & Non-Fungsional
- **Fungsional:** Sistem dapat memproses file teks, menolak data di luar rentang 0–100, menghitung statistik, dan mengekspor laporan.
- **Non-Fungsional:** Kode terstruktur secara modular, mudah dibaca, dan dilengkapi dokumentasi pengoperasian.

## 6. IPO (Input, Process, Output)
- **Input:** File teks berisi `Nama,Nilai` per baris.
- **Process:** Validasi data, parsing string ke dictionary/list, perhitungan statistik matematika, dan seleksi ketuntasan KKM.
- **Output:** Tampilan ringkasan di terminal serta file laporan rekapitulasi teks.

## 7. Pseudocode / Alur Utama
```text
data_mentah = baca_file("data/nilai_contoh.txt")
data_valid = validasi_data(data_mentah)
if data_valid kosong:
    tampilkan pesan error
else:
    statistik = hitung_statistik(data_valid)
    ketuntasan = cek_ketuntasan(data_valid, kkm=60)
    tampilkan_hasil(statistik, ketuntasan)
    simpan_laporan(statistik, ketuntasan)