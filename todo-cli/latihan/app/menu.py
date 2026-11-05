
from .manager import create_todo, get_all_todos

def show_menu():
    print("\n=== Todo App ===")
    print("1. Tambah todo")
    print("2. Lihat semua todo")
    print("3. Tandai selesai")
    print("4. Ubah judul todo")
    print("5. Hapus todo")
    print("6. Keluar")

def handle_add():
    pass

def handle_list():
    get_all_todos()

def handle_complete():
    pass

def handle_rename():
    pass

def handle_remove():
    pass


