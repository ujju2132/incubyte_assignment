import unittest
from library import Library

class TestLibraryManagementSystem(unittest.TestCase):
    def setUp(self):
        self.library = Library()

    def test_add_book(self):
        self.library.add_book("123", "Book Title", "Author Name", 2023)
        self.assertIn("123", self.library.books)