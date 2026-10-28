
def hitung_diskon(harga, persen):
    return harga - harga * persen / 100

def format_rupiah(angka):
    return f"Rp{angka:,.0f}"