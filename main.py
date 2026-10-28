from src.proses import ringkasan

def main():
    data_nilai = [75, 80, 60, 90, 45, 85]
    
    print("=== PROGRAM ANALISIS NILAI SISWA ===")
    print(f"Data Nilai: {data_nilai}")
    
    hasil = ringkasan(data_nilai)
    
    print("\n--- Ringkasan Statistik ---")
    for kunci, nilai in hasil.items():
        print(f"{kunci.capitalize()}: {nilai}")

if __name__ == "__main__":
    main()