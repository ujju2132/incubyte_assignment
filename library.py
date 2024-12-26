class Book:
    def __init__(self, isbn, title, author, publication_year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.is_available = True
    
    def __repr__(self):
        return f"Book({self.isbn}, {self.title}, {self.author}, {self.publication_year}, Available: {self.is_available})"