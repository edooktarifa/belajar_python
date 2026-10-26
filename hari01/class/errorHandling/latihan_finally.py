# latihan_finally.py

class Karyawan:
    def __init__(self, nama, gaji):
        self.nama = nama
        self.gaji = gaji

    def bagi_bonus(self, jumlah_penerima):
        return self.gaji / jumlah_penerima


def hitung_bonus(karyawan, jumlah_penerima):
    try:
        bonus_per_orang = karyawan.bagi_bonus(jumlah_penerima=jumlah_penerima)
    except ZeroDivisionError:
        print("Jumlah penerima tidak boleh 0")
    else:
        print(f"{karyawan.nama}: bonus per orang Rp{bonus_per_orang}")
    finally:
        print(f"Selesai hitung bonus untuk {karyawan.nama}")


karyawan = Karyawan(nama="Sari", gaji=6000000)

hitung_bonus(karyawan=karyawan, jumlah_penerima=4)
hitung_bonus(karyawan=karyawan, jumlah_penerima=0)