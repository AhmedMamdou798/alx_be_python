class Book:
  """
  This class represents a base book object.
  """
  def __init__(self, title, author):
    """
    Initializes the book with title and author.

    Args:
      title (str): The title of the book.
      author (str): The author of the book.
    """
    self.title = title
    self.author = author

  def __str__(self):
    """
    Returns a string representation of the book in a basic format.

    Returns:
      str: A string representation of the book in the format "(title) by (author)"
    """
    return f"{self.title} by {self.author}"

class EBook(Book):
  """
  This class represents an Ebook derived from the Book class.
  """
  def __init__(self, title, author, file_size):
    """
    Initializes the Ebook with title, author, and file size.

    Args:
      title (str): The title of the Ebook.
      author (str): The author of the Ebook.
      file_size (int): The file size of the Ebook in KB.
    """
    super().__init__(title, author)  # Call base class constructor
    self.file_size = file_size

class PrintBook(Book):
  """
  This class represents a PrintBook derived from the Book class.
  """
  def __init__(self, title, author, page_count):
    """
    Initializes the PrintBook with title, author, and page count.

    Args:
      title (str): The title of the PrintBook.
      author (str): The author of the PrintBook.
      page_count (int): The page count of the PrintBook.
    """
    super().__init__(title, author)  # Call base class constructor
    self.page_count = page_count

  def __str__(self):
    """
    Returns a string representation of the PrintBook.

    Returns:
      str: A string representation of the PrintBook in the format
           "(title) by (author), Page Count: (page_count)"
    """
    return f"{self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
  """
  This class represents a Library that manages a collection of books.
  """
  def __init__(self):
    """
    Initializes the Library with an empty list to store books.
    """
    self.books = []

  def add_book(self, book):
    """
    Adds a Book, EBook, or PrintBook instance to the library collection.

    Args:
      book (Book, EBook, or PrintBook): The book object to be added.
    """
    self.books.append(book)

  def list_books(self):
    """
    Prints details of each book in the library.
    """
    for book in self.books:
      # Print book details based on the type
      if isinstance(book, EBook):
        print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB")
      elif isinstance(book, PrintBook):
        print(book)  # Use the __str__ method of PrintBook
      else:
        print(book)  # Use the __str__ method of Book