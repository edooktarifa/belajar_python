

class Siswa:
    sekolah = "SMA 1"
    jumlah_siswa = 0

    def __init__(self, nama, nilai):
        self.nama = nama
        self.nilai = nilai
        Siswa.jumlah_siswa += 1



sw1 = Siswa(nama="Toni", nilai=80)
print(f"jumlah sw {sw1.jumlah_siswa}")
sw2 = Siswa(nama="Doni", nilai=60)

print(f"jumlah siswa sw1 {sw1.jumlah_siswa} dan jumlah siswa sw2 {sw2.jumlah_siswa}")

# Latihan Mini

class Product:

    jumlah_product = 0

    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga
        Product.jumlah_product += 1


p1 = Product(nama="Toko maju", harga=50)
p2 = Product(nama="Toko maju", harga=50)

print(f"jumlah product p1 {p1.jumlah_product} dan jumlah p2 {p2.jumlah_product}")