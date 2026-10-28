

class Kalkulator:
    def __init__(self, angka_awal):
        self.angka_awal = angka_awal

    def tambah(self, nilai):
        return self.angka_awal + nilai

    def kali(self, nilai):
        return self.angka_awal * nilai

    def persen(self, persentase):
        return self.angka_awal * persentase / 100

def format_angka(angka):
    return f"{angka:,.0f}"