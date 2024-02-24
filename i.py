from abc import ABC, abstractmethod


class Searchable(ABC):
    @abstractmethod
    def search_books(self, query):
        pass

class Borrowable(ABC):
    @abstractmethod
    def borrow_book(self, book_id, user_id):
        pass
    
    @abstractmethod
    def return_book(self, book_id, user_id):
        pass

class Manageable(ABC):
    @abstractmethod
    def add_book(self, book):
        pass
    
    @abstractmethod
    def remove_book(self, book_id):
        pass
    
    @abstractmethod
    def generate_reports(self):
        pass


class Librarian(Searchable, Borrowable, Manageable):
    def __init__(self):
        self.catalog = {}
        self.borrowed_books = {}

    def search_books(self, query):
        print(f"Searching for books with query: {query}")

    def borrow_book(self, book_id, user_id):
        print(f"Borrowing book with ID {book_id} for user {user_id}")

    def return_book(self, book_id, user_id):
        print(f"Returning book with ID {book_id} from user {user_id}")

    def add_book(self, book_id, book):
        print(f"Adding book to the catalog: {book} with ID {book_id}")

    def remove_book(self, book_id):
        print(f"Removing book from the catalog with ID: {book_id}")

    def generate_reports(self):
        print("Generating reports")

class Member(Searchable, Borrowable):
    def search_books(self, query):
        print(f"Searching for books with query: {query}")

    def borrow_book(self, book_id, user_id):
        print(f"Borrowing book with ID {book_id} for user {user_id}")

    def return_book(self, book_id, user_id):
        print(f"Returning book with ID {book_id} from user {user_id}")


def main():
    librarian = Librarian()
    librarian.add_book("Dune", 9780441013593)

    guest_member = Member()
    guest_member.search_books("Dune")
    guest_member.borrow_book(9780441013593, 800685560)
    guest_member.return_book(9780441013593, 800685560)

if __name__ == "__main__":
    main()
