def calculate_area(l,a,b,d):
    #Local Function for the Polynomial
    def fn(x):
        func = 0
        for i in l:
            func += x ** i
        return func

    #Calculate the Integrand:
    integrand = 0
    if a>b:
        return "Lower Bound cannot be Greater than Upper Bound"
    else:    
        if (b-a) % d == 0:
            for i in range(a,b,d):
                integrand += (d/6)*(fn(i) + 4*fn((2*i + d)/2) + fn(i + d))
        else:
            return "Cannot apply Simpson's Algorithm for this combination of Bounds and Common Difference(d). b-a) must be divisible by d for the algorithm to be applicable."
    return integrand  

a = int(input("Lower Bound of Integration(a): "))
b = int(input("Upper Bound of Integration(b): "))
d = int(input("Common Difference for Simpson's Algorithm, remember that (b-a) must be divisble by this input of yours: "))
l = list(map(float, input("With spaces enter the exponents of the variables in your polynomial. Order does not matter, just all exponents must be written WITH spaces in one line:- ").split()))
print(calculate_area(l,a,b,d))               