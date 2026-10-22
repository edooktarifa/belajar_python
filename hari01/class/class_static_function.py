
class Rekening:
    nama_bank = "Bank Nusantara"

    def __init__(self, pemilik, saldo):
        self.pemilik = pemilik
        self.saldo = saldo

    def info(self):
        print(f"{self.pemilik} : Rp{self.saldo}")

    @staticmethod
    def hitung_bunga(saldo, persen):
        return saldo * persen/100


print(Rekening.hitung_bunga(saldo=100000, persen=10))


# Latihan
class RekeningLatihan:

    @staticmethod
    def rupiah(jumlah):
        return f"Rp {jumlah:,}".replace(",", ".")


print(RekeningLatihan.rupiah(jumlah=15000000))