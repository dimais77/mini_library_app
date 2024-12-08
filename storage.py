import json
from typing import List, Dict


class Storage:
    """Класс для управления хранилищем данных библиотеки."""

    def __init__(self, file_path: str) -> None:
        """Инициализация хранилища с указанным файлом.

        Параметры:
            file_path (str): Путь к файлу данных.
        """
        self.file_path: str = file_path

    def load_data(self) -> List[Dict]:
        """Загружает данные из файла.

        Возвращает:
            List[Dict]: Список записей из файла.
        """
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_data(self, data: List[Dict]) -> None:
        """Сохраняет данные в файл.

        Параметры:
            data (List[Dict]): Список записей для сохранения.
        """
        with open(self.file_path, "w",
                  encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
