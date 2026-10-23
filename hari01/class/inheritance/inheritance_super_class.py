
class Kendaraan:
    def __init__(self, merek, tahun):
        self.merek = merek
        self.tahun = tahun

    def info(self):
        print(f"{self.merek} ({self.tahun})")


class Mobil(Kendaraan):
    def __init__(self, merek, tahun, jumlah_pintu):
        super().__init__(merek, tahun)
        self.jumlah_pintu = jumlah_pintu

    def info_pintu(self):
        print(f"{self.merek} punya {self.jumlah_pintu} pintu")


avanza = Mobil(merek="Toyota", tahun=2020, jumlah_pintu=5)

avanza.info()
avanza.info_pintu()