
class Kendaraan:
    def __init__(self, merek, tahun):
        self.merek = merek
        self.tahun = tahun

    def jalan(self):
        print(f"{self.merek} ({self.tahun}) mulai berjalan")

    def klakson(self):
        print(f"{self.merek} bilang: tin tin!")


class Mobil(Kendaraan):
    pass

avanza = Mobil(merek="Toyota", tahun=2020)
avanza.jalan()
avanza.klakson()