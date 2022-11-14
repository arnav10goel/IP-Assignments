lst = []
print("Provide the following Details for your Polynomial: ")
degree = int(input("What is the degree of your polynomial?: "))
for i in range(1, (degree+2)):
    lst.append(float(input("What is the coefficient? (Start from the leading coefficient and then all the way to the constant term): ")))

#Bounds need to be Int to use Range
lower = int(input("Int - Lower Bound of x for your Polynomial: "))   
upper = int(input("Int - Upper Bound of x for your Polynomial: "))
inc = int(input("Int - By how much should x increase between the lower and upper bound while we plot the function: "))

for i in range(lower, upper+1, inc):
    a = 0
    
    #This For Loop adds the corresponding value of x in the given range into the function and stores the function output as var 'a'.
    for j in range(len(lst)): 
        a += ((i)**(len(lst)-1-j))*(lst[j]) 
    
    #Absolute function is used so that incase the input is negative, range function can be used for the same number of iterations of '*' 
    final = abs(round(a)) 
    for i in range(final):
        print("*", end = '')
    print("\n")        