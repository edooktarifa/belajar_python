import random

randomAngka = random.randint(1,10)
print("kunci jawaban adalah", randomAngka)

while True:
    tebakAngka = int(input("Tebak angka antara 1 sampai 10: "))

    if tebakAngka == randomAngka:
        print("Selamat, tebakan anda benar!")
        break

    elif tebakAngka < randomAngka:
        print("Tebakan anda terlalu rendah, coba lagi.")

    else:
        print("Tebakan anda terlalu tinggi, coba lagi.")