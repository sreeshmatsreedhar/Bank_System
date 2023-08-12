class BankAccount:
    acc_no=4205300
    no_cust=0
    def __init__(self,name,initial_deposit,contact_no,pin,city):
        self.name=name
        self.city=city
        self.contact_no=contact_no
        self.acc_balance=initial_deposit
        self.pin=pin
        self.cust_acc_no=BankAccount.acc_no
        BankAccount.acc_no=BankAccount.acc_no+1
# profile,to print detailes of the customer
    def profile(self):
        print(f'Name:{self.name}\tcity:{self.city}\tcontact number:{self.contact_no}\tAccount number:{self.cust_acc_no}')
        BankAccount.my_choice(self)
#to deposite money
    def deposit(self):
        amount=int(input('Enter your deposit amount:'))
        if amount>0:
            self.acc_balance=self.acc_balance+amount
            print(f'Transaction completed.  Current balance:₹{self.acc_balance}')
            BankAccount.my_choice(self)
        else:
            print('Invalid amound !!!\nTransaction cancelled!!!')
            BankAccount.my_choice(self)
# to withdraw money
    def withdraw(self):
        amount=int(input('Enter withdrawl amount:'))
        if amount<=self.acc_balance and amount >0:
            self.acc_balance=self.acc_balance-amount
            print(f'Transaction completed.  Current balance:₹{self.acc_balance}')
            BankAccount.my_choice(self)
        else:
            print('Trancasction cancelled!!\nInsufficient bank balance\nCheck your balance and try again.')
            BankAccount.my_choice(self)
#to make payment to another account
    def payment(self,other):
        print('>.>.PAYMENT.<.<')
        amount=int(input('Enter payment amount:'))
        if amount <= self.acc_balance and amount > 0:
            self.acc_balance = self.acc_balance - amount
            other.acc_balance=other.acc_balance+amount
            print(f'Transaction completed.  Current balance:₹{self.acc_balance}')
            BankAccount.my_choice(self)
        else:
            print('Trancasction cancelled!!\nInsufficient bank balance\nCheck your balance and try again.')
            BankAccount.my_choice(self)
#log out
    def logout(self):

        print('YOU HAVE BEEN LOGGED OUT')
        print('Thank you for using Jandhan Bank online service. Hope you find our service useful.\nTo know more about Jandhan Bank and services, please visit your nearest branch.\nComplaints and suggestions can be sent to us via email at jhandanabank.complaint.@gmail.com.')
    def my_choice(self):
        print('\n*****************************************************************\n')
        print('Make your choice\npress1:My profile\npress2:Deposit\npress3:Withdraw\npress4:About us\npress5:Check my balance\npress6:Log out')
        a = int(input('Enter your option:'))
        print('\n*****************************************************************\n')
        if a == 1:
            BankAccount.profile(self)
        elif a == 2:
            BankAccount.deposit(self)
        elif a == 3:
            BankAccount.withdraw(self)
        elif a == 4:
            print('\t\t\tJANDHAN BANK\t\nJandhan Bank is a Commercial Banks.JDB is an Indian Multinational,\nPublic Sector Banking and Financial services statutory body\n headquartered in calicut. The rich heritage and legacy since 1988.')
            BankAccount.my_choice(self)
        elif a == 5:
            print(f'Current balance:₹{self.acc_balance}')
            BankAccount.my_choice(self)
        elif a == 6:
            BankAccount.logout(self)
    def login(self):
        print('\n>>>>Login<<<<\n')
        user=input("Enter your name as per registered:")
        pin=int(input('Enter six digit security pin:'))
        if user==self.name and pin==self.pin:
            print('Welcome to JANDHAN BANK')
            BankAccount.my_choice(self)
        else:
            print('Invalid name or pin!!!')
            BankAccount.register(self)
            #Registraion of new customer and login
    def register(self):
        print('\n\n____JANDHAN BANK____')
        print('Your personal financial partner')
        print('             since 1988\n\n')
        n=int(input('Enter 1 if already Registerd else enter 2...'))
        if n==2:
            self.name=input('\nEnter your name:')
            self.city=input('Enter your city:')
            self.contact_no=input('Enter your phone no:')
            print('note the pin, it will help you further communication with us.\nDo not share it anyone!!')
            self.pin=int(input('Enter six digit pin:'))
            print(f'Account created successfully\nYour Account Number is{self.cust_acc_no}')
            self.acc_balance=0
            print(f'\nWelcome {self.name}')
            print('loging to JANDHAN BANk using name&pin')
            self.cust_acc_no=self.cust_acc_no+1
            self.no_cust=self.no_cust+1

            BankAccount.login(self)
        elif n==1:
            BankAccount.login(self)
        else:
            BankAccount.register(self)


if __name__=='__main__':
    c = BankAccount('Radha', 300, 98767898, 234561, 'bombay')
    v=BankAccount('seema',400,989786787,123456,'New delhi')
    #c.payment(v)
    d=input('could you like to enter JANDHAN BANK online service\nif YES press 1 if NO press any key ')
    if d=='1':

        print(BankAccount.register(c))
    #

