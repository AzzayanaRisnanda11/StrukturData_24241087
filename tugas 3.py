# Global variable untuk menyimpan data mahasiswa
data_mahasiswa = []

# Fungsi untuk Create
def create_mahasiswa():
    nama = input("Masukkan nama mahasiswa: ")
    data_mahasiswa.append(nama)
    print(f"Mahasiswa '{nama}' berhasil ditambahkan.")

# Fungsi untuk Read
def read_mahasiswa():
    if not data_mahasiswa:
        print("Belum ada data mahasiswa.")
    else:
        print("Daftar Mahasiswa:")
        for idx, nama in enumerate(data_mahasiswa):
            print(f"{idx}. {nama}")

# Fungsi untuk Update
def update_mahasiswa():
    read_mahasiswa()
    try:
        indeks = int(input("Masukkan indeks mahasiswa yang ingin diubah: "))
        if 0 <= indeks < len(data_mahasiswa):
            nama_baru = input("Masukkan nama baru: ")
            data_mahasiswa[indeks] = nama_baru
            print(f"Mahasiswa pada indeks {indeks} berhasil diubah menjadi '{nama_baru}'.")
        else:
            print("Indeks tidak valid.")
    except ValueError:
        print("Input harus berupa angka.")

# Fungsi untuk Delete
def delete_mahasiswa():
    read_mahasiswa()
    try:
        indeks = int(input("Masukkan indeks mahasiswa yang ingin dihapus: "))
        if 0 <= indeks < len(data_mahasiswa):
            nama = data_mahasiswa.pop(indeks)
            print(f"Mahasiswa '{nama}' berhasil dihapus.")
        else:
            print("Indeks tidak valid.")
    except ValueError:
        print("Input harus berupa angka.")

# Main loop
def main():
    while True:
        print("\nMenu:")
        print("1. Tambah Mahasiswa")
        print("2. Tampilkan Mahasiswa")
        print("3. Ubah Mahasiswa")
        print("4. Hapus Mahasiswa")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            create_mahasiswa()
        elif pilihan == '2':
            read_mahasiswa()
        elif pilihan == '3':
            update_mahasiswa()
        elif pilihan == '4':
            delete_mahasiswa()
        elif pilihan == '5':
            print("Keluar dari program.")
            exit()
        else:
            print("Pilihan tidak valid, coba lagi.")

# Menjalankan program
if __name__ == "_main_":
    main()