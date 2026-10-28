
class Karyawan:
    def __init__(self, nama, gaji):
        self.nama = nama
        self.gaji = gaji

    def hitung_bonus(self, persen):
        return self.gaji * persen/100

def format_rupiah(angka):
    return f"Rp{angka:,.0f}"
