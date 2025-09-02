#daftar_tugas.py

tugas = []

def tambah_tugas(nama):
    tugas.append(nama)
    print(f"Tugas '{nama}' berhasil ditambahkan!")
    
def tampilkan_tugas():
    if not tugas:
        print("belum ada tugas.")
    else:
        print("\nDaftar Tugas: ")
        for i, t in enumerate(tugas, 1):
            print(f"{i}. {t}")
            
# Tes program
if __name__ == "__main__":
    while True:
        print("\n=== Menu Daftar Tugas ===")
        print("1. Tambah Tugas")
        print("2. Lihat Tugas")
        print("3. Keluar")

        pilihan = input("Pilih menu (1/2/3): ")

        if pilihan == "1":
            nama = input("Masukkan nama tugas: ")
            tambah_tugas(nama)
        elif pilihan == "2":
            tampilkan_tugas()
        elif pilihan == "3":
            print("Keluar dari program. Sampai jumpa! 👋")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")