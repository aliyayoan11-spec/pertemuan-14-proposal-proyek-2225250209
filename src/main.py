from data_io import baca_data
from analisis import hitung_statistik, hitung_ketuntasan
from utilitas import simpan_laporan

def main():
    path_input = "data/nilai_contoh.txt"
    path_output = "output/laporan_hasil.txt"
    kkm = 60

    print("Memproses data nilai...")
    data_siswa = baca_data(path_input)

    if not data_siswa:
        print("Tidak ada data valid yang dapat diproses.")
        return

    statistik = hitung_statistik(data_siswa)
    ketuntasan = hitung_ketuntasan(data_siswa, kkm)

    print("\n--- HASIL ANALISIS NILAI ---")
    print(f"Jumlah Siswa : {ketuntasan['total_siswa']}")
    print(f"Rata-rata    : {statistik['rata_rata']}")
    print(f"Nilai Min    : {statistik['min']}")
    print(f"Nilai Max    : {statistik['max']}")
    print(f"Tuntas (>=60): {ketuntasan['tuntas']}")
    print(f"Belum Tuntas : {ketuntasan['belum_tuntas']}")

    simpan_laporan(path_output, statistik, ketuntasan)

if __name__ == "__main__":
    main()