

# Karyawan ini nama class nya
# karyawan ini adalah nama filenya

from karyawan import Karyawan, format_rupiah

karyawan = Karyawan(nama="Budi", gaji=5000000)
gaji_per_hari = karyawan.hitung_gaji_per_hari(hari_kerja=22)

print(f"{karyawan.nama}: gaji per hari {format_rupiah(angka=gaji_per_hari)}")