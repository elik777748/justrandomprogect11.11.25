class Book:
    def __init__(self, author, title, book_id):
        self.author = author
        self.title = title
        self.book_id = book_id

    def __str__(self):
        return f"ID: {self.book_id}, Автор: {self.author}, Назва: {self.title}"

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
            print(f"Книга {book.title} додана до бібліотеки {self.name}\n")
        else:
            raise ValueError("Ви додаете не книгу")

    def remove_book(self, book_id):
        initial_count = len(self.books)
        self.books = [book for book in self.books if book.book_id != book_id]
        
        if len(self.books) < initial_count:
            print(f"Книга з ID {book_id} видалена з бібліотеки {self.name}")
        else:
            print(f"Книга з ID {book_id} не знайдена у бібліотеці {self.name}")

    def display_books(self):
        print(f"Книги в бібліотеці {self.name}")
        if not self.books:
            print("Бібліотека порожня")
        else:
            for book in self.books:
                print(book)
        print("\n")


my_library = Library("e7")

my_library.add_book(Book("Іван Франко", "Захар Беркут", "001"))
my_library.add_book(Book("Леся Українка", "Лісова пісня", "002"))
my_library.add_book(Book("Тарас Шевченко", "Кобзар", "003"))

my_library.display_books()

my_library.remove_book("002")

my_library.display_books()

my_library.remove_book("999")

my_library.add_book(Book("Стівен Кінг", "Воно", "004"))

my_library.display_books()
