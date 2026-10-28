
class Rekening:
    def __init__(self, pemilik, saldo):
        self.pemilik = pemilik
        self.saldo = saldo

    def setor(self, jumlah):
        return self.saldo + jumlah