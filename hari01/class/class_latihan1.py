
class Mobil:
    def __init__(self, merk, warna):
        self.merk = merk
        self.warna = warna

    def info(self):
        return ("Merek mobil " + self.merk + " Dengan warna " + self.warna)


mb1 = Mobil(merk="Toyota", warna="merah")
mb2 = Mobil(merk="Honda", warna="hitam")

print(f"Mobil 1 {mb1.merk} warna {mb1.warna}")
print(f"Mobil 2 {mb2.merk} warna {mb2.warna}")


print(f"Mb1 {mb1.info()} ==== Mb2 {mb2.info()}")

class Siswa:
    def __init__(self, nama, nilai):
        self.nama = nama
        self.nilai = nilai

    def lulus(self):
        return "Lulus" if self.nilai >= 70 else "Tidak Lulus"
        
sw1 = Siswa(nama="Budi", nilai=70)
sw2 = Siswa(nama="Sari", nilai=69)

print(sw1.lulus())
print(sw2.lulus())