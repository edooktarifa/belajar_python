

with open("daftar_harga.txt", "w") as f:
    f.write("apel \n")
    f.write("mangga \n")

with open("daftar_harga.txt", "a") as f:
    f.write("jeruk\n")


buah = []
with open("daftar_harga.txt", "r") as f:
    for i in f:
        buah.append(i.strip())

print(buah)