# latihan_validasi.py

class Karyawan:
    def __init__(self, nama, gaji):
        if gaji < 0:
            raise ValueError("Gaji tidak boleh negatif")
        self.nama = nama
        self.gaji = gaji

    def potong_gaji(self, jumlah_potongan):
        if not isinstance(jumlah_potongan, (int, float)):
            raise TypeError("Potongan harus berupa angka")
        if jumlah_potongan <= 0 or jumlah_potongan > self.gaji:
            raise ValueError("Potongan harus lebih dari 0 dan tidak boleh melebihi gaji")
        self.gaji -= jumlah_potongan
        return self.gaji


karyawan = Karyawan(nama="Sari", gaji=6000000)
daftar_potongan = [500000, 0, 9000000, "lima ratus ribu"]

for potongan in daftar_potongan:
    try:
        gaji_setelah_potongan = karyawan.potong_gaji(jumlah_potongan=potongan)
    except ValueError as error:
        print(f"Gagal (nilai): {error}")
    except TypeError as error:
        print(f"Gagal (tipe): {error}")
    else:
        print(f"{karyawan.nama}: gaji setelah potongan Rp{gaji_setelah_potongan}")

try:
    karyawan_andi = Karyawan(nama="Andi", gaji=-100)
except ValueError as error:
    print(f"Gagal buat karyawan: {error}")