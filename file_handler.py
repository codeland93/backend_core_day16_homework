import json
from book import Book
from user import User
from author import Author
from reservation import Reservation

class FileHandler:
    def __init__(self):
        self.books_file = "books.txt"
        self.users_file = "users.txt"
        self.authors_file = "authors.txt"
        self.reservations_file = "reservations.txt"

    def load_books(self):
        try:
            with open(self.books_file, "r") as file:
                books_data = json.load(file)
                return [Book(**data) for data in books_data]
        except FileNotFoundError:
            return []

    def save_books(self, books):
        with open(self.books_file, "w") as file:
            books_data = [book.__dict__ for book in books]
            json.dump(books_data, file)

    def load_users(self):
        try:
            with open(self.users_file, "r") as file:
                users_data = json.load(file)
                return [User(**data) for data in users_data]
        except FileNotFoundError:
            return []

    def save_users(self, users):
        with open(self.users_file, "w") as file:
            users_data = [user.__dict__ for user in users]
            json.dump(users_data, file)

    def load_authors(self):
        try:
            with open(self.authors_file, "r") as file:
                authors_data = json.load(file)
                return [Author(**data) for data in authors_data]
        except FileNotFoundError:
            return []

    def save_authors(self, authors):
        with open(self.authors_file, "w") as file:
            authors_data = [author.__dict__ for author in authors]
            json.dump(authors_data, file)

    def load_reservations(self):
        try:
            with open(self.reservations_file, "r") as file:
                reservations_data = json.load(file)
                return [Reservation(**data) for data in reservations_data]
        except FileNotFoundError:
            return []

    def save_reservations(self, reservations):
        with open(self.reservations_file, "w") as file:
            reservations_data = [reservation.__dict__ for reservation in reservations]
            json.dump(reservations_data, file)
