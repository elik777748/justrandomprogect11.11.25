import pytest

from library import Book, Library

@pytest.fixture
def library_with_books():
    lib = Library("Тестова бібліотека")
    lib.add_book(Book("Автор 1", "Книга 1", "001"))
    lib.add_book(Book("Автор 2", "Книга 2", "002"))
    return lib

def test_book_str():
    book = Book("Автор", "Назва", "123")
    assert str(book) == "ID: 123, Автор: Автор, Назва: Назва"

def test_add_book_valid(library_with_books):
    initial_count = len(library_with_books.books)
    new_book = Book("Автор 3", "Книга 3", "003")
    library_with_books.add_book(new_book)
    assert len(library_with_books.books) == initial_count + 1
    assert library_with_books.books[-1].title == "Книга 3"

def test_add_book_invalid(library_with_books):
    with pytest.raises(ValueError):
        library_with_books.add_book("не книга")

def test_remove_existing_book(library_with_books, capsys):
    library_with_books.remove_book("001")
    captured = capsys.readouterr()
    assert "видалена" in captured.out
    assert all(book.book_id != "001" for book in library_with_books.books)

def test_remove_nonexistent_book(library_with_books, capsys):
    library_with_books.remove_book("999")
    captured = capsys.readouterr()
    assert "не знайдена" in captured.out

def test_display_books_output(library_with_books, capsys):
    library_with_books.display_books()
    captured = capsys.readouterr()
    assert "Книги в бібліотеці" in captured.out
    assert "Книга 1" in captured.out
    assert "Книга 2" in captured.out

def test_display_books_empty(capsys):
    empty_lib = Library("Порожня")
    empty_lib.display_books()
    captured = capsys.readouterr()
    assert "Бібліотека порожня" in captured.out