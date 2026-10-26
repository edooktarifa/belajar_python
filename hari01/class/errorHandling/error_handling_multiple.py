# latihan_multiple_except.py

class Karyawan:
    def __init__(self, nama, gaji):
        self.nama = nama
        self.gaji = gaji

    def bagi_bonus(self, jumlah_penerima):
        return self.gaji / jumlah_penerima


karyawan = Karyawan(nama="Sari", gaji=6000000)

try:
    bonus_per_orang = karyawan.bagi_bonus(jumlah_penerima=3)
    print(f"{karyawan.nama}: bonus per orang Rp{bonus_per_orang}")
except ZeroDivisionError:
    print("Jumlah penerima tidak boleh 0")
except TypeError as error:
    print(f"Tipe data salah: {error}")

try:
    bonus_per_orang = karyawan.bagi_bonus(jumlah_penerima=0)
    print(f"{karyawan.nama}: bonus per orang Rp{bonus_per_orang}")
except ZeroDivisionError:
    print("Jumlah penerima tidak boleh 0")
except TypeError as error:
    print(f"Tipe data salah: {error}")

try:
    bonus_per_orang = karyawan.bagi_bonus(jumlah_penerima="tiga")
    print(f"{karyawan.nama}: bonus per orang Rp{bonus_per_orang}")
except ZeroDivisionError:
    print("Jumlah penerima tidak boleh 0")
except TypeError as error:
    print(f"Tipe data salah: {error}")