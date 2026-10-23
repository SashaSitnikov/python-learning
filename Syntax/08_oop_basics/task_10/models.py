class BookNotFoundError(Exception):
    pass
    
class BookAlreadyBorrowedError(Exception): 
    pass
    
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.is_available = True
        
    def __str__(self):
        status = "Доступна" if self.is_available else "Выдана"
        return f"'{self.title}' — {self.author} ({self.year}) [{status}]"