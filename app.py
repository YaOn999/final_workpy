from datetime import datetime
from note import Note


def app():
    while True:
        print("1. Просмотреть все заметки")
        print("2. Создать новую заметку")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выйти")

        choice = input("Выберите действие: ")
        if choice == "1":
            notes = Note.load_all()
            for note in notes:
                print(f"Заметка #{note.id}")
                print(f"Заголовок: {note.title}")
                print(f"Тело: {note.body}")
                print(f"Дата создания: {note.created_at}")
                print(f"Дата последнего изменения: {note.updated_at}")
                print()
        elif choice == "2":
            title = input("Введите заголовок заметки: ")
            body = input("Введите тело заметки: ")
            created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            updated_at = created_at
            note = Note(int(len(Note.load_all()) + 1), title, body, created_at, updated_at)
            note.save()
            print("Заметка успешно создана!")
        elif choice == "3":
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
        elif choice == "4":
            id = int(input("Введите идентификатор заметки для удаления: "))
            notes = Note.load_all()
            for note in notes:
                if note.id == id:
                    note.delete()
                    print("Заметка успешно удалена!")
                    break
            else:
                print("Заметка с таким идентификатором не найдена.")

        elif choice == "5":
            break
        else:
            print("Неверный выбор. Попробуйте еще раз.")
