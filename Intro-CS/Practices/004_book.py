class Book(object):
    def __init__(self, title, author, borrowed=False):
        self.title = title
        self.author = author
        self.borrowed = borrowed
    
    # check if borrowed

    def borrow(self):
        """
        checks if already borrowed,
        if not,
        set borrowed to True
        """
        if self.borrowed:
            raise ValueError("Book Already Borrowed")
        else:
            self.borrowed = True
        return self.borrowed
    
    # return Book
    def return_book(self):
        """
        updates the borrowed
        status
        """
        self.borrowed = False
    
    # is available
    def is_available(self):
        available = False
        if not self.borrowed:
            available = True
        return available


# examples
# Create a new book
book1 = Book("The Art of Hacking", "Cybernerddd")

print("Available?", book1.is_available())   # True

# Borrow the book
print("Borrowing:", book1.borrow())         # True
print("Available?", book1.is_available())   # False
