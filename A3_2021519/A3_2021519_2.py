class LaundryService:
    id = 0
    
    def __init__(self, name: str, contact: int, email: str, type_cloth: str, brand: int, season: str):
        self.name = name
        self.contact = contact
        self.email = email
        self.cloth = type_cloth.lower()
        self.brand = bool(brand)
        self.season = season.lower()
        LaundryService.id += 1
        self.id = LaundryService.id

    def customerDetails(self):
        print('--------------------********-----------------------')
        print('Customer Specific Details: ')
        print()
        print(f'Customer ID: {self.id}')
        print(f'Customer Name: {self.name}')
        print(f'Contact: {self.contact}')
        print(f'Email: {self.email}')
        print(f'Type of Cloth: {self.cloth}')
        if self.brand:
            print('Branded')
        else:
            print('Not Branded')
    
    def calcCharge(self):
        charge = 0
        dict = {'cotton': 50, 'silk': 30, 'woolen': 90, 'polyester': 20}
        for x,y in list(dict.items()):
            if x == self.cloth:
                charge += dict[x]
        
        if self.brand:
            charge = (1.5)*charge
        else:
            pass

        if self.season == 'winter':
            charge = charge / 2
        else:
            charge = 2 * charge

        return charge

    def finalDetails(self):
        self.customerDetails()
        print(f'Total Charge: {self.calcCharge()}')
        if self.calcCharge() >= 200:
            print('To be returned in 4 days!')
            print('--------------------********-----------------------\n')
        else:
            print('To be returned in 7 days!\n')
            print('--------------------********-----------------------\n')


n = int(input("How many objects are there (atleast 4 should be there)? "))

for i in range(n):
    name = input('Name: ')
    contact = int(input('Contact No: '))
    email = input('Email: ')
    type_cloth = input('Type of Cloth: ')
    brand = int(input('Branded or Not (1/0): '))
    season = input('Season: ')

    c1 = LaundryService(name, contact, email, type_cloth, brand, season)
    c1.finalDetails()