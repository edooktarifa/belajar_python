
def read_number(prompt):
    try:
        return int(input(prompt))
    except:
        print("Anda harus memasukkan angka")
        return None

def read_text(prompt):
    pass