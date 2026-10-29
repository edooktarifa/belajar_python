# latihan_import.py

import math
from math import floor
import datetime as dt


class Karyawan:
    def __init__(self, nama, gaji):
        self.nama = nama
        self.gaji = gaji

    def hitung_gaji_per_hari(self, hari_kerja):
        return self.gaji / hari_kerja

    def gaji_dibulatkan_atas(self, hari_kerja):
        return math.ceil(self.hitung_gaji_per_hari(hari_kerja=hari_kerja))

    def gaji_dibulatkan_bawah(self, hari_kerja):
        return floor(self.hitung_gaji_per_hari(hari_kerja=hari_kerja))


karyawan = Karyawan(nama="Sari", gaji=6000000)
tanggal_cetak = dt.date(year=2026, month=11, day=1)
gaji_per_hari = karyawan.hitung_gaji_per_hari(hari_kerja=22)

print(f"Tanggal cetak: {tanggal_cetak}")
print(f"{karyawan.nama}: gaji per hari Rp{gaji_per_hari:.2f}")
print(f"Dibulatkan atas: Rp{karyawan.gaji_dibulatkan_atas(hari_kerja=22)}")
print(f"Dibulatkan bawah: Rp{karyawan.gaji_dibulatkan_bawah(hari_kerja=22)}")
