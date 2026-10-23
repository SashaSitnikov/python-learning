from models import Book, BookNotFoundError, BookAlreadyBorrowedError

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        
    def find_by_author(self, author):
        return [b for b in self.books if b.author.lower() == author.lower()]

    
    def borrow(self, title):
        for book in self.books:
            if title.lower() == book.title.lower():
                if not book.is_available:
                    raise BookAlreadyBorrowedError(f"Книга: {title} уже выдана другому человеку!")
                book.is_available = False
                print(f"Книга: {title} успешно выдана!")
                return None
        else:
            raise BookNotFoundError(f"Книга: {title} не найдена!")
    
    def return_book(self, title):
        for book in self.books:
            if title.lower() == book.title.lower():
                if book.is_available:
                    raise BookAlreadyBorrowedError(f"Книга: {title} уже находится в библиотеке!")
                book.is_available = True
                print(f"Книга: {title} успешно возвращена в библиотеку!")
                return None
        else:
            raise BookNotFoundError(f"Книга: {title} не найдена!")