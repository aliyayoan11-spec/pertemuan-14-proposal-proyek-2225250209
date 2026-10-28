# Dokumen Pengujian (Test Case) - Proyek Analisis Nilai

Dokumen ini berisi daftar skenario pengujian untuk memastikan modul I/O, validasi, dan analisis statistik berjalan sesuai harapan tanpa error yang tidak terduga.

## Daftar Test Case

| ID Test | Kategori | Kondisi / Input | Expected Result (Harapan) | Status |
| :--- | :--- | :--- | :--- | :--- |
| **TC01** | Normal | Data nilai: `[85, 78, 92, 55, 60]` | Program menghitung rata-rata, min, max, dan jumlah tuntas dengan akurat[cite: 1]. | Belum Diuji |
| **TC02** | Batas (Boundary) | Input nilai tepat `0` | Diterima sebagai nilai valid oleh sistem validasi[cite: 1]. | Belum Diuji |
| **TC03** | Batas (Boundary) | Input nilai tepat `100` | Diterima sebagai nilai valid oleh sistem validasi[cite: 1]. | Belum Diuji |
| **TC04** | Invalid | Input nilai negatif (`-5`) atau lebih dari 100 (`105`) | Ditolak oleh sistem dengan pesan peringatan/validasi yang jelas[cite: 1]. | Belum Diuji |
| **TC05** | Invalid | File sumber data (`nilai_contoh.txt`) dihapus/tidak ada | Program menangkap error `FileNotFoundError` dan menampilkan pesan kesalahan ramah[cite: 1]. | Belum Diuji |
| **TC06** | Normal | Semua siswa mendapat nilai di atas KKM ($\ge 60$) | Jumlah siswa tuntas sama dengan total keseluruhan data siswa[cite: 1]. | Belum Diuji |