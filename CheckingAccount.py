#CheckingAccount.py

class CheckingAccount:

    #constructor
    def __init__(self,name,address,accountnumber,balance):

        self.name = name;
        self.address = address
        self.accNumber = accountnumber
        self._balance = balance

    #credit account with additonal funds
    def credtitAccount(self,amount):

        self._balance = self._balance + amount
        print("${:.2f} has been credited to account {} \n------------------------".format(amount, self.accNumber))

    #debit account and withdrawl funds
    def debitAccount(self,amount):

        if self._balance < amount:

            print("Not enough funds - Withdrawl of ${:.2f} canceled \n------------------------".format(amount))

        else:

            self._balance = self._balance - amount
    
    #display account information: account number, owner, and balance
    def accBalance(self):

        print("Account {} \n{}\nBalance of ${:.2f} \n------------------------".format(self.accNumber,self.name,self._balance))
    
