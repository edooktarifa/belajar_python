import random

angka = random.randint(1,10)
kesempatan = 0
maxKesempatan = 5

print(f"Jawabannya adalah {angka}")

while True:
    tebakAngka = int(input("Tebak angka antara 1 sampai 10: "))
    kesempatan += 1

    if tebakAngka == angka:
        print(f"Benar! Kamu butuh {kesempatan} tebakan untuk menebak angka yang benar.")
        break  

    else:
        if kesempatan == maxKesempatan:
            print("Kesempatan anda habis, jawaban yang benar adalah", angka)
            break
        else: 
            sisaPercobaan = maxKesempatan - kesempatan      
            print(f"Tebakan anda salah sisa percobaan tinggal {sisaPercobaan} kali lagi.")