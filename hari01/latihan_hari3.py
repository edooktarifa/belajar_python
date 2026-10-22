nama = input("Siapa nama anda? ")
umur = int(input("Berapa umur anda? "))
tinggi = float(input("Berapa tinggi badan anda? "))
berat = float(input("Berapa berat badan anda? "))

bmi = berat / (tinggi * tinggi)
print(f"Hallo, {nama}" )
print(f"umurmu {umur} tahun")
print(f"BMI kamu: {bmi:.2f}")
