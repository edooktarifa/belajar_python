
# Kalkulator ini nama class nya
# kalkulator ini adalah nama filenya

# from kalkulator import Kalkulator, format_angka

import kalkulator as kal

kalkulator = kal.Kalkulator(angka_awal=8000000)
hasil_tambah = kal.format_angka(kalkulator.tambah(nilai=500000))
hasil_kali = kal.format_angka(kalkulator.kali(nilai=2))
hasil_persen = kal.format_angka(kalkulator.persen(persentase=5))

print(f"Angka awal: {kalkulator.angka_awal}")
print(f"tambah 500000: {hasil_tambah}")
print(f"kali 2: {hasil_kali}")
print(f"persen 5: {hasil_persen}")
