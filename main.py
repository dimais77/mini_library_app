import json
from mini_library_app.library import Library
from mini_library_app.storage import Storage


def load_config(config_file: str) -> dict:
    """
    Загружает конфигурационный файл в формате JSON.
    Args:
        config_file (str): Путь к конфигурационному файлу.
    Returns:
        Dict: Словарь с параметрами конфигурации.
        """
    with open(config_file, encoding='utf-8') as file:
        return json.load(file)


def main():
    """
    Основная функция для запуска приложения управления библиотекой.
    """
    CONFIG_FILE: str = "config.json"
    config: dict = load_config(CONFIG_FILE)
    STATUSES: dict[str, str] = config["book_statuses"]
    file_manager = Storage(config["data_file"])
    library = Library(file_manager)

    while True:
        print("\n--- Меню ---")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Поиск книг")
        print("4. Изменить статус книги")
        print("5. Показать все книги")
        print("6. Выход")
        choice: str = input("Введите номер операции: ")

        if choice == "1":
            title: str = input("Введите название книги: ")
            author: str = input("Введите автора книги: ")
            year: int = int(input("Введите год издания: "))
            library.add_book(title, author, year)
            print("Книга успешно добавлена!")

        elif choice == "2":
            book_id: int = int(input("Введите ID книги для удаления: "))
            if library.remove_book(book_id):
                print("Книга успешно удалена!")
            else:
                print("Книга с таким ID не найдена.")

        elif choice == "3":
            search_fields: List[str] = config["search_fields"]

            print("\nВыберите поле для поиска:")
            for i, field in enumerate(search_fields, start=1):
                print(f"{i} - {field.capitalize()}")

            try:
                field_choice: int = int(input("Введите номер поля: "))
                if 1 <= field_choice <= len(search_fields):
                    field: str = search_fields[field_choice - 1]
                    query: str = input(
                        f"Введите значение для поиска по '{field.capitalize()}': ").strip()
                    kwargs: Dict[str, str] = {field: query}
                    results: List[Book] = library.search_books(**kwargs)
                    if results:
                        print("\nРезультаты поиска:")
                        for book in results:
                            print(book)
                    else:
                        print("Книги не найдены.")
                else:
                    print("Неверный выбор поля, попробуйте снова.")
            except ValueError:
                print("Введите корректный номер поля.")

        elif choice == "4":
            try:
                book_id: int = int(input("Введите ID книги: "))
            except ValueError:
                print("ID книги должен быть числом.")
                continue

            print("\nВыберите новый статус:")
            for i, status in enumerate(STATUSES.values(), start=1):
                print(f"{i} - {status}")

            try:
                status_choice: int = int(input("Введите номер статуса: "))
                if 1 <= status_choice <= len(STATUSES):
                    new_status: str = list(STATUSES.values())[
                        status_choice - 1]
                    if library.update_status(book_id, new_status):
                        print("Статус книги успешно обновлён!")
                    else:
                        print("Не удалось обновить статус книги.")
                else:
                    print("Неверный выбор статуса, попробуйте снова.")
            except ValueError:
                print("Введите корректный номер статуса.")

        elif choice == "5":
            books: List[Book] = library.display_books()
            if books:
                for book in books:
                    print(book)
            else:
                print("Библиотека пуста.")

        elif choice == "6":
            print("Выход из программы.")
            break

        else:
            print("Неверный ввод, попробуйте снова.")


if __name__ == "__main__":
    main()
