**Library Management System**

**Overview:**
The Library Management System is a command-line application designed to manage books, users, and authors within a library. Built using Object-Oriented Programming (OOP) principles in Python, this system supports various functionalities, including adding books, users, and authors, borrowing and returning books, and more. This system also includes advanced features like reservation handling and fine calculation for overdue books.

**Features:**
- Book Operations: Add, borrow, return, search, and display books.
- User Operations: Add, view details, and display all users.
- Author Operations: Add, view details, and display all authors.
- Reservation System: Reserve books and notify users when books become available.
- Fine Calculation: Calculate fines for overdue books and update user accounts.

*Navigate through the application using the following options:*

**Book Operations:**

- Add a new book
- Borrow a book
- Return a book
- Search for a book
- Display all books

**User Operations:**

- Add a new user
- View user details
- Display all users

**Author Operations:**

- Add a new author
- View author details
- Display all authors
- Quit: Exit the application

**Data Persistence**

The system handles data through text files for books, users, and authors. Ensure that the data directory contains the following files:

books.txt
users.txt
authors.txt
Data will be automatically loaded from and saved to these files.

**Code Structure:**

library.py: The entry point of the application, handling user interaction and menu navigation.

book.py: Contains the all Book information and options.

user.py: Contains the all User information and options.

author.py: Contains the all author information and options. 

reservation.py: Contains the all reservation information and options.

file_handler.py: Contains the file list and options for handling files and adding files from the program options. 

Including fine calculations for overdue books. Assigning due dates to borrowed books, and calculate fines for users who exceed the due date. 

Optional Features:
Text File Handling: Data is saved to and loaded from text files for books, users, and authors.
Reservation System: Allows users to reserve unavailable books and notifies them when books are available.
Fine Calculation: Calculates and manages fines for overdue books.