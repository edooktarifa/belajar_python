
class Kendaraan: 
    def __init__(self, merek, tahun, harga):
        self.merek = merek
        self.tahun = tahun
        self.harga = harga

    def label(self):
        return f"{self.merek} ({self.tahun})"

    def hitung_pajak(self):
        return self.harga * 2 // 100


class Truk(Kendaraan):
    def label(self):
        return f"[TRUK] {self.merek} ({self.tahun})"

# override hitung pajak parent + 500_000
class Bus(Kendaraan):
    def hitung_pajak(self):
        return super().hitung_pajak() + 500_000


sedan = Kendaraan(merek="Suzuki", tahun=2018, harga=150_000_000)
hino = Truk(merek="Hino", tahun=2019, harga=400_000_000)
mercy = Bus(merek="Mercedes", tahun=2021, harga=600_000_000)

print(sedan.label())
print(sedan.hitung_pajak())
print(hino.label())
print(hino.hitung_pajak())
print(mercy.label())
print(mercy.hitung_pajak())