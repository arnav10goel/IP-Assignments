from datetime import datetime

class BankAccount:
    def __init__(self, username, password, current):
        self.username = username
        self.password = password
        self.current = current

        filename = './A3_2021519_3/u.txt'
        f = open(filename, 'w')
        f.close()

    def authenticate(self):
        count = 3
        while count != 0:
            string = input('What is your secret password? ')
            if string == self.password:
                return True
            else:
                print('Wrong Attempt, Please Retry')
                count -= 1
        return False
    
    def deposit(self):
        try:
            assert self.authenticate()
            pass
        except:
            print('Too many wrong re-attempts')
            return
        amt = int(input('How much amount needs to be added? '))
        self.current += amt
        f = open('./A3_2021519_3/u.txt', 'a')
        time = datetime.now()
        f.write(f'{time} The amount of Rupees {amt} has been added, Current balance -> {self.current}\n')
        f.close()
        print()
        
    def withdraw(self):
        try:
            assert self.authenticate()
            pass
        except:
            print('Too many wrong re-attempts')
            return
        amt = int(input('How much amount needs to be withdrawn? '))
        try:
            assert amt <= self.current
            pass
        except AssertionError:
            print('Low Balance! Cannot be debited at this time!')
            return 
        self.current -= amt
        f = open('./A3_2021519_3/u.txt', 'a')
        time = datetime.now()
        f.write(f'{time} The amount of Rupees {amt} has been debited, Current balance -> {self.current}\n')
        f.close()
        print()

    def bankStatement(self):
        try:
            assert self.authenticate()
            pass
        except:
            print('Too many wrong re-attempts')
            return
        f2 = open('./A3_2021519_3/u.txt', 'r')
        data = f2.readlines()
        lines = [i.strip() for i in data]
        print(f'Hey {self.username}! Your transactions history: \n')
        for i in lines:
            print(i)
        print()
        f2.close()

print('Welcome to the Bank of IIITD')
print()

name = input('Enter Username: ')
password = input('Enter Password: ')
balance = int(input('Starting Balance for your Account: '))
chomu = BankAccount(name, password, balance)
while True:
    print('Select your Option: ')
    print('1. Deposit')
    print('2. Withdraw')
    print('3. Bank Statement')
    choice = int(input('Enter your Choice (1/2/3): '))
    if choice == 1:
        chomu.deposit()
        consent = input('Do you wish to continue? (Y/N): ')
        print(consent.lower())
        if consent == 'y':
            pass
        elif consent == 'n':
            break
        else:
            print('Choose between Y and N only')

    elif choice == 2:
        chomu.withdraw()
        consent = input('Do you wish to continue? (Y/N): ')
        consent.lower()
        if consent == 'y':
            pass
        elif consent == 'n':
            break
        else:
            print('Choose between Y and N only')
    elif choice == 3:
        chomu.bankStatement()
        consent = input('Do you wish to continue? (Y/N): ')
        consent.lower()
        print(consent)
        if consent == 'y':
            pass
        elif consent == 'n':
            break
        else:
            print('Choose between Y and N only')
    else:
        print('Choose between 1,2 and 3 only.')