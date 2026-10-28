def baca_data(filepath):
    """Membaca file teks dan mengembalikan list of dictionary data siswa."""
    data_siswa = []
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            for baris in file:
                baris = baris.strip()
                if baris:
                    parts = baris.split(",")
                    if len(parts) == 2:
                        nama = parts[0].strip()
                        try:
                            nilai = float(parts[1].strip())
                            # Validasi rentang nilai 0 - 100
                            if 0 <= nilai <= 100:
                                data_siswa.append({"nama": nama, "nilai": nilai})
                            else:
                                print(f"Peringatan: Nilai {nilai} untuk {nama} di luar batas (0-100), diabaikan.")
                        except ValueError:
                            print(f"Peringatan: Format nilai tidak valid untuk {nama}.")
    except FileNotFoundError:
        print(f"Error: File pada path '{filepath}' tidak ditemukan.")
    return data_siswa