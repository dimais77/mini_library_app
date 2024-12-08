import unittest
from unittest.mock import MagicMock
from mini_library_app.library import Library, Book


class TestLibrary(unittest.TestCase):
    """Тесты для класса Library"""

    def setUp(self):
        """Инициализация тестов: создание mock-объекта для хранилища и экземпляра библиотеки."""
        self.mock_storage = MagicMock()
        self.mock_storage.load_data.return_value = []
        self.library = Library(self.mock_storage)

    def test_add_book(self):
        """Тест добавления книги в библиотеку."""
        self.library.add_book("Title1", "Author1", 2020)
        self.assertEqual(len(self.library.books), 1)
        self.assertEqual(self.library.books[0].title, "Title1")
        self.assertEqual(self.library.books[0].author, "Author1")
        self.assertEqual(self.library.books[0].year, 2020)
        self.assertEqual(self.library.books[0].status, "в наличии")
        self.mock_storage.save_data.assert_called_once()

    def test_remove_book(self):
        """Тест удаления книги из библиотеки."""
        self.library.add_book("Title1", "Author1", 2020)
        book_id = self.library.books[0].id
        self.assertTrue(self.library.remove_book(book_id))
        self.assertEqual(len(self.library.books), 0)
        self.mock_storage.save_data.assert_called()

    def test_remove_nonexistent_book(self):
        """Тест удаления несуществующей книги."""
        self.assertFalse(self.library.remove_book(999))

    def test_search_books_by_title(self):
        """Тест поиска книг по названию."""
        self.library.add_book("Python Programming", "Author1", 2020)
        self.library.add_book("Learn Python", "Author2", 2021)
        results = self.library.search_books(title="Python")
        self.assertEqual(len(results), 2)

    def test_search_books_by_author(self):
        """Тест поиска книг по автору."""
        self.library.add_book("Book1", "Author1", 2020)
        self.library.add_book("Book2", "Author2", 2021)
        results = self.library.search_books(author="Author2")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].author, "Author2")

    def test_update_status(self):
        """Тест обновления статуса книги."""
        self.library.add_book("Title1", "Author1", 2020)
        book_id = self.library.books[0].id
        self.assertTrue(self.library.update_status(book_id, "выдана"))
        self.assertEqual(self.library.books[0].status, "выдана")
        self.mock_storage.save_data.assert_called()

    def test_update_status_invalid_id(self):
        """Тест обновления статуса для несуществующей книги."""
        self.assertFalse(self.library.update_status(999, "выдана"))

    def test_load_books_from_storage(self):
        """Тест загрузки книг из хранилища."""
        book_data = [
            {
                "id": 1,
                "title": "Title1",
                "author": "Author1",
                "year": 2020,
                "status": "в наличии",
            }
        ]
        self.mock_storage.load_data.return_value = book_data
        library = Library(self.mock_storage)
        self.assertEqual(len(library.books), 1)
        self.assertEqual(library.books[0].title, "Title1")

    def test_save_books_to_storage(self):
        """Тест сохранения книг в хранилище."""
        self.library.add_book("Title1", "Author1", 2020)
        self.library.save_books()
        self.mock_storage.save_data.assert_called()


class TestBook(unittest.TestCase):
    """Тесты для класса Book."""

    def test_book_initialization(self):
        """Тест инициализации экземпляра книги."""
        book = Book("Title1", "Author1", 2020)
        self.assertEqual(book.title, "Title1")
        self.assertEqual(book.author, "Author1")
        self.assertEqual(book.year, 2020)
        self.assertEqual(book.status, "в наличии")

    def test_book_to_dict(self):
        """Тест преобразования книги в словарь."""
        book = Book("Title1", "Author1", 2020)
        expected_dict = {
            "id": book.id,
            "title": "Title1",
            "author": "Author1",
            "year": 2020,
            "status": "в наличии",
        }
        self.assertEqual(book.to_dict(), expected_dict)

    def test_book_from_dict(self):
        """Тест создания книги из словаря."""
        data = {
            "id": 1,
            "title": "Title1",
            "author": "Author1",
            "year": 2020,
            "status": "в наличии",
        }
        book = Book.from_dict(data)
        self.assertEqual(book.id, 1)
        self.assertEqual(book.title, "Title1")
        self.assertEqual(book.author, "Author1")
        self.assertEqual(book.year, 2020)
        self.assertEqual(book.status, "в наличии")


if __name__ == "__main__":
    unittest.main()
