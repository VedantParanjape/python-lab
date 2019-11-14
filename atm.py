import os

class atm:
    def __init__(self):
        self.__account= {}
        self.__counter = 0

    def ReturnDetails(self, account_number):
        return self.__account.get(account_number)

    def CreateAccount(self, name, balance, pin):
        details = {'name':name, 'balance':balance, 'pin':pin}
        temp = {self.__counter:details}
        self.__account.update(temp)
        self.__counter = self.__counter + 1

    def CheckUser(self, account_number, pin):
        details = self.__account.get(account_number)
        if details.get('pin') == pin:
            return True
        else:
            return False

    def CheckBalance(self, account_number):
        print('User balance = ', self.__account.get(account_number).get('balance'))
        a = input()

    def WithdrawCash(self, account_number):
        amount = int(input('enter amount to withdraw: '))
        balance = self.__account.get(account_number).get('balance')
        
        if(balance - amount >= 0):
            self.__account.get(account_number)['balance']= balance-amount
            print('new balance: ', balance - amount)
            a = input()
        else:
            print('insufficient balance')
            a = input()
    
    def ChangePin(self, account_number):
        if self.CheckUser(account_number, int(input('Enter old pin: '))):
            new_pin = int(input('Enter new pin: '))

            self.__account.get(account_number)['pin'] = new_pin
        else:
            print('incorrect pin')
            a = input() 
            
def menu():
    os.system('clear')
    print('1. Check Balance')
    print('2. Withdraw Balance')
    print('3. Change Pin')
    print('4. Exit')
    option = input('Enter option: ')

    return option

ATM = atm()

ATM.CreateAccount('vedant', 1000, 1234)
ATM.CreateAccount('shantanu', 1000, 2345)

opt = 1

tag = 0

while tag <= 3:
    os.system('clear')
    acc_num = int(input('enter account number: '))
    pin = int(input('enter account pin: '))
    det = ATM.ReturnDetails(acc_num)

    if det.get('pin') == pin:
        tag = 0
        while(1):
            opt = int(menu())

            if opt == 1:
                os.system('clear')
                ATM.CheckBalance(acc_num)

            if opt == 2:
                os.system('clear')
                ATM.WithdrawCash(acc_num)

            if opt == 3:
                os.system('clear')
                ATM.ChangePin(acc_num)

            if opt == 4:
                break

    else:
        tag = tag + 1
        print('incorrect pin')
        a = input()

print('wrong pin more than 3 times....exit')

