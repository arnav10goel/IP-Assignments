print("---------------------------------Hello, Welcome to Delhi Days---------------------------------")
print()
a = int(input("Price of Item 1: "))
b = int(input("Price of Item 2: "))
c = int(input("Price of Item 3: "))

print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
print()
print()
print()
print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

def NumDigits(n):
    num = 0
    while n != 0:
        n = n//10
        num += 1
    return num 

while True:
    p1 = float(input("Provide discount(in percentage) for the 1st saver combo: "))
    p2 = float(input("Provide discount(in percentage) for the 2nd saver combo: "))
    p3 = float(input("Provide discount(in percentage) for the 3rd saver combo: "))
    if (NumDigits(p1) or NumDigits(p2) or NumDigits(p3)) > 2.0:
        print("Discounts must be 2 digits smarty pants.")
        pass
    else:
        break

print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*") 

print()
while True:
    phone = int(input("Provide your 10 digit contact number: "))
    if NumDigits(phone) != 10:
        print("Phone Number needs to be 10 digit.")
        pass
    else:
        break

print("The resulting catalogue is: ") 
print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*") 
print()
print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*") 
print("Delhi Days") 
print("R-Block, Model Town 3")  
print("Delhi: 110009")

print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
print()
print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*") 
print("Item                           Price (per pack)")
print("|                              |")
print("Item 1                        ", a)
print("Item 2                        ", b)
print("Item 3                        ", c)
combopack1 = (a+b)*(1-(p1/100))
combopack2 = (b+c)*(1-(p2/100))
combopack3 = (c+a)*(1-(p3/100))
supersaver = (a+b+c)*(0.72)
print("ComboPack1:                   ", combopack1)
print("ComboPack2:                   ", combopack2)
print("ComboPack3:                   ", combopack3)
print("SuperSaver:                   ", supersaver)
print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
print()
print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*") 
print()
print("For home delivery, contact here: 9876543210")