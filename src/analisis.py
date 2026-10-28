def hitung_statistik(data_siswa):
    """Menghitung rata-rata, nilai minimum, dan maksimum dari data siswa."""
    if not data_siswa:
        return {"rata_rata": 0, "min": 0, "max": 0}

    nilai_list = [siswa["nilai"] for siswa in data_siswa]
    rata = sum(nilai_list) / len(nilai_list)
    nilai_min = min(nilai_list)
    nilai_max = max(nilai_list)

    return {
        "rata_rata": round(rata, 2),
        "min": nilai_min,
        "max": nilai_max
    }

def hitung_ketuntasan(data_siswa, kkm=60):
    """Menghitung jumlah siswa tuntas dan belum tuntas berdasarkan KKM."""
    tuntas = 0
    belum_tuntas = 0

    for siswa in data_siswa:
        if siswa["nilai"] >= kkm:
            tuntas += 1
        else:
            belum_tuntas += 1

    return {
        "tuntas": tuntas,
        "belum_tuntas": belum_tuntas,
        "total_siswa": len(data_siswa)
    }