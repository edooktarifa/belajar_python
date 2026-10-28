from hitung import Karyawan, format_rupiah

hitung = Karyawan(nama="Jhon", gaji=6000000)
hitung_bonus = hitung.hitung_bonus(persen=10)

gaji = format_rupiah(angka=hitung.gaji)
bonus = format_rupiah(angka=hitung_bonus)

print(f"{hitung.nama}: gaji {gaji}")
print(f"{hitung.nama}: bonus {bonus}")