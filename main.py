class Book:
    def __init__(self, title):
        self.title = title
        self.borrowed = False

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title):
        book = Book(title)
        self.books.append(book)
        print(f'Book {title} has been added to the library')

    def borrow_book(self, title, user):
        for book in self.books:
            if book.title == title and not book.borrowed:
                book.borrowed = True
                user.borrowed_books.append(book)
                print(f'Book {title} has been borrowed by {user.name}')
                return
        print(f'Book {title} is either not available or already borrowed ')

    def return_book(self, title, user):
        for book in user.borrowed_books:
            if book.title == title and book.borrowed:
                book.borrowed = False
                user.borrowed_books.remove(book)
                print(f'Book {title} has been returned by {user.name}')
                return
        print(f'Book {title} is either not in the library or not borrowed by {user.name}')

    def display_available_books(self):
        if not self.books:
            print('No books available in the library')
        else:
            print('\nAvailable Books in the library:')
            for book in self.books:
                if not book.borrowed:
                    print(book.title)

class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

def main():
    library = Library()

    user_name = input('enter your name: ')
    user = User(user_name)

    while True:
        print('\nLibrary menu:')
        print("1. Add a Book")
        print("2. Borrow a Book")
        print("3. Return a Book")
        print("4. View Borrowed Books")
        print("5. Display Available Books")
        print("6. Exit")

        choice = input('Enter your choice (1-6):')

        try:

            if choice == '1':
                title = input('Enter the title of the book to add: ')
                library.add_book(title)

            elif choice == '2':
                title = input('Enter the title of the book to borrow: ')
                library.borrow_book(title, user)

            elif choice == '3':
                title = input('Enter the title of the book to return: ')
                library.return_book(title, user)

            elif choice == '4':
                print(f'\nBorrowed Books by {user.name}: ')
                for book in user.borrowed_books:
                    print(book.title)

            elif choice == '5':
                library.display_available_books()

            elif choice == '6':
                print('Exiting the program. Goodbye')
                break

            else:
                print('Invalid choice. Please enter a number between 1 and 6.')
        except ZeroDivisionError:
            print('ZeroDivisionError')
        except ValueError:
            print('ValueError')
        except TypeError:
            print('TypeError')
        except Exception as a:
            print('error', a)

if __name__ == '__main__':
    main()











