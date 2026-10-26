
class Karyawan:
    def __init__(self, nama, gaji):
        self.nama = nama
        self.gaji = gaji

    def hitung_gaji_perhari(self, hari_kerja):
        return self.gaji/hari_kerja


karyawan = Karyawan(nama="Sari", gaji=6000000)


try:
    gaji = karyawan.hitung_gaji_perhari(hari_kerja=20)
    print(f"{karyawan.nama}: gaji per hari Rp {gaji}")

except ZeroDivisionError:
    print("Hari kerja tidak boleh 0")

print("Program selesai")

try:
    gaji = karyawan.hitung_gaji_perhari(hari_kerja=0)
    print(f"{karyawan.nama}: gaji per hari Rp {gaji}")

except ZeroDivisionError:
    print("Hari kerja tidak boleh 0")

print("Program selesai")