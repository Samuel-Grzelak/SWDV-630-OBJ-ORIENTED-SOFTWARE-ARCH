#import the class

from CheckingAccount import CheckingAccount

#checkingAccount object created
account = CheckingAccount("Samuel Grzelak","Chicago, IL",1001,0)

#calls to credit and debit the account

account.credtitAccount(550.00)
account.debitAccount(600.00)
account.debitAccount(10.00)

#call to display account balance
account.accBalance()