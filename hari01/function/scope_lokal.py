
# hitungan = 0

# def tambah_satu():
#     return hitungan + 1

# print(tambah_satu())

# angka = 0
# def hitung():
#     global angka
#     angka = 5

# hitung()
# print(angka)


def terbesar_kecil(a,b):
    if a < b:
        return (a, b)
    return (b,a)


print(terbesar_kecil(2,5))