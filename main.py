# ── BOOK CLASS ─────────────────────────────────────────────────

class Book:

    # Initialize the book attributes
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    # Borrow a book
    def borrow(self):
        if self.is_borrowed:
            print(f'"{self.title}" is already borrowed.')
        else:
            self.is_borrowed = True
            print(f'You have borrowed "{self.title}".')

    # Return a book
    def return_book(self):
        if not self.is_borrowed:
            print(f'"{self.title}" was not borrowed.')
        else:
            self.is_borrowed = False
            print(f'You have returned "{self.title}".')

    # Display book details
    def __str__(self):
        if self.is_borrowed:
            status = "Borrowed"
        else:
            status = "Available"

        return f"{self.title} by {self.author} [{status}]"


# ── LIBRARY ────────────────────────────────────────────────────

# Create three Book objects
book1 = Book("Python Crash Course", "Eric Matthes")
book2 = Book("Atomic Habits", "James Clear")
book3 = Book("The Alchemist", "Paulo Coelho")

print("=" * 42)
print("         📚  LIBRARY SYSTEM")
print("=" * 42)

# Display all books
print("\n--- Initial Book List ---")
print(book1)
print(book2)
print(book3)

# Borrow some books
print("\n--- Borrow Books ---")
book1.borrow()
book2.borrow()

# Try to borrow the same book twice
print("\n--- Try Borrowing Again ---")
book1.borrow()

# Return a borrowed book
print("\n--- Return Book ---")
book1.return_book()

# Try to return a book that was never borrowed
print("\n--- Try Returning an Available Book ---")
book3.return_book()

# Display all books again to show updated status
print("\n--- Updated Book List ---")
print(book1)
print(book2)
print(book3)

print("\n" + "=" * 42)
print("         END OF LIBRARY SYSTEM")
print("=" * 42)