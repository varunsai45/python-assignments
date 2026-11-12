print("========== LIBRARY MANAGEMENT SYSTEM ==========")


class Person:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id


class Member(Person):
    def __init__(self, name, member_id):
        super().__init__(name, member_id)
        self.borrowed_books = []

    def show_details(self):
        books = ", ".join(self.borrowed_books) if self.borrowed_books else "None"
        print(f"{self.member_id:<10} {self.name:<22} {books}")


class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True
        self.issued_to = None

    def show_details(self):
        status = "Available" if self.is_available else f"Issued to {self.issued_to}"
        print(f"{self.book_id:<10} {self.title:<30} {self.author:<22} {status}")


class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self):
        book_id = input("Enter book ID: ").strip().upper()
        if not book_id:
            print("Book ID cannot be empty!")
            return
        if book_id in self.books:
            print("A book with this ID already exists.")
            return

        title = input("Enter book title: ").strip().title()
        author = input("Enter author name: ").strip().title()
        if not title or not author:
            print("Title and author cannot be empty!")
            return

        self.books[book_id] = Book(book_id, title, author)
        print(f"Book '{title}' added to the library.")

    def register_member(self):
        member_id = input("Enter member ID: ").strip().upper()
        if not member_id:
            print("Member ID cannot be empty!")
            return
        if member_id in self.members:
            print("A member with this ID already exists.")
            return

        name = input("Enter member name: ").strip().title()
        if not name:
            print("Member name cannot be empty!")
            return

        self.members[member_id] = Member(name, member_id)
        print(f"Member '{name}' registered successfully.")

    def issue_book(self):
        book_id = input("Enter book ID to issue: ").strip().upper()
        member_id = input("Enter member ID: ").strip().upper()

        book = self.books.get(book_id)
        member = self.members.get(member_id)

        if book is None:
            print("Book not found.")
            return
        if member is None:
            print("Member not found.")
            return
        if not book.is_available:
            print(f"Sorry, '{book.title}' is already issued to {book.issued_to}.")
            return

        book.is_available = False
        book.issued_to = member.name
        member.borrowed_books.append(book.title)
        print(f"'{book.title}' issued to {member.name} ({member.member_id}).")

    def return_book(self):
        book_id = input("Enter book ID to return: ").strip().upper()
        book = self.books.get(book_id)

        if book is None:
            print("Book not found.")
            return
        if book.is_available:
            print(f"'{book.title}' is already available in the library.")
            return

        member = None
        for registered_member in self.members.values():
            if book.title in registered_member.borrowed_books:
                member = registered_member
                break

        book.is_available = True
        book.issued_to = None
        if member is not None:
            member.borrowed_books.remove(book.title)
            print(f"'{book.title}' returned by {member.name}.")
        else:
            print(f"'{book.title}' returned to the library.")

    def search_book(self):
        query = input("Enter title or author to search: ").strip().lower()
        if not query:
            print("Search text cannot be empty!")
            return

        matches = [
            book
            for book in self.books.values()
            if query in book.title.lower() or query in book.author.lower()
        ]

        if not matches:
            print("No matching books found.")
            return

        print("\n" + "=" * 85)
        print(f"{'Book ID':<10} {'Title':<30} {'Author':<22} {'Status':<20}")
        print("-" * 85)
        for book in matches:
            book.show_details()
        print("=" * 85)

    def display_books(self):
        if not self.books:
            print("No books in the library.")
            return

        print("\n" + "=" * 85)
        print("LIBRARY BOOKS")
        print("=" * 85)
        print(f"{'Book ID':<10} {'Title':<30} {'Author':<22} {'Status':<20}")
        print("-" * 85)
        for book_id in sorted(self.books):
            self.books[book_id].show_details()
        print("=" * 85)
        available = sum(1 for book in self.books.values() if book.is_available)
        print(f"Total books: {len(self.books)}    Available: {available}")

    def display_members(self):
        if not self.members:
            print("No members registered.")
            return

        print("\n" + "=" * 75)
        print("LIBRARY MEMBERS")
        print("=" * 75)
        print(f"{'Member ID':<10} {'Name':<22} {'Borrowed Books'}")
        print("-" * 75)
        for member_id in sorted(self.members):
            self.members[member_id].show_details()
        print("=" * 75)


library = Library()
library.books["B101"] = Book("B101", "Python Programming", "Reema Thareja")
library.books["B102"] = Book("B102", "Data Structures", "Seymour Lipschutz")
library.books["B103"] = Book("B103", "Database Systems", "Korth And Silberschatz")
library.members["M001"] = Member("Aarav Sharma", "M001")
library.members["M002"] = Member("Diya Patel", "M002")

while True:
    print("\n1. Add Book")
    print("2. Register Member")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Search Book")
    print("6. Display All Books")
    print("7. Display All Members")
    print("8. Exit")

    choice = input("Enter your choice (1-8): ").strip()

    if choice == "1":
        library.add_book()
    elif choice == "2":
        library.register_member()
    elif choice == "3":
        library.issue_book()
    elif choice == "4":
        library.return_book()
    elif choice == "5":
        library.search_book()
    elif choice == "6":
        library.display_books()
    elif choice == "7":
        library.display_members()
    elif choice == "8":
        print("Exiting Library Management System. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 8.")
