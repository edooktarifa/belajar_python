
class Kucing:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def __str__(self):
        return f"nama kucing {self.nama}, umur {self.umur} tahun"



k1 = Kucing(nama="Tom", umur=5)
print(k1)

k1.umur = 7
print(k1)

# cara ke 2

class ModifiedKucing:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def update_umur(self, updateUmur):
        self.umur = updateUmur

    def __str__(self):
        return f"nama kucing saya {self.nama} umurnya sekarang {self.umur} tahun"


k2 = ModifiedKucing(nama="Tom2", umur=5)
print(k2)

k2.update_umur(updateUmur=7)
print(k2)