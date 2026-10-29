from data.storage import simpan_data, muat_data


daftar_tugas = muat_data()


def tambah_tugas(judul):
    if len(daftar_tugas) == 0:
        id_baru = 1
    else:
        id_baru = daftar_tugas[-1]["id"] + 1
    tugas_baru = {
        "id": id_baru,
        "judul": judul,
        "selesai": False
    }
    daftar_tugas.append(tugas_baru)
    simpan_data(daftar_tugas)


def lihat_tugas():
    if len(daftar_tugas) == 0:
        print("Belum ada tugas.")
        return

    jumlah_selesai = 0

    for tugas in daftar_tugas:
        if tugas["selesai"]:
            status = "✓"
            jumlah_selesai += 1
        else:
            status = " "
        print(f"{tugas['id']}. [{status}] {tugas['judul']}")

    print(f"\nSelesai: {jumlah_selesai} dari {len(daftar_tugas)} tugas")


def tandai_selesai(id_tugas):
    tugas = cari_tugas(id_tugas=id_tugas)
    if tugas is None:
        return False

    tugas["selesai"] = True
    simpan_data(daftar_tugas)
    return True

def edit_tugas(id_tugas, judul_baru):
    tugas = cari_tugas(id_tugas=id_tugas)
    if tugas is None:
        return False
    tugas["judul"] = judul_baru
    simpan_data(daftar_tugas)
    return True


def hapus_tugas(id_tugas):
    tugas = cari_tugas(id_tugas)
    if tugas is None:
        return False
    daftar_tugas.remove(tugas)
    simpan_data(daftar_tugas)
    return True

def input_nomor(pertanyaan):
    try:
        return int(input(pertanyaan))
    except ValueError:
        print("Input tidak valid. Harap masukkan nomor yang benar.")
        return None

def cari_tugas(id_tugas):
    for tugas in daftar_tugas:
        if tugas["id"] == id_tugas:
            return tugas
    return None