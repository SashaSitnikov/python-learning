from models import Book, BookNotFoundError, BookAlreadyBorrowedError
from library import Library

def main():
    lib = Library()

    book1 = Book("Капитанская дочка", "Пушкин", 1836)
    book2 = Book("Руслан и Людмила", "Пушкин", 1820)
    book3 = Book("Преступление и наказание", "Достоевский", 1866)
    
    lib.add_book(book1)
    lib.add_book(book2)
    lib.add_book(book3)
    
    print("--- Демонстрация работы библиотеки ---")
    print("\nИщем книги Пушкина:")
    pushkin_books = lib.find_by_author("Пушкин")
    for b in pushkin_books:
        print(b)

    print("\n--- Пробуем взять книгу 'Капитанская дочка' ---")
    try:
        lib.borrow("Капитанская дочка")
    except (BookNotFoundError, BookAlreadyBorrowedError) as e:
        print(f"Ошибка: {e}")

    print("\n--- Пробуем взять её же второй раз ---")
    try:
        lib.borrow("Капитанская дочка")
    except (BookNotFoundError, BookAlreadyBorrowedError) as e:
        print(f"Поймали исключение: {e}")

    print("\n--- Пробуем взять несуществующую книгу ---")
    try:
        lib.borrow("Гарри Поттер")
    except (BookNotFoundError, BookAlreadyBorrowedError) as e:
        print(f"Поймали исключение: {e}")

    print("\n--- Возвращаем книгу обратно ---")
    try:
        lib.return_book("Капитанская дочка")
    except BookNotFoundError as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nВыход из программы.")
