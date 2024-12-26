import unittest
from library import Library

class TestLibraryManagementSystem(unittest.TestCase):
    def setUp(self):
        self.library = Library()

    def test_add_book(self):
        self.library.add_book("123", "Book Title", "Author Name", 2023)
        self.assertIn("123", self.library.books)

    def test_add_book_duplicate_isbn(self):
        self.library.add_book("123", "Book Title", "Author Name", 2023)
        with self.assertRaises(ValueError):
            self.library.add_book("123", "Another Title", "Another Author", 2024)

    def test_borrow_book(self):
        self.library.add_book("123", "Book Title", "Author Name", 2023)
        self.library.borrow_book("123")
        self.assertFalse(self.library.books["123"].is_available)

    def test_borrow_nonexistent_book(self):
        with self.assertRaises(ValueError):
            self.library.borrow_book("999")

    def test_borrow_already_borrowed_book(self):
        self.library.add_book("123", "Book Title", "Author Name", 2023)
        self.library.borrow_book("123")
        with self.assertRaises(ValueError):
            self.library.borrow_book("123")

    def test_return_book(self):
        self.library.add_book("123", "Book Title", "Author Name", 2023)
        self.library.borrow_book("123")
        self.library.return_book("123")
        self.assertTrue(self.library.books["123"].is_available)

    def test_return_nonexistent_book(self):
        with self.assertRaises(ValueError):
            self.library.return_book("999")

    def test_return_unborrowed_book(self):
        self.library.add_book("123", "Book Title", "Author Name", 2023)
        with self.assertRaises(ValueError):
            self.library.return_book("123")

if __name__ == "__main__":
    unittest.main()