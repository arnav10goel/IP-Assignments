#Function for Finding Reverse
def getReverse(n):
    lst = []
    while n != 0:
        lst.append(n % 10)
        n = n//10
    num = 0    
    for i in range(len(lst)):
        num += (10**(len(lst) - i -1) * lst[i])
    #int function has been added to the num variable to remove any trailing zeroes in the case of reverse.
    return int(num) 

#Function for checking Palindrome:
def checkPalindrome(n):
    rev = getReverse(n)
    if rev == n:
        return True
    else:
        return False

#Function for Checking Narcissistic Number:
#2 Functions need to be defined before to allow for n to be put in conditional as n is overwritten by the While Loops
def NumDigits(n):
    num = 0
    while n != 0:
        n = n//10
        num += 1
    return num 

def Narcissistic(n):
    num = NumDigits(n)
    sum = 0
    while n != 0:
        sum += (n%10)**(num)  
        n = n//10
    return sum    

def checkNarcissistic(n):
    sum = Narcissistic(n)
    if sum == n:
        return True
    else:
        return False

#Function for Sum:
def findDigitSum(n):
    sum = 0
    while n != 0:
        sum += n%10
        n = n//10
    
    if NumDigits(sum) == 1:
        return sum     
    else:
        sum += findDigitSum(sum) 
    return sum     

#Sum of Squares
def findSquareDigitSum(n):
    sum = 0
    while n != 0:
        sum += (n%10)**2
        n = n//10
    
    if NumDigits(sum) == 1:
        return sum     
    else:
        sum += findSquareDigitSum(sum) 
    return sum  

while True:
    print("Hello User, Welcome to the Application. Please select one of the following operations:")  
    print("1. Find reverse of a number")
    print("2. Check whether a number is a palindrome or not.")
    print("3. Check whether a number is a Narcissistic number or not")
    print("4. Find the sum of digits of a number")
    print("5. Find the sum of squares of digits of a number.")
    print("6. Select 6 to exit the application.")
    a = int(input("Choose the serial number according to whatever operation you wanna perform: (1/2/3/4/5/6)?"))
    if a == 1:
        n = int(input("Enter the number you want to perform the operation on: "))
        print("The reverse of",n, "is", getReverse(n))
    elif a == 2:
        n = int(input("Enter the number you want to perform the operation on: "))
        print(checkPalindrome(n))   
    elif a==3:
        n = int(input("Enter the number you want to perform the operation on: "))
        print(checkNarcissistic(n)) 
    elif a == 4:
        n = int(input("Enter the number you want to perform the operation on: "))
        print(findDigitSum(n), "is the required sum of digits.")   
    elif a==5:
        n = int(input("Enter the number you want to perform the operation on: "))
        print(findSquareDigitSum(n), "is the  required sum of square of digits.")     
    elif a==6:
        print("Program Ended")
        break

    
