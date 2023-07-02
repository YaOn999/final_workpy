from datetime import datetime
from note import Note


def print_menu():
    print("1. Просмотреть все заметки")
    print("2. Создать новую заметку")
    print("3. Редактировать заметку")
    print("4. Удалить заметку")
    print("5. Выйти")


def load_notes():
    notes = Note.load_all()
    for note in notes:
        print(f"Заметка #{note.id}")
        print(f"Заголовок: {note.title}")
        print(f"Тело: {note.body}")
        print(f"Дата создания: {note.created_at}")
        print(f"Дата последнего изменения: {note.updated_at}")
        print()


def new_note():
    title = input("Введите заголовок заметки: ")
    body = input("Введите тело заметки: ")
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    updated_at = created_at
    note = Note(int(len(Note.load_all()) + 1), title, body, created_at, updated_at)
    note.save()
    print("Заметка успешно создана!")


def edit_note():
    id = int(input("Введите идентификатор заметки для редактирования: "))
    notes = Note.load_all()
    for note in notes:
        if note.id == id:
            title = input("Введите новый заголовок заметки: ")
            body = input("Введите новое тело заметки: ")
            note.update(title, body)
            print("Заметка успешно отредактирована!")
            break
    else:
        print("Заметка с таким идентификатором не найдена.")


def del_note():
    id = int(input("Введите идентификатор заметки для удаления: "))
    notes = Note.load_all()
    for note in notes:
        if note.id == id:
            note.delete()
            print("Заметка успешно удалена!")
            break
    else:
        print("Заметка с таким идентификатором не найдена.")
