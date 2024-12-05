import os
import json
from typing import Dict, List, Optional

STATUS_AVAILABLE = "в наличии"
STATUS_BORROWED = "выдана"
DATA_FILE = "library.json"

class Book:
    """Класс Книга. Каждая книга должна содержать следующие поля:
 • id (уникальный идентификатор, генерируется автоматически)
 • title (название книги)
 • author (автор книги)
 • year (год издания)
 • status (статус книги: “в наличии”, “выдана”)
"""

    def __init__(self, book_id: int, title: str, author: str, year: int,
                 status: str = STATUS_AVAILABLE):
        self.id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def __str__(self) -> str:
        return f"ID: {self.id} | Название: {self.title} | Автор: {self.author} | Год: {self.year} | Статус: {self.status}"

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status,
        }

    @staticmethod
    def from_dict(data: Dict[str, str | int]) -> "Book":
        return Book(
            book_id=data["id"],
            title=data["title"],
            author=data["author"],
            year=data["year"],
            status=data["status"]
        )


class Library:
    """Класс управления Библиотекой книг.
    Приложение должно позволять добавлять, удалять, искать и отображать книги.
    """

    def __init__(self, data_file: str = DATA_FILE):
        self.data_file = data_file
        self.books: List[Book] = self.load_books()

    def load_books(self) -> List[Book]:
        if not os.path.exists(self.data_file):
            return []
        with open(self.data_file, "r", encoding="utf-8") as file:
            data = json.load(file)
        return [Book.from_dict(book) for book in data]

    def save_books(self) -> None:
        with open(self.data_file, "w", encoding="utf-8") as file:
            json.dump([book.to_dict() for book in self.books], file, ensure_ascii=False, indent=4)

    def add_book(self, title: str, author: str, year: int) -> None:
        book_id = max((book.id for book in self.books), default=0) + 1
        new_book = Book(book_id, title, author, yaer)
        self.books.append(new_book)
        self.save_books()
        print("Книга успешно добавлена.")

    def delete_book(self):
        pass

    def search_books(self):
        pass

    def display_books(self):
        pass

    def update_status(self):
        pass
