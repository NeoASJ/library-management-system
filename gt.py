from datetime import datetime, timedelta

class Library:
    lib = {}

    def add_user(self, name, phone_no, user_id):
        self.name = name
        self.phone_no = phone_no
        self.user_id = user_id
        Library.lib[self.user_id] = {"name": self.name, "phone_no": self.phone_no, "Borrowed Books": []}

    @staticmethod
    def remove_user(user_id):
        if user_id in Library.lib:
            del Library.lib[user_id]
        else:
            print("No record matched. Enter a valid user ID.")

    @staticmethod
    def update_user(name, phone_no, user_id):
        if user_id in Library.lib.keys():
            Library.lib[user_id] = {"name": name, "phone_no": phone_no}
        else:
            print("No records were created using this user ID earlier.")

    @staticmethod
    def display():
        if len(Library.lib) < 1:
            print("No user records found.")
        else:
            print("User records:")
            for user_id, details in Library.lib.items():
                print(user_id, details)


class Book(Library):
    bk = {}

    def add_book(self, isbn, title, author, year, genre):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        Book.bk[isbn] = {"title": self.title, "author": self.author, "year": self.year, "genre": self.genre, "status": 'Available'}

    @staticmethod
    def update_book(isbn, key, value):
        if isbn in Book.bk.keys():
            if key in Book.bk[isbn].keys():
                Book.bk[isbn][key] = value
                print(f"Book with ISBN {isbn} updated. {key} set to {value}.")
            else:
                print(f"Key '{key}' not found in the book details.")
        else:
            print(f"Book with ISBN {isbn} not found.")

    @staticmethod
    def view_book(isbn):
        if isbn in Book.bk.keys():
            print(Book.bk[isbn])
        else:
            print("No records found.")

    @staticmethod
    def remove(isbn):
        if isbn in Book.bk:
            del Book.bk[isbn]
        else:
            print("No records found.")

    @staticmethod
    def borrow_book(isbn, user_id, borrow_date=None):
        borrow_date = datetime.now() if borrow_date is None else borrow_date
        return_day = borrow_date + timedelta(days=14)
        d = return_day - borrow_date

        if user_id in Library.lib:
            if "Borrowed Books" not in Library.lib[user_id]:
                Library.lib[user_id]["Borrowed Books"] = []

            if isbn in Book.bk:
                if Book.bk[isbn]["status"] == 'Available':
                    Library.lib[user_id]["Borrowed Books"].append({
                        "isbn": isbn,
                        "borrow date": borrow_date,
                        "due date": return_day
                    })
                    Book.bk[isbn]["status"] = 'Borrowed'
                    print(f"The due date for the book is on {return_day.day}-{return_day.strftime('%b')}-{return_day.year}, within {d.days} days.")
                    print(f"Book with ISBN {isbn} borrowed by {user_id}.")
                else:
                    print(f"Book with ISBN {isbn} is already borrowed.")
            else:
                print("ISBN not found.")
        else:
            print("User ID not found.")

    @staticmethod
    def return_book(isbn, user_id, return_date=None):
        if return_date is None:
            return_date = datetime.now()
        if isbn in Book.bk and user_id in Library.lib:
            if Book.bk[isbn]['status'] == "Borrowed":
                Book.bk[isbn]['status'] = "Available"
                borrowed_books = Library.lib[user_id]['Borrowed Books']
                book_to_return = next((book for book in borrowed_books if book['isbn'] == isbn), None)
                if book_to_return:
                    borrowed_books.remove(book_to_return)
                    print(f"Book with ISBN {isbn} returned by User {user_id} on {return_date}.")
                else:
                    print(f"Book with ISBN {isbn} not found in User {user_id}'s borrowed books list.")
            else:
                print(f"Book with ISBN {isbn} is not currently borrowed.")
        else:
            print('User ID or ISBN not found.')
        print(f"Book is returned on {return_date}.")

    @staticmethod
    def check_status(isbn):
        if isbn in Book.bk:
            print(Book.bk[isbn]["status"])
        else:
            print(f"Book with ISBN {isbn} not found.")

    @staticmethod
    def borrow_history(user_id):
        if user_id in Library.lib:
            history = Library.lib[user_id]['Borrowed Books']
            if history:
                print(f"Borrowing history of {user_id}:")
                for book in history:
                    print(f"ISBN: {book['isbn']}, Borrow date: {book['borrow date']}, Due date: {book['due date']}")
            else:
                print("No records found.")
        else:
            print("User ID not found.")

    @staticmethod
    def view_all_books():
        if len(Book.bk) < 1:
            print("No books found.")
        else:
            print("All Books in the Library:")
            for isbn, details in Book.bk.items():
                print(f"ISBN: {isbn}, Details: {details}")

    @staticmethod
    def view_available_books():
        available_books = {isbn: details for isbn, details in Book.bk.items() if details['status'] == 'Available'}
        if len(available_books) < 1:
            print("No available books found.")
        else:
            print("Available Books:")
            for isbn, details in available_books.items():
                print(f"ISBN: {isbn}, Details: {details}")

    @staticmethod
    def view_borrowed_books():
        borrowed_books = {isbn: details for isbn, details in Book.bk.items() if details['status'] == 'Borrowed'}
        if len(borrowed_books) < 1:
            print("No borrowed books found.")
        else:
            print("Borrowed Books:")
            for isbn, details in borrowed_books.items():
                print(f"ISBN: {isbn}, Details: {details}")


def main():
    library = Library()
    book = Book()
    while True:
        print("\nLibrary Management System:")
        print("1. Add User")
        print("2. Remove User")
        print("3. Update User")
        print("4. Display Users")
        print("5. Add Book")
        print("6. Update Book")
        print("7. View Book")
        print("8. Remove Book")
        print("9. Borrow Book")
        print("10. Return Book")
        print("11. Check Book Status")
        print("12. Borrow History")
        print("13. View All Books")
        print("14. View Available Books")
        print("15. View Borrowed Books")
        print("16. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter user name: ")
            phone_no = input("Enter user phone number: ")
            user_id = input("Enter user ID: ")
            library.add_user(name, phone_no, user_id)
        elif choice == 2:
            user_id = input("Enter user ID: ")
            library.remove_user(user_id)
        elif choice == 3:
            name = input("Enter new user name: ")
            phone_no = input("Enter new user phone number: ")
            user_id = input("Enter user ID: ")
            library.update_user(name, phone_no, user_id)
        elif choice == 4:
            library.display()
        elif choice == 5:
            isbn = input("Enter book ISBN: ")
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            year = input("Enter book publication year: ")
            genre = input("Enter book genre: ")
            book.add_book(isbn, title, author, year, genre)
        elif choice == 6:
            isbn = input("Enter book ISBN: ")
            key = input("Enter detail to update (title, author, year, genre): ")
            value = input("Enter new value: ")
            book.update_book(isbn, key, value)
        elif choice == 7:
            isbn = input("Enter book ISBN: ")
            book.view_book(isbn)
        elif choice == 8:
            isbn = input("Enter book ISBN: ")
            book.remove(isbn)
        elif choice == 9:
            isbn = input("Enter book ISBN: ")
            user_id = input("Enter user ID: ")
            book.borrow_book(isbn, user_id)
        elif choice == 10:
            isbn = input("Enter book ISBN: ")
            user_id = input("Enter user ID: ")
            book.return_book(isbn, user_id)
        elif choice == 11:
            isbn = input("Enter book ISBN: ")
            book.check_status(isbn)
        elif choice == 12:
            user_id = input("Enter user ID: ")
            book.borrow_history(user_id)
        elif choice == 13:
            book.view_all_books()
        elif choice == 14:
            book.view_available_books()
        elif choice == 15:
            book.view_borrowed_books()
        elif choice == 16:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

