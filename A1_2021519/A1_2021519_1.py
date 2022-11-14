def right_angled(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j, end = '')
        print("\n")    

def half_kite(n):
    #This prints the upper part of the half kite till the longest row.
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j, end = '')
        print("\n")
    #This then prints from the 2nd longest row to the smallest to complete half kite.
    for k in range(n-1, 0, -1):
        for l in range(1,k+1):
            print(l, end = '')
        for m in range(k,n):
            print(" ", end = '')
        print("\n") 

def isos_triangle(n):
    for i in range(1,(2*n + 1),2):
        for j in range(1,(2*n + 1-i)//2):
            print(" ", end = '')
        for l in range(1, i+1):
            print(l, end = '')
        print("\n")    

def kite(n):
    #This prints the upper part of the kite till the longest row.
    for i in range(1,(2*n + 1),2):
        for j in range(1,(2*n + 1-i)//2):
            print(" ", end = '')
        for l in range(1, i+1):
            print(l, end = '')
        print("\n") 
    #This prints from the 2nd longest till the shortest.    
    for i in range((2*n - 3), -1, -2):
        for j in range((2*n-1-i)//2):
            print(" ", end = '')
        for k in range(1,i+1):
            print(k, end='')
        print("\n")    

def X(n):
    #This prints the upper portion of the X till the shortest row
    for i in range((2*n - 1), -1, -2):
        for j in range((2*n-1-i)//2):
            print(" ", end = '')
        for k in range(1,i+1):
            print(k, end='')
        print("\n")
    #This then starts from the 2nd shortest row and goes to the longest to complete the X. 
    for i in range(3,(2*n + 1),2):
        for j in range(1,(2*n + 1-i)//2):
            print(" ", end = '')
        for l in range(1, i+1):
            print(l, end = '')
        print("\n")           

while True:
    print("Please choose a pattern among the following")
    print("“Right-angled triangle")
    print("Isosceles triangle")
    print("Kite")
    print("Half Kite")
    print("X")
    print("Type 'Exit' to leave the program")
    pattern = input("Right the name of the pattern you want to print: ")
    pattern.lower() #Whatever be the input this converts it to lower so that there is uniformity for the conditional
    if pattern == 'right-angled triangle':
        n = int(input("Pattern till how many terms? "))
        right_angled(n)
    if pattern == 'isosceles triangle' :
        n = int(input("Pattern till how many terms? "))
        isos_triangle(n)
    if pattern == 'kite':
        n = int(input("Pattern till how many terms? "))
        kite(n)
    if pattern == 'half kite':
        n = int(input("Pattern till how many terms? "))
        half_kite(n)
    if pattern == 'x':
        n = int(input("Pattern till how many terms? "))
        X(n)
    if pattern == 'exit':
        break                    