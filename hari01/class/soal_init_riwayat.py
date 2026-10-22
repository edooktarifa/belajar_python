class Produk:
    def __init__(self, nama, harga, stok=0):
        if harga <= 0:
            raise ValueError("Harga harus lebih dari 0")
        if stok < 0:
            raise ValueError("Stok tidak boleh negatif")

        self.nama = nama
        self.harga = harga
        self.stok = stok
        self.terjual = 0
        self.riwayat = []

    def info(self):
        print(f"{self.nama}: Rp{self.harga}, stok {self.stok}, terjual {self.terjual}")

    def tambah_stok(self, jumlah):
        self.stok += jumlah
        self.riwayat.append(f"Tambah stok {jumlah}")

    def jual(self, jumlah):
        if self.stok >= jumlah:
            self.stok -= jumlah
            self.terjual += jumlah
            self.riwayat.append(f"Jual {jumlah}")
        else:
            print("Stok tidak cukup")

    def cetak_riwayat(self):
        for catatan in self.riwayat:
            print(catatan)


p1 = Produk(nama="Pensil", harga=2000, stok=10)
p2 = Produk(nama="Buku", harga=5000)

p1.jual(jumlah=3)
p1.tambah_stok(jumlah=5)
p1.jual(jumlah=20)
p2.jual(jumlah=1)

p1.info()
p2.info()
p1.cetak_riwayat()
p2.cetak_riwayat()