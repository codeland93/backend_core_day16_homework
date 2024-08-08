class Reservation:
    def __init__(self, user_id, book_title):
        self.__user_id = user_id
        self.__book_title = book_title

    def get_user_id(self):
        return self.__user_id

    def get_book_title(self):
        return self.__book_title
    
