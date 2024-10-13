class Book:
  """
  This class represents a Book with title, author, and publication year.
  """

  def __init__(self, title, author, year):
    """
    Initializes the Book object with the provided title, author, and year.

    Args:
      title (str): The title of the book.
      author (str): The author of the book.
      year (int): The publication year of the book.
    """
    self.title = title
    self.author = author
    self.year = year

  def __del__(self):
    """
    Prints a message when the Book object is deleted.

    This method is called by Python's garbage collector 
    when the object is no longer referenced.
    """
    print(f"Deleting {self.title}")

  def __str__(self):
    """
    Returns a string representation of the book in a human-readable format.

    Returns:
      str: A string representation of the book in the format
           "(title) by (author), published in (year)"
    """
    return f"{self.title} by {self.author}, published in {self.year}"

  def __repr__(self):
    """
    Returns a string representation of the Book object that can be used to recreate it.

    This is the official representation and can be used with eval() to create a new instance.

    Returns:
      str: A string representation in the format 
           "Book('{self.title}', '{self.author}', {self.year})"
    """
    return f"Book('{self.title}', '{self.author}', {self.year})"

# This part is for testing purposes and not included in book_class.py
if __name__ == "__main__":
  # Creating an instance of Book
  my_book = Book("1984", "George Orwell", 1949)

  # Demonstrating the __str__ method
  print(my_book)  # Expected to use __str__

  # Demonstrating the __repr__ method
  print(repr(my_book))  # Expected to use __repr__

  # Deleting a book instance to trigger __del__
  del my_book