class BankAccount:
  """
  A class representing a bank account with deposit, withdraw, and balance display functionalities.
  """
  def __init__(self, initial_balance=0.0):
    """
    Initializes a BankAccount object with an optional initial balance. Defaults to 0.0.
    """
    self.account_balance = initial_balance

  def deposit(self, amount):
    """
    Deposits the specified amount into the account balance.
    """
    self.account_balance += amount

  def withdraw(self, amount):
    """
    Attempts to withdraw the specified amount from the account balance.
    Returns True if successful, False otherwise.
    """
    if amount <= self.account_balance:
      self.account_balance -= amount
      return True
    else:
      return False

  def display_balance(self):
    """
    Prints the current account balance in a user-friendly format.
    """
    print(f"Current Balance: ${self.account_balance:.2f}")