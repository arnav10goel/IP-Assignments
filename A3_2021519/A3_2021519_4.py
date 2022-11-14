class Person:
    def __init__(self, firstname: str, lastname: str, age: int):
        self.first = firstname
        self.last = lastname
        self.age = age
    
    def object_info(self):
        print(f'{self.first} {self.last} {self.age}')

def sort_attribute(query, lst_obj):
    if query == 'firstname':
        lst_firstname.sort()
        print('Order: ')
        for i in range(len(lst_firstname)):
            for j in range(len(lst_obj)):
                if lst_firstname[i] == lst_obj[j].first:
                    lst_obj[j].object_info()
        
    elif query == 'lastname':
        lst_lastname.sort()
        print('Order: ')
        for i in range(len(lst_lastname)):
            for j in range(len(lst_obj)):
                if lst_lastname[i] == lst_obj[j].last:
                    lst_obj[j].object_info()

    elif query == 'age':
        lst_age.sort()
        print('Order: ')
        for i in range(len(lst_age)):
            for j in range(len(lst_obj)):
                if lst_age[i] == lst_obj[j].age:
                    lst_obj[j].object_info()
    else:
        print('No such Query')

print('Welcome to the Application!')
print()
n = int(input('Specify number of people to be enrolled: '))
lst_firstname = []
lst_lastname = []
lst_age = []
lst_obj = []
print()
for i in range(1, n+1):
    first = input(f'Enter Firstname for Person {i}: ')
    second = input(f'Enter Lastname for Person {i}: ')
    age = input(f'Enter Age for Person {i}: ')
    print()
    obj = Person(first, second, age)
    lst_firstname.append(obj.first)
    lst_lastname.append(obj.last)
    lst_age.append(obj.age)
    lst_obj.append(obj)

queries = int(input("Specify number of queries: "))
print()
for i in range(1, queries+1):
    query = input(f'Query {i}: ')
    sort_attribute(query, lst_obj)