class Book:
    def __init__(self, author, title):
        self.author = author
        self.title = title

    def __str__(self):
        return f'{self.author}, {self.title}'

    def __eq__(self, other):
        if self.author == other.author and self.title == other.title:
            return True
        else:
            return False

        from book import Book

        class BookCase:
            def __init__(self):
                self.books = []

            def add_books(self, book):
                self.books.append(book)