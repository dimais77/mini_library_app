class Book:
    """Класс Книга. Каждая книга должна содержать следующие поля:
 • id (уникальный идентификатор, генерируется автоматически)
 • title (название книги)
 • author (автор книги)
 • year (год издания)
 • status (статус книги: “в наличии”, “выдана”)
"""
    def __init__(self, book_id, title, author, year, status):
        self.id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = status


class Library:
    """Класс управления Библиотекой книг.
    Приложение должно позволять добавлять, удалять, искать и отображать книги.
    """
    def __init__(self):
        pass

    def add_book(self):
        pass

    def delete_book(self):
        pass

    def search_books(self):
        pass

    def display_books(self):
        pass






