class Kendaraan:
    def __init__(self, merek, tahun):
        self.merek = merek
        self.tahun = tahun

    def label(self):
        return f"{self.merek} ({self.tahun})"

    def biaya_parkir(self, jam, diskon):
        return 2_000 * jam - diskon


class Mobil(Kendaraan):
    def biaya_parkir(self, jam, diskon):
        return 5_000 * jam - diskon


class Motor(Kendaraan):
    def biaya_parkir(self, jam, diskon):
        return super().biaya_parkir(diskon=diskon, jam=jam) // 2


daftar_kendaraan = [
    Kendaraan(merek="Suzuki", tahun=2018),
    Mobil(merek="Toyota", tahun=2020),
    Motor(merek="Honda", tahun=2022),
]

total_biaya = 0
for kendaraan in daftar_kendaraan:
    biaya = kendaraan.biaya_parkir(jam=3, diskon=1_000)
    total_biaya += biaya
    print(f"{kendaraan.label()}: {biaya}")

print(f"Total: {total_biaya}")