

class Product:
    toko = "Toko Maju"
    jumlah_product = 0

    def __init__(self, nama, harga, stock):
        self.nama = nama
        self.harga = harga
        self.stock = stock

    def jual(self, jumlah):
        self.stock -= jumlah

    def total_harga(self, jumlah):
        return jumlah * self.harga

    def info(self):
        print(f"product {self.nama} harga {self.harga} stock {self.stock}") 


p1 = Product(nama="Pensil", harga=2000, stock=10)
p1.info()
p1.jual(jumlah=3)
p1.info()
print(p1.total_harga(jumlah=5))


# Latihan
class Rekening: 
    nama_bank = "Bank Nusantara"
    jumlah_rekening = 0

    def __init__(self, pemilik, saldo):
        self.pemilik = pemilik
        self.saldo = saldo
        Rekening.jumlah_rekening += 1

    def info(self):
        print(f"{self.pemilik} : Rp{self.saldo}")

    def setor(self, jumlah):
        self.saldo += jumlah

    def tarik(self, jumlah):
        self.saldo -= jumlah

    def cek_cukup(self, jumlah):
        return True if self.saldo >= jumlah else False 

    def info_bank(self):
        print(f"Bank Nusantara memiliki {Rekening.jumlah_rekening} rekening")


r1 = Rekening(pemilik="Budi", saldo=100000)
r2 = Rekening(pemilik="Sari", saldo=50000)
r1.info()
r1.setor(jumlah=25000)
r1.info()
r1.tarik(jumlah=30000)
r1.info()

print(f"{r2.cek_cukup(jumlah=80000)}")
r1.info_bank()