class BankAccount(object):
  balance = 0
  def __init__(self, name):
    self.name = name
  def __repr__(self):
    return "This is %s's account and the balance is $%.2f" % (self.name, self.balance)
  
  def show_balance(self):
    print "Current Balance: $%.2f" % (self.balance)
  
  def deposit(self, amount):
    if amount <= 0:
      print "Your deposit is too low"
      return
    else:
      print "You are depositing $%.2f" % (amount)
    self.balance += amount
    self.show_balance()
    
  def withdraw(self, amount):
    if amount > self.balance:
      print "You are trying to withdraw more than what is currently in your account"
    else:
      print "You are withdrawing $%.2f" % (amount)
    self.balance -= amount
    self.show_balance()
    
my_account = BankAccount("Dan")
print my_account
my_account.show_balance()
my_account.deposit(2000)
my_account.withdraw(3000)
print my_account
