
class Rekening:
    nama_bank = "Bank Nusantara"
    jumlah_rekening = 0

    def __init__(self, pemilik, saldo):
        self.pemilik = pemilik
        self.saldo = saldo
        Rekening.jumlah_rekening += 1

    def info(self):
        print(f"{self.pemilik} :Rp{self.saldo}")

    def setor(self, jumlah):
        self.saldo += jumlah

    @classmethod
    def info_bank(cls):
        print(f"{cls.nama_bank} memiliki {cls.jumlah_rekening} rekening")


r1 = Rekening(pemilik="Budi", saldo=100000)
r2 = Rekening(pemilik="Sari", saldo=50000)

r1.setor(jumlah=25000)
r1.info()
r2.info()
Rekening.info_bank()