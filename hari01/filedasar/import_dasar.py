import math
from math import ceil
import datetime as dt

class Karyawan:
    def __init__(self, nama, gaji):
        self.nama = nama
        self.gaji = gaji

    def hitung_gaji_per_hari(self,hari_kerja):
        return self.gaji / hari_kerja

    def gaji_dibulatkan_atas(self, hari_kerja):
        return ceil(self.hitung_gaji_per_hari(hari_kerja=hari_kerja))

    def gaji_dibulatkan_kebawah(self, hari_kerja):
        return math.floor(self.hitung_gaji_per_hari(hari_kerja=hari_kerja))

karyawan = Karyawan(nama="Budi", gaji=5000000)
tanggal_cetak = dt.date(year=2026, month=10, day=26)

print(f"Tanggal cetak: {tanggal_cetak}")
print(f"{karyawan.nama}: gaji per hari Rp{karyawan.hitung_gaji_per_hari(hari_kerja=22)}")
print(f"Dibulatkan keatas: Rp{karyawan.gaji_dibulatkan_atas(hari_kerja=22)}")
print(f"Dibulatkan bawah: Rp{karyawan.gaji_dibulatkan_kebawah(hari_kerja=22)}")