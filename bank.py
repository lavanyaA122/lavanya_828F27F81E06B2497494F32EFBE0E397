 class BankAccount:
 
  def _init_(self, account_number, account_holder_name, initial_balance=0.0):
      
  self.__account_number = account_number
     
   self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__account_balance}")
        else:
            print("Invalid deposit amount. Please enter a positive amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__account_balance}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def display_balance(self):
        print(f"Account Number: {self.__account_number}")
        print(f"Account Holder: {self.__account_holder_name}")
        print(f"Account Balance: ${self.__account_balance}")

# Example usage:
if _name_ == "_main_":
    account = BankAccount("123456789", "John Doe", 1000.0)
    
    account.display_balance()
   
account.deposit(500.0)
   
account.withdraw(200.0)
   
account.display_balance()
 class Player:
    
def play(self):
   
     print("The player is playing cricket.")


class Batsman(Player):
    
def play(self):
      
  print("The batsman is batting.")


class Bowler(Player):
   
def play(self):
        
print("The bowler is bowling.")


# Example usage:
if _name_ == "_main_":
 
   batsman = Batsman()
    bowler = Bowler()
    
    batsman.play()
   
 bowler.play()
 # Python 3 program to find 

# factorial of given number
def factorial(n):
 
   if n < 0:
     
   return 0
  
  elif n == 0 or n == 1:
      
  return 1
    
else:
     
   fact = 1
  
      while(n > 1):
   
         fact *= n
         
   n -= 1
       
 return fact
 
# Driver Code
num = 5
print("Factorial of",num,"is",
factorial(num))

 
# This code is contributed by Dharmik Thakkar