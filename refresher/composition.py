class Book_shelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"Bookshelf with {len(self.books)} books"


class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):  
        return f"Book {self.name}"


book = ("Game of Thrones")
book1 = ("Python 101")
shelf = Book_shelf(book, book1)

print(shelf)