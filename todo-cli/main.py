
from tasks import tambah_tugas, lihat_tugas, tandai_selesai, edit_tugas, hapus_tugas, input_nomor

def tampilkan_menu():
    print("\n=== TO-DO LIST ===")
    print("1. Tambah tugas")
    print("2. Lihat tugas")
    print("3. Tandai selesai")
    print("4. Edit tugas")
    print("5. Hapus tugas")
    print("6. Keluar")

def jalankan():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            judul = input("Judul tugas: ").strip()
            if not judul:
                print("Judul tugas tidak boleh kosong.")
            else:
                tambah_tugas(judul)
        elif pilihan == "2":
            lihat_tugas()
        elif pilihan == "3":
            id_tugas = input_nomor("Masukkan ID tugas yang ingin ditandai selesai: ")
            if id_tugas is None:
                continue
            if tandai_selesai(int(id_tugas)):
                print(f"Tugas dengan ID {id_tugas} telah ditandai selesai.")
            else:
                print(f"Tugas dengan ID {id_tugas} tidak ditemukan.")
        if pilihan == "4":
            lihat_tugas()
            id_tugas = input_nomor("Masukkan ID tugas yang ingin diedit: ")
            if id_tugas is None:
                continue
            judul_baru = input("Masukkan judul baru: ").strip()
            if not judul_baru:
                print("Judul tugas tidak boleh kosong.")
            else:
                edit_tugas(id_tugas=id_tugas, judul_baru=judul_baru)
        elif pilihan == "5":
            lihat_tugas()
            id_tugas = input_nomor("Masukkan ID tugas yang ingin dihapus: ")
            if id_tugas is None:
                continue
            hapus_tugas(id_tugas=id_tugas)
        elif pilihan == "6":
            print("Sampai jumpa!")
            break

jalankan()