import json

NAME_FILE = "data/tasks.json"

def simpan_data(tugas):
    with open(NAME_FILE, "w") as file:
        json.dump(tugas, file, indent=2)

def muat_data():
    try:
        with open(NAME_FILE, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("File JSON tidak valid. Membuat file baru.")
        return []

    if not isinstance(data, list):
        print("Format data salah. Memulai dengan daftar kosong.")
        return []

    return data