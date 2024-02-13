class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book  {self.name}, {self.book_type}, weighing {self.weight}gr>"

    # create new object inside a class
    # because it's class method, we don't need to crete object first
    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight)


book = Book.hardcover("Harry Potter", 1500)
book_paperback = Book.paperback("Game of Thrones", 1700)

print(book)
