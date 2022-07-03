
import random
import os



std_code = 9999
password_db = [123]

class Menu():
    def __init__(self, principal):
        print("***** MORASOL BANK *****\n")
        print("How can we help you?\n ----------------- \n")
        opt = input(
            "(1) New Account\n ----------------- \n (2) Login\n ----------------- \n  (4) Exit\n ----------------- \n ")
        try:
            opt = int(opt)
        except ValueError:
            print(".........")

        while True:
            try:

                if (opt == 1):
                    new_account()
                if (opt == 2):
                    login(1, 2, 3, 4)
                if (opt == 4):
                    print("Thank you, have a nice day!")
                    exit()
                else:
                    print("Invalid option. Please enter a valid option")
                    Menu(1)


            except ValueError:
                    print("Invalid Option")
            continue





class Account():
    def __init__(self, name, SC, account, balance):

        self.SC = SC
        self.account = account
        self.balance = 0

    def deposit(self):
        amount_deposit = int(input("Enter the amount to Deposit:  "))
        if amount_deposit <= 0:
            print("Invalid Amount ")
        else:
            self.balance += amount_deposit
            print(f"Your new Balance is: {self.balance} £ ")

    def withdraw(self):
        amount_withdraw = float(input("Enter the amount to withdraw: "))
        self.balance -= amount_withdraw
        print(f"Withdraw Successfull, Your new balance is: {self.balance} £ ")

    def check_balance(self):
        print(f"Your Balance is: £{self.balance}  ")




#class User():
    #def __init__(self, name, password):
        #self.name = name
       # self.password = password




# FUNCOES GLOBAIS







def new_account():
    print("Please insert your details: ")
    name = input("Full Name ").title()
    password = input("New Password ")
    password_db.append(password)
    SC = std_code
    balance = 0
    print(f"Your Account Number : {random.choice(open('accounts.txt').read().split())} ")
    print(f"Your Sort-Code: {std_code} ")
    print(f"Your Balance: {balance} ")

    rep = int(input("Login? 1 = yes / 2 = no  "))
    if rep == 1:
        login(1, 2, 3, 4)
    else:
        Menu(1)


class login():

        #def check_id(self):
       # if SC == std_code:
            #print(f"Login Successfull! \n Welcome!\n Mr(s):{name}\n {SC}\n {account} \n How can we help you? \n ")
           # opt = int(input(
                    #"(1) Deposit\n ----------------- \n (2) Withdraw\n ----------------- \n(3) Check Balance\n ----------------- \n(4) Back to Menu\n ----------------- \n "))
        #elif password in password_db:
            #print("----------")
       # elif account in open('accounts.txt').read():
           # print("-----------------------------")
        #else:
           # print("Account or Sort-Code  Invalid \n Please try again!")
           # login(1, 2, 3, 4)

    while True:

        try:
            check_id(self)
            if (opt == 1):
                Account.deposit(self)
                break
            if (opt == 2):
                Account.withdraw(self)
                break
            if (opt == 3):
                Account.check_balance(self)
                break
            if (opt == 4):
                Menu(1)
            else:
                print("Invalid option. Please enter a valid option")
                Menu(1)
        except ValueError:
                print("Invalid Option")

                continue
      





Menu(1)








