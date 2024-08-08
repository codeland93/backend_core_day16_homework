import datetime

class User:
    def __init__(self, name, library_id):
        self.__name = name
        self.__library_id = library_id
        self.__borrowed_books = []

    def get_library_id(self):
        return self.__library_id

    def get_name(self):
        return self.__name

    def borrow_book(self, book_title, due_date):
        self.__borrowed_books.append({"title": book_title, "due_date": due_date})

    def return_book(self, book_title):
        for book in self.__borrowed_books:
            if book["title"] == book_title:
                self.__borrowed_books.remove(book)
                return

    def display_info(self):
        print(f"Name: {self.__name}")
        print(f"Library ID: {self.__library_id}")
        print("Borrowed Books:")
        for book in self.__borrowed_books:
            due_date = book["due_date"]
            fine = self.calculate_fine(due_date)
            print(f"  - {book['title']} (Due Date: {due_date}, Fine: {fine})")

    def calculate_fine(self, due_date):
        today = datetime.date.today()
        if today > due_date:
            delta = today - due_date
            return delta.days * 0.5  # $0.5 per day overdue
        return 0.0

