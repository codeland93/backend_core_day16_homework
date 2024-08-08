class Book:
    def __init__(self, title, author, genre, publication_date):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__publication_date = publication_date
        self.__is_available = True

    def get_title(self):
        return self.__title

    def is_available(self):
        return self.__is_available

    def set_availability(self, status):
        self.__is_available = status

    def display_info(self):
        availability = "Available" if self.__is_available else "Borrowed"
        print(f"Title: {self.__title}")
        print(f"Author: {self.__author}")
        print(f"Genre: {self.__genre}")
        print(f"Publication Date: {self.__publication_date}")
        print(f"Status: {availability}")

