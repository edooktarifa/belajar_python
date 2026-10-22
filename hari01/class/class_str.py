

class Kucing:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def __str__(self):
        return f"nama kucing {self.nama}, umur {self.umur} tahun"


k1 = Kucing(nama="Tom", umur=5)
print(k1)