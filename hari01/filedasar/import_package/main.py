

# toko adalah folder, produk adalah nama filenya

from toko.produk import Produk
from toko import harga

produk = Produk(nama="Sepatu", harga=500000)
harga_diskon = harga.hitung_diskon(harga=produk.harga, persen=20)

print(f"{produk.nama}: harga normal {harga.format_rupiah(angka=produk.harga)}")
print(f"{produk.nama}: harga diskon {harga.format_rupiah(angka=harga_diskon)}")