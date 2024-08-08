import datetime
from book import Book
from user import User
from author import Author
from reservation import Reservation
from file_handler import FileHandler

class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.authors = []
        self.reservations = []
        self.file_handler = FileHandler()
        self.load_data()

    def load_data(self):
        self.books = self.file_handler.load_books()
        self.users = self.file_handler.load_users()
        self.authors = self.file_handler.load_authors()
        self.reservations = self.file_handler.load_reservations()

    def save_data(self):
        self.file_handler.save_books(self.books)
        self.file_handler.save_users(self.users)
        self.file_handler.save_authors(self.authors)
        self.file_handler.save_reservations(self.reservations)

    def main_menu(self):
        while True:
            print("\nWelcome to the Library Management System!")
            print("Main Menu:")
            print("1. Book Operations")
            print("2. User Operations")
            print("3. Author Operations")
            print("4. Quit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.book_operations()
            elif choice == '2':
                self.user_operations()
            elif choice == '3':
                self.author_operations()
            elif choice == '4':
                print("Exiting the Library Management System.")
                self.save_data()
                break
            else:
                print("Invalid choice. Please try again.")

    def book_operations(self):
        while True:
            print("\nBook Operations:")
            print("1. Add a new book")
            print("2. Borrow a book")
            print("3. Return a book")
            print("4. Search for a book")
            print("5. Display all books")
            print("6. Back to Main Menu")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_book()
            elif choice == '2':
                self.borrow_book()
            elif choice == '3':
                self.return_book()
            elif choice == '4':
                self.search_book()
            elif choice == '5':
                self.display_all_books()
            elif choice == '6':
                break
            else:
                print("Invalid choice. Please try again.")

    def user_operations(self):
        while True:
            print("\nUser Operations:")
            print("1. Add a new user")
            print("2. View user details")
            print("3. Display all users")
            print("4. Back to Main Menu")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_user()
            elif choice == '2':
                self.view_user_details()
            elif choice == '3':
                self.display_all_users()
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")

    def author_operations(self):
        while True:
            print("\nAuthor Operations:")
            print("1. Add a new author")
            print("2. View author details")
            print("3. Display all authors")
            print("4. Back to Main Menu")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_author()
            elif choice == '2':
                self.view_author_details()
            elif choice == '3':
                self.display_all_authors()
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        genre = input("Enter book genre: ")
        publication_date = input("Enter book publication date: ")
        new_book = Book(title, author, genre, publication_date)
        self.books.append(new_book)
        print("Book added successfully.")

    def borrow_book(self):
        title = input("Enter the title of the book to borrow: ")
        for book in self.books:
            if book.get_title() == title and book.is_available():
                book.set_availability(False)
                due_date = datetime.date.today() + datetime.timedelta(days=14)
                user_id = input("Enter your user ID: ")
                user = self.find_user(user_id)
                if user:
                    user.borrow_book(title, due_date)
                    print(f"You have borrowed '{title}'. Due date is {due_date}.")
                return
        print("Book not found or already borrowed.")
        reserve = input("Would you like to reserve this book? (y/n): ")
        if reserve.lower() == 'y':
            user_id = input("Enter your user ID: ")
            user = self.find_user(user_id)
            if user:
                self.reservations.append(Reservation(user_id, title))
                print(f"You have reserved '{title}'.")

    def return_book(self):
        title = input("Enter the title of the book to return: ")
        for book in self.books:
            if book.get_title() == title and not book.is_available():
                book.set_availability(True)
                user_id = input("Enter your user ID: ")
                user = self.find_user(user_id)
                if user:
                    user.return_book(title)
                    print(f"You have returned '{title}'.")
                    self.check_reservations(title)
                return
        print("Book not found or not borrowed.")

    def search_book(self):
        title = input("Enter the title of the book to search: ")
        for book in self.books:
            if book.get_title() == title:
                book.display_info()
                return
        print("Book not found.")

    def display_all_books(self):
        if not self.books:
            print("No books available.")
        for book in self.books:
            book.display_info()

    def add_user(self):
        name = input("Enter user name: ")
        library_id = input("Enter user library ID: ")
        new_user = User(name, library_id)
        self.users.append(new_user)
        print("User added successfully.")

    def view_user_details(self):
        library_id = input("Enter user library ID: ")
        for user in self.users:
            if user.get_library_id() == library_id:
                user.display_info()
                return
        print("User not found.")

    def display_all_users(self):
        if not self.users:
            print("No users available.")
        for user in self.users:
            user.display_info()

    def add_author(self):
        name = input("Enter author name: ")
        biography = input("Enter author biography: ")
        new_author = Author(name, biography)
        self.authors.append(new_author)
        print("Author added successfully.")

    def view_author_details(self):
        name = input("Enter author name: ")
        for author in self.authors:
            if author.get_name() == name:
                author.display_info()
                return
        print("Author not found.")

    def display_all_authors(self):
        if not self.authors:
            print("No authors available.")
        for author in self.authors:
            author.display_info()

    def find_user(self, library_id):
        for user in self.users:
            if user.get_library_id() == library_id:
                return user
        print("User not found.")
        return None

    def check_reservations(self, title):
        for reservation in self.reservations:
            if reservation.get_book_title() == title:
                user = self.find_user(reservation.get_user_id())
                if user:
                    print(f"Notification: '{title}' is now available for {user.get_name()}.")
                self.reservations.remove(reservation)
                return

if __name__ == "__main__":
    library = Library()
    library.main_menu()
