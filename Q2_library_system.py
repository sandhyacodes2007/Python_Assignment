

def add_book(catalog, book_id, title, author, year):
    catalog[book_id] = (title, author, year)
    print(f"Book '{title}' added.")


def borrow_book(catalog, borrowed_books, book_id):
    if book_id not in catalog:
        print(f"Book ID {book_id} does not exist.")
    elif book_id in borrowed_books:
        print(f"Book ID {book_id} is already borrowed.")
    else:
        borrowed_books.append(book_id)
        print(f"Book ID {book_id} borrowed successfully.")


def return_book(borrowed_books, book_id):
    if book_id in borrowed_books:
        borrowed_books.remove(book_id)
        print(f"Book ID {book_id} returned successfully.")
    else:
        print(f"Book ID {book_id} was not borrowed.")


def register_member(members, member_id):
    members.add(member_id)  # duplicates are ignored automatically


def show_available(catalog, borrowed_books):
    print("\nAvailable Books:")
    
    available = False
    for book_id, details in catalog.items():
        if book_id not in borrowed_books:
            title, author, year = details
            print(f"ID: {book_id} | {title} | {author} | {year}")
            available = True

    if not available:
        print("No books available.")


def main():
    # Data Structures
    catalog = {}          # Dictionary
    borrowed_books = []   # List
    members = set()       # Set

    # Add 4 books
    add_book(catalog, 101, "Python Basics", "John Smith", 2020)
    add_book(catalog, 102, "Data Structures", "Alice Brown", 2019)
    add_book(catalog, 103, "Algorithms", "Robert Lee", 2021)
    add_book(catalog, 104, "Database Systems", "Emma Davis", 2018)

    # Register 3 members (one duplicate)
    register_member(members, 1001)
    register_member(members, 1002)
    register_member(members, 1003)
    register_member(members, 1002)  # Duplicate

    print("\nRegistered Members:", members)

    # Borrow 2 books
    borrow_book(catalog, borrowed_books, 101)
    borrow_book(catalog, borrowed_books, 103)

    print("Borrowed Books:", borrowed_books)

    # Return 1 book
    return_book(borrowed_books, 101)

    print("Borrowed Books After Return:", borrowed_books)

    # Display available books
    show_available(catalog, borrowed_books)


if __name__ == "__main__":
    main()