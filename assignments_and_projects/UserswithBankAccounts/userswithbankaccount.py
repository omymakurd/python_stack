class User :
    
    def  __init__(self,name,balance=0):
        self.name = name
        self.account = BankAccount(balance=balance)
    def make_deposit(self,amount):
        self.account.deposit(amount)
    def make_withdrawal(self , amount):
        self.account.withdraw(amount)
    def display_user_balance(self):
         print(f"User: {self.name}, Balance: ${self.account.balance}")
    def transfer_mony(self,outher_user , amount):
         self.make_withdrawal(amount)
         outher_user.make_deposit(amount)
class BankAccount:
    def __init__(self, int_rate=0.01,balance=0):
        self.int_rate=int_rate
        self.balance=balance

    def deposit(self,amount):
        self.balance += amount
        return self

    def withdraw(self,amount):
        if self.balance >= amount:
           self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance : ${self.balance}")
        return self
    def yield_interest(self):
        if self.balance > 0 :
            self.balance +=self.balance*self.int_rate
        return self
user1 = User("Ahmed" ,500)
user2 = User("Sara",300)
user3=User("omyma",100)

user1.make_deposit(100)
user1.make_deposit(100)
user1.make_deposit(100)

user1.make_withdrawal(100)
user1.display_user_balance()


user2.make_deposit(100)
user2.make_deposit(100)
user2.make_withdrawal(100)
user2.make_withdrawal(100)
user2.display_user_balance()

user3.make_deposit(100)
user3.make_withdrawal(100)
user3.make_withdrawal(100)
user3.make_withdrawal(100)
user3.display_user_balance()

user1.transfer_mony(user2 , 50)
user1.display_user_balance()