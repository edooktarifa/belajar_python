
def hitung(a,b):
    jumlah = a + b
    selisih = a - b
    return (jumlah, selisih)

get_jumlah, get_selisih = hitung(10,9)

print(get_jumlah, get_selisih)



def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

def check_lulus(nilai):
    if nilai >= 70:
        return "Lulus"
    return "Tidak Lulus"

def statistik(a,b):
    kali = a * b
    bagi = a / b
    return kali, bagi

print(luas_persegi_panjang(10, 10))
print(check_lulus(80))

hasil_kali, hasil_bagi = statistik(10,10)
print(hasil_kali)
print(hasil_bagi)