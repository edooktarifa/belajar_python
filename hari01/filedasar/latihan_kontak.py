import csv

NAMA_FILE = "kontak.csv"
KOLOM = ["nama", "telepon"]


def muat_kontak():
    try:
        with open(NAMA_FILE, "r", newline="") as f:
            return list(csv.DictReader(f))
    except FileNotFoundError:
        return []


def simpan_kontak(daftar):
    with open(NAMA_FILE, "w", newline="") as f:
        penulis = csv.DictWriter(f, fieldnames=KOLOM)
        penulis.writeheader()

        for kontak in daftar:
            penulis.writerow(kontak)


daftar = muat_kontak()
print(daftar)
daftar.append({"nama": "Budi", "telepon": "0812"})
simpan_kontak(daftar)

print(muat_kontak())