
class Karyawan:
    def __init__(self, nama, gaji):
        self.nama = nama
        self.gaji = gaji

    def hitung_gaji_per_hari(self,hari_kerja):
        return self.gaji / hari_kerja

def format_rupiah(angka):
    return f"Rp{angka:,.2f}"