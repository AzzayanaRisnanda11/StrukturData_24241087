def main():
    mahasiswa = {}

    jumlah_mhs = int(input("Masukkan jumlah mahasiswa: "))

    for _ in range(jumlah_mhs):
        nim = input("Masukkan NIM: ")
        nama = input("Masukkan Nama: ")

        mata_kuliah = {}
        while True:
            mk = input("Masukkan nama mata kuliah (atau ketik 'selesai' untuk berhenti): ")
            if mk.lower() == 'selesai':
                break
            nilai = float(input(f"Masukkan nilai untuk mata kuliah {mk}: "))
            mata_kuliah[mk] = nilai

        mahasiswa[nim] = {
            'nama': nama,
            'mata_kuliah': mata_kuliah
        }

    print("\n--- Rekap Nilai Mahasiswa ---")
    for nim, data in mahasiswa.items():
        nama = data['nama']
        nilai_list = list(data['mata_kuliah'].values())
        rata_rata = sum(nilai_list) / len(nilai_list) if nilai_list else 0
        print(f"NIM: {nim}")
        print(f"Nama: {nama}")
        print("Mata Kuliah dan Nilai:")
        for mk, nilai in data['mata_kuliah'].items():
            print(f"  - {mk}: {nilai}")
        print(f"Rata-rata Nilai: {rata_rata:.2f}\n")

if __name__ == "_main_":
    main()