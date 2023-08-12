# Bank_System
This is a python project of simple banking system using 'BankAccount' class,and named the bank as JANDHAN.
It allows user to create new account in this bank,login,view their profile,make payment,deposit,withdraw,check balance and log out.
Class attributes: acc_no (used to generate account numbers), no_cust (count of customers), and methods.
The __init__ method is the constructor that initializes account details when a new instance is created.
profile(): Displays the user's profile and calls the my_choice() method.
deposit(): Allows the user to deposit funds into their account.
withdraw(): Allows the user to withdraw funds from their account if the balance is sufficient.
payment(other): Enables the user to transfer funds to another account (other).
logout(): Logs the user out of their account.
my_choice(): Provides a menu for users to choose actions and directs to respective methods.
login(): Validates user credentials and logs them in.
register(): Facilitates user registration and login.
