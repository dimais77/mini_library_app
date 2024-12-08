import unittest
import os
import json
from ..storage import Storage


class TestStorage(unittest.TestCase):
    """Тесты для класса Storage."""

    TEST_FILE = "test_data.json"

    def setUp(self) -> None:
        """Создает тестовый файл перед каждым тестом."""
        self.storage = Storage(self.TEST_FILE)

    def tearDown(self) -> None:
        """Удаляет тестовый файл после каждого теста."""
        if os.path.exists(self.TEST_FILE):
            os.remove(self.TEST_FILE)

    def test_load_data_file_not_found(self):
        """Тестирует случай, когда файл не существует."""
        data = self.storage.load_data()
        self.assertEqual(data, [], "Должен возвращаться пустой список, если файл не существует")

    def test_load_data_invalid_json(self):
        """Тестирует случай, когда файл содержит некорректный JSON."""
        with open(self.TEST_FILE, "w", encoding="utf-8") as file:
            file.write("{invalid_json}")
        data = self.storage.load_data()
        self.assertEqual(data, [], "Должен возвращаться пустой список при ошибке JSONDecodeError")

    def test_load_data_success(self):
        """Тестирует успешную загрузку данных из файла."""
        test_data = [{"id": 1, "title": "Test Book"}]
        with open(self.TEST_FILE, "w", encoding="utf-8") as file:
            json.dump(test_data, file)
        data = self.storage.load_data()
        self.assertEqual(data, test_data, "Данные должны корректно загружаться из файла")

    def test_save_data_success(self):
        """Тестирует успешное сохранение данных в файл."""
        test_data = [{"id": 1, "title": "Test Book"}]
        self.storage.save_data(test_data)
        with open(self.TEST_FILE, "r", encoding="utf-8") as file:
            loaded_data = json.load(file)
        self.assertEqual(loaded_data, test_data, "Данные должны корректно сохраняться в файл")

    def test_save_data_creates_file(self):
        """Тестирует создание файла при сохранении данных."""
        test_data = [{"id": 1, "title": "Test Book"}]
        self.storage.save_data(test_data)
        self.assertTrue(os.path.exists(self.TEST_FILE), "Файл должен быть создан при сохранении данных")


if __name__ == "__main__":
    unittest.main()
