#Create Account Class
class Account:
    #create account constructor method
    def __init__(self, name, balance, min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance

    #Deposit Method
    def deposit(self, amount):
        self.balance += amount
        print(f'{self.name}, You Have Deposited {amount} into your account')

    #Withdrawal Method
    def withdraw(self, amount):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
            print(f'{amount} has been withdrawn from your account {self.name}')
        else:
            print(f'{self.name} ! Sorry, You dont have enough founds')
    
    #Statement Method
    def statement(self):
        self.balance

    def __str__(self):
        return f"Hi {self.name} Your balance is {self.balance}"

#Create Current Account Class and inherite the Account Class
class Current(Account):
    #Create Constructor method for the class and pass the default arguments
    def __init__(self, name, balance):


        #Call the Parent Constructor and Pass Child Class arguments
        super().__init__(name, balance, min_balance=-1000)

class Savings(Account):

    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance = 0)

gande = Savings('Apollos', 20000)

print(gande)

gande.deposit(2500)
print(gande)

gande.withdraw(500)
print(gande)


