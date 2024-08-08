class Author:
    def __init__(self, name, biography):
        self.__name = name
        self.__biography = biography

    def get_name(self):
        return self.__name

    def display_info(self):
        print(f"Name: {self.__name}")
        print(f"Biography: {self.__biography}")

