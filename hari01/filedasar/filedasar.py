
class FileTidakDitemukan(Exception):
    pass

class FileKosong(Exception):
    pass


def check_file(file_name):
    try:
        with open(file_name, "r") as f:
            isi = f.read()
            if isi == "":
                return FileKosong("File " + file_name + " kosong")
            return isi
    except:
        raise FileTidakDitemukan("File " + file_name + "tidak ditemukan")


with open("catatan", "w") as f:
    f.write("mantaps")


try:
    isi = check_file("catatan")
    print(isi)
except FileKosong as e:
    print("Error", e)

except FileTidakDitemukan as e:
    print("Error",e)
