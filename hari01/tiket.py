umur = int(input("Berapa umur anda? "))
hari_nonton = input("pilih hari buat nonton? ")

if umur < 5:
    harga = 0
elif umur <= 12:
    harga = 25000
elif umur <= 59:
    harga = 50000
else:
    harga = 30000

if hari_nonton == "weekend" and harga != 0:
    harga += 10000

print(f"Harga tiket anda adalah {harga}")