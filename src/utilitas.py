import os

def simpan_laporan(filepath, statistik, ketuntasan):
    """Menyimpan hasil rekapitulasi analisis ke dalam file teks output."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as file:
        file.write("=== LAPORAN REKAPITULASI NILAI MATEMATIKA ===\n")
        file.write(f"Total Siswa       : {ketuntasan['total_siswa']}\n")
        file.write(f"Siswa Tuntas      : {ketuntasan['tuntas']}\n")
        file.write(f"Siswa Belum Tuntas: {ketuntasan['belum_tuntas']}\n")
        file.write(f"Nilai Rata-rata   : {statistik['rata_rata']}\n")
        file.write(f"Nilai Minimum     : {statistik['min']}\n")
        file.write(f"Nilai Maksimum    : {statistik['max']}\n")
        file.write("=============================================\n")
    print(f"Laporan berhasil disimpan ke {filepath}")