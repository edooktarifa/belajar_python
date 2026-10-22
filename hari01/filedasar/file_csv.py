import csv

data = [
    ["nama", "umur", "kota"],
    ["budi", 20, "Jakarta"],
    ["Sari", 17, "Bandung"]
]

with open("siswa.csv", "w", newline="") as f:
    penulis = csv.writer(f)
    for baris in data:
        penulis.writerow(baris)


with open("siswa.csv", "r", newline="") as f:
    pembaca = csv.reader(f)
    for baris in pembaca:
        print(baris)