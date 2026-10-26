
class Karyawan:
    def __init__(self, nama, gaji):
        self.nama = nama
        self.gaji = gaji

    def bagi_bonus(self, jumlah_penerima):
        return self.gaji / jumlah_penerima


karyawan = Karyawan(nama="Sari", gaji=6000000)

try:
    hasil = karyawan.bagi_bonus(jumlah_penerima=4)
except ZeroDivisionError:
    print("Jumlah penerima tidak boleh 0")
else:
    print(f"{karyawan.nama}: bonus per orang Rp{hasil}")
finally:
    print(f"Selesai hitung bonus untuk {karyawan.nama}")