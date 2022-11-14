class Student:
    def __init__(self, namestu: str, cgpa: float, branch: str):
        self.namestu = namestu
        self.cgpa = cgpa
        self.branch = branch
        self.isPlaced = False
    
    def isEligible(self, company):
        if self.cgpa >= company.grade and self.branch in company.branches and not self.isPlaced:
            print(f'{self.namestu} is eligible for the Company {company.name}.')
            return True
        else:
            print(f'{self.namestu} is not eligible for the Company {company.name}.')
            return False
    
    def Apply(self, company):
        company.appliedStudents.append(self.namestu)
    
    def getsPlaced(self):
        self.isPlaced = True

class Company:
    def __init__(self, name: str, requiredcgpa: float, branches, positionOpen: int):
        self.name = name
        self.grade = requiredcgpa
        self.branches = branches
        self.num = positionOpen
        self.appliedStudents = []
        self.applicationOpen = True

    def hireStudents(self):
        count = 0
        for i in range(len(lst_obj)):
            if lst_obj[i].namestu in self.appliedStudents[:self.num]:
                count += 1
                lst_obj[i].getsPlaced()
                print(f'Student {lst_obj[i].namestu} has been hired by Company {self.name}')
        print(f'Company {self.name} has hired {count} students.')
        self.closeApplication()
    
    def closeApplication(self):
        self.applicationOpen = False

n = int(input('Enter the Number of Students: \n'))
lst_obj = []
for i in range(n):
    name = input(f'Enter Name of Student {i+1}: \n')
    while True:
        try:
            grade = float(input(f'Enter CGPA of Student {i+1}: \n'))
            assert 0 <= grade <= 10
            break
        except AssertionError:
            print('The CGPA is invalid, enter CGPA of student again\n')
    branch = input(f'Enter Branch of Student {i+1}: \n')
    Stu = Student(name, grade, branch)
    lst_obj.append(Stu)

#Sorts list of objects according to CGPA
lst_obj.sort(key = lambda self: self.cgpa, reverse = True)

num_comp = int(input('Enter the Number of Companies: \n'))
for i in range(num_comp):
    name_comp = input(f'Enter name of Company {i+1}: \n')
    grade_comp = float(input(f'Enter required CGPA of {i+1}: \n'))
    branches_comp = [x for x in input(f'Enter space separated Branches of Company {i+1}: ').split()]
    positions_comp = int(input(f'Enter number of Positions open for Company {i+1}: \n'))    
    company_obj = Company(name_comp, grade_comp, branches_comp, positions_comp)
    for i in range(len(lst_obj)):
        if lst_obj[i].isEligible(company_obj):
            lst_obj[i].Apply(company_obj)
        else:
            pass
    company_obj.hireStudents()