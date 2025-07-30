class User :
    def  __init__(self,name,balance=0):
        self.name = name
        self.balance = balance
    def make_deposit(self,amount):
        self.balance += amount
    def make_withdrawal(self , amount):
        self.balance -= amount
    def display_user_balance(self):
         print(f"User: {self.name}, Balance: ${self.balance}")
    def transfer_mony(self,outher_user , amount):
         self.make_withdrawal(amount)
         outher_user.make_deposit(amount)

 

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