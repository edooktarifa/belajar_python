from .repository import save_todo, load_todos

def create_todo(title):
    if not title:
        print("title tidak boleh kosong")

def get_all_todos():
    pass

def find_todo_by_id(todo_id):
    pass

def mark_done(todo_id):
    pass

def rename_todo(todo_id, new_title):
    pass

def remove_todo(todo_id):
    pass

def count_done():
    pass

def generate_id():
    pass