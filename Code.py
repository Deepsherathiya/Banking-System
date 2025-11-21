from abc import ABC, abstractmethod

class BankAccount(ABC):

    def _init_(self, Acc_Number, balance):
        self.Acc_number=Acc_Number
        self.balance=balance

    def deposit(self,amount):
        self.balance += amount
        print(f"{amount} deposit in account.")

    def withdraw(self,amount):
        if amount <=self.balance:
            self.balance=self.balance-amount
            print(f"{amount} is withdrew from account.")
        
        else:
            print("Insufficient balance")

    def CheckBalance(self):
        print(f"The available balance is {self.balance}")
    
    @abstractmethod
    def CalculateInterest(self):
        pass

class SavingAccount(BankAccount):
    
    def CalculateInterest(self):
        interest=self.balance*0.03
        self.balance += interest
        print(f"The interest is{interest}")

class CurrentAccount(BankAccount):

    def CalculateInterest(self):
        print("Current Account don't have interest.")

class Bank:

    total_account=0
    @staticmethod
    def IncrementAccount():
        Bank.total_account += 1
    @staticmethod
    def GetTotalAccount():
        return Bank.total_account
    
class MainApp:
    
    def _init_(self):
        
        self.accounts={}

    def create_Savingaccounts(self):

        account_number=int(input("Enter the bank number: "))
        initial_balance=float(input("Enter the initial amount to deposit in the bank: "))
        self.accounts[account_number]=SavingAccount(account_number,initial_balance)
        Bank.IncrementAccount()
        print("Saving account created successfully.")

    def create_Currentaccount(self):

        account_number=int(input("Enter the bank number: "))
        initial_balance=float(input("Enter the initial amount to deposit in the bank: "))
        self.accounts[account_number]=CurrentAccount(account_number,initial_balance)
        Bank.IncrementAccount()
        print("Current account created successfully.")

    def Deposit(self):
        account_number=int(input("Enter the account number: "))
        if account_number in self.accounts:
            amount=int(input("Enter amount to be deposited: "))
            self.accounts[account_number].deposit(amount)
        
        else:
            print("Account not found")
        
    def withdraw_money(self):
        account_number=int(input("Enter the account number: "))
        if account_number in self.accounts:
            amount=int(input("Enter amount to be withdrawn"))
            self.accounts[account_number].withdraw(amount)
        
        else:
            print("Account not found.")
    
    def balance_check(self):
        account_number=int(input("Enter the account number: "))
        if account_number in self.accounts:
            self.accounts[account_number].CheckBalance()
        else: 
            print("Account not found.")
    def CI(self):
        account_number=int(input("Enter the account number: "))
        if account_number in self.accounts:
            self.accounts[account_number].CalculateInterest()
        else: 
            print("Account not found.")
    def TotalAccount(Self):
        print(f"Total number of Accounts are: {Bank.GetTotalAccount()}")
    
    def run(self):
        while True:

            print("\nMenu: ")
            print("1. Create Saving Account.")
            print("2. Create Current Account.")
            print("3. Deposit Money.")
            print("4. Withdraw Money.")
            print("5. Check Balance.")
            print("6. Calculate Interest.")
            print("7. Display Total  Number of Accounts.")
            print("8. Exit.")
            choice = int(input("Enter the choice: "))

            if choice==1:
                self.create_Savingaccounts()
            elif choice==2:
                self.create_Currentaccount()
            elif choice==3:
                self.Deposit()
            elif choice==4:
                self.withdraw_money()
            elif choice==5:
                self.balance_check()
            elif choice==6:
                self.CI()
            elif choice==7:
                self.TotalAccount()
            elif choice==8:
                print("Exiting Program. ThankYou!")
                break
            else:
                print("Invalid Choice.")
            
Obj=MainApp()
Obj.run()
