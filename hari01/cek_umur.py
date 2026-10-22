
# nilai = int(input("berapa nilai yang anda dapatkan? "))


# if nilai >= 100:
#     print("Nilai anda sangat memuaskan")
# elif nilai >= 80:
#     print("Nilai anda memuaskan")
# elif nilai >= 70:
#     print("Nilai anda normal")
# else:
#     print("Nilai anda di bawah rata rata")


umur = int(input("Berapa umur anda? "))
punya_ktp = input("Apakah anda sudah punya KTP? (ya/tidak) ")

if umur >= 17 and punya_ktp:
    print("Anda sudah boleh membuat SIM")
elif umur >= 17 and not punya_ktp:
    print("Anda sudah boleh membuat SIM, tapi harus membuat KTP dulu")
else:
    print("Anda belum boleh membuat SIM")