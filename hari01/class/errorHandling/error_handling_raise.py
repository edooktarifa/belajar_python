
class Karyawan:
    def __init__(self, nama, gaji):
        self.nama = nama
        self.gaji = gaji

    def hitung_per_hari(self, hari_kerja):
        if hari_kerja <= 0:
            raise ValueError("Hari kerja harus lebih dari 0")
        return self.gaji/hari_kerja

    def cetak_gaji_per_hari(self, hari_kerja):
        try:
            hitung_gaji_per_hari = self.hitung_per_hari(hari_kerja=hari_kerja)

        except ValueError as error:
            raise

        else:
            return hitung_gaji_per_hari


karyawan = Karyawan(nama="Sari", gaji=6000000)
total_hari_kerja = [20, 0, -5]

for hari in total_hari_kerja:
    try:
        gaji_per_hari = karyawan.cetak_gaji_per_hari(hari_kerja=hari)
    except ValueError as error:
        print(f"Gagal: {error}")
    else:
        print(f"{karyawan.nama}: gaji per hari Rp{gaji_per_hari}")