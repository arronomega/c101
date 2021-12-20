class Atm :
    def __init__(self,cardnum,pin) -> None:
        self.cardnum = cardnum
        self.pin = pin
        self.balance=10000
    def cash_withdraw(self):
        print("You have withdrawn $1000")
        self.balance=self.balance-1000
    def cash_deposit(self,balance):
        print("You have deposited $1000")
        self.balance=self.balance+1000
    def balanceEnquiry(self):
        print("Your balance is "+ str(self.balance))


reponse = input("What do you want to do? write 1 for your balance , 2 for cash deposit or 3 for cash withdraw")

atm = Atm(202212312,2835)

if reponse == "1":
    atm.balanceEnquiry()
if reponse == "2":
    atm.cash_withdraw()
    print("Your new balance " + str(atm.balance))
if reponse == "3":
    atm.cash_deposit()
    print("Your new balance " + str(atm.balance))
