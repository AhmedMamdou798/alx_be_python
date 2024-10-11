class Book:
  """
  A class representing a book in the library.
  """

  def __init__(self, title, author):
    """
    Initializes a Book object with title, author, and availability status.

    Args:
      title: The title of the book.
      author: The author of the book.
    """
    self.title = title
    self.author = author
    self._is_checked_out = False  # Private attribute for availability

  def __str__(self):
    """
    Defines how a Book object is represented as a string.

    Returns:
      A string representation of the book (title by author).
    """
    return f"{self.title} by {self.author}"

  def check_out(self):
    """
    Marks the book as checked out (unavailable).
    """
    self._is_checked_out = True

  def return_book(self):
    """
    Marks the book as returned (available).
    """
    self._is_checked_out = False

  def is_checked_out(self):
    """
    Returns whether the book is currently checked out.

    Returns:
      True if the book is checked out, False otherwise.
    """
    return self._is_checked_out


class Library:
  """
  A class representing a library with a collection of books.
  """

  def __init__(self):
    """
    Initializes a Library object with an empty list to store books.
    """
    self._books = []

  def add_book(self, book):
    """
    Adds a Book object to the library's collection.

    Args:
      book: A Book object to be added to the library.
    """
    self._books.append(book)

  def check_out_book(self, title):
    """
    Checks out a book by title, marking it as unavailable if found.

    Args:
      title: The title of the book to be checked out.

    Returns:
      True if the book is found and checked out successfully, False otherwise.
    """
    for book in self._books:
      if book.title == title and not book.is_checked_out():
        book.check_out()
        return True
    return False

  def return_book(self, title):
    """
    Returns a book by title, marking it as available if found.

    Args:
      title: The title of the book to be returned.

    Returns:
      True if the book is found and returned successfully, False otherwise.
    """
    for book in self._books:
      if book.title == title and book.is_checked_out():
        book.return_book()
        return True
    return False

  def list_available_books(self):
    """
    Prints a list of all available books in the library.
    """
    print("Available books:")
    for book in self._books:
      if not book.is_checked_out():
        print(book)


# Run the library management simulation
