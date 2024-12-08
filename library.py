from typing import Dict, List
from mini_library_app.storage import Storage


class Book:
    """
    Класс, представляющий книгу в библиотеке.

    Атрибуты:
        id (int): Уникальный идентификатор книги.
        title (str): Название книги.
        author (str): Автор книги.
        year (int): Год издания книги.
        status (str): Текущий статус книги ('в наличии', 'выдана').
    """
    id_counter: int = 1

    def __init__(self, title: str, author: str, year: int):
        self.id: int = Book.id_counter
        Book.id_counter += 1
        self.title: str = title
        self.author: str = author
        self.year: int = year
        self.status: str = "в наличии"

    def __str__(self) -> str:
        return f"ID: {self.id} | Название: {self.title} | Автор: {self.author} | Год: {self.year} | Статус: {self.status}"

    def to_dict(self) -> Dict[str, int | str]:
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status,
        }

    @staticmethod
    def from_dict(data: Dict[str, str | int]) -> "Book":
        book = Book(data["title"], data["author"], data["year"])
        book.id = data["id"]
        book.status = data["status"]
        Book.id_counter = max(Book.id_counter, book.id + 1)
        return book


class Library:
    """Класс управления библиотекой.

    Позволяет добавлять, удалять, искать, отображать книги и изменять их статус.
    """

    def __init__(self, file_manager: Storage) -> None:
        """Инициализация библиотеки с файловым менеджером."""
        self.file_manager: Storage = file_manager
        self.books: List[Book] = self.load_books()

    def load_books(self) -> List[Book]:
        """Загружает список книг из хранилища."""
        data = self.file_manager.load_data()
        return [Book.from_dict(book) for book in data]

    def save_books(self) -> None:
        """Сохраняет список книг в хранилище."""
        data = [book.to_dict() for book in self.books]
        self.file_manager.save_data(data)

    def add_book(self, title: str, author: str, year: int) -> None:
        """Добавляет книгу в библиотеку."""
        new_book = Book(title, author, year)
        self.books.append(new_book)
        self.save_books()

    def remove_book(self, book_id: int) -> bool:
        """Удаляет книгу по ID.

        Возвращает:
            bool: True, если книга удалена, иначе False.
        """
        for book in self.books:
            if book.id == book_id:
                self.books.remove(book)
                self.save_books()
                return True
        return False

    def search_books(self, **kwargs) -> List[Book]:
        """Ищет книги по заданным полям и значениям.

        Параметры:
            kwargs (dict): Поля и значения для поиска.

        Возвращает:
            List[Book]: Список найденных книг.
        """
        results = self.books[:]

        for key, value in kwargs.items():
            if isinstance(getattr(results[0], key),
                          int):
                results = [book for book in results if
                           getattr(book, key) == int(value)]
            else:
                results = [book for book in results
                           if value.lower() in getattr(book, key).lower()]
        return results

    def display_books(self) -> List[Book]:
        """Возвращает список всех книг."""
        return self.books

    def update_status(self, book_id: int, new_status: str) -> bool:
        """Обновляет статус книги по ID.

        Возвращает:
            bool: True, если статус обновлен, иначе False.
        """
        for book in self.books:
            if book.id == book_id:
                book.status = new_status
                self.save_books()
                return True
            else:
                print("Неверный статус, попробуйте снова.")
                return False
