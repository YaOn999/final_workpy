import json
from datetime import datetime


class Note:
    def __init__(self, id, title, body, created_at, updated_at):
        self.id = id
        self.title = title
        self.body = body
        self.created_at = created_at
        self.updated_at = updated_at

    def save(self):
        # Сохранение заметки в файл в формате json
        data = {
            "id": self.id,
            "title": self.title,
            "body": self.body,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
        with open("notes.json", "a") as file:
            json.dump(data, file)
            file.write("\n")

    @staticmethod
    def load_all():
        # Загрузка всех заметок из файла
        notes = []
        with open("notes.json", "r") as file:
            for line in file:
                data = json.loads(line)
                note = Note(
                    data["id"],
                    data["title"],
                    data["body"],
                    data["created_at"],
                    data["updated_at"]
                )
                notes.append(note)
        return notes


    def update(self, title, body):
        # Обновление заголовка и тела заметки
        self.delete()
        self.title = title
        self.body = body
        self.updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.save()

    def delete(self):
        # Удаление заметки из файла
        with open("notes.json", "r") as file:
            lines = file.readlines()
        with open("notes.json", "w") as file:
            for line in lines:
                data = json.loads(line)
                if data["id"] != self.id:
                    json.dump(data, file)
                    file.write("\n")
