
class Kucing:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def mengeong(self):
        return (self.nama + " sedang mengeong")


k1 = Kucing(nama="Tom", umur=10)
print(k1.mengeong())