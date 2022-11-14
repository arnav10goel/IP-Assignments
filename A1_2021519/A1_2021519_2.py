#Square Function
def square(s):
    print("Perimeter:", 4*s)
    print("Area:", s**2)

#Rectangle Function
def rectangle(l,b):
    print("Perimeter:", 2*(l+b))
    print("Area:", l*b)

#Rhombus Function
def rhombus(a, d1, d2):
    print("Perimeter:", 4*a)
    print("Area:", (d1*d2)/2)        

#Parallelogram Function
def pllgm(l,b,h):
    print("Perimeter:", 2*(l+b))
    b = True
    while b:
        a = input("What does the height correspond to: Type (l/b)?")
        a = a.lower()
        if a == 'l':
            print("Area:", l*h)
            b = False   
        elif a == 'b':
            print("Area:", b*h)
            b = False  
        else:
            print("Type (l/b) only") 

#Circle Function
def Circle(r):
    print("Circumference is: ", 2*3.142*r) #pi is taken as (3.142) everywhere
    print("Area: ", r*3.142*r)

#Cube Function
def Cube(a):
    print("CSA is: ", 4*a*a)
    print("TSA is: ", 6*a*a)
    print("Volume is: ", a*a*a)

#Cuboid Function
def Cuboid(l,b,h):
    print("CSA is: ", 2*(l*h + b*h))
    print("TSA is: ", 2*(l*h + b*h + l*b))
    print("Volume is: ", l*b*h)

#Right Circular Function
def RightCircCone(l,r,h):
    print("CSA is: ", 2*3.142*r*l)
    print("TSA is: ", 3.142*r*(2*l + r))
    print("Volume is: ", (1/3)*(3.142)*r*r*h)

#Hemisphere Function
def Hemisphere(r):
    print("CSA is: ", 2*3.142*r*r)
    print("TSA is: ", 3*3.142*r*r)
    print("Volume is: ", (2/3)*3.142*r*r*r) 

#Sphere Function
def Sphere(r):
    print("CSA is: ", 4*3.142*r*r)
    print("TSA is: ", 4*3.142*r*r)
    print("Volume is: ", (4/3)*3.142*r*r*r) 

#Solid Cylinder Function
def SolidCylinder(r,h):
    print("CSA is: ", 2*3.142*r*h)
    print("TSA is: ", (2*3.142*r*h)+(2*3.142*r*r))
    print("Volume is: ", 3.142*r*r*h) 

#Hollow Cylinder Function
def HollowCylinder(r1,r2,h):
    print("CSA is: ", 2*3.142*h*(r1+r2))
    print("TSA is: ", 2*3.142*h*(r1+r2) + 2*3.142*(abs((r1*r1)-(r2*r2))))
    print("Volume is: ", 3.142*h*(abs(r1*r1 - r2*r2)))

#Menu Program for Various Shapes
n = int(input("No of students in the class: "))    
for i in range(n):
    dim = input("What is the type of your Shape? (2D/3D) or type the number 13 if you want to pass your chance:")
    dim.lower()
    if dim == '2d':
        print("Here are the 2-Dimensional Shapes you can choose from:")
        print("1. Square")
        print("2. Rectangle")
        print("3. Rhombus")
        print("4. Parallelogram")
        print("5. Circle")
        num = int(input("Choose the correct number according to the shape you want: (1/2/3/4/5) "))
        if num == 1:
            s = float(input("Side of the square?"))
            square(s)            
        elif num ==2:
            l = float(input("Length of the Rectangle?"))   
            b = float(input("Breadth of the Rectangle?"))
            rectangle(l,b)
            
        elif num == 3:
            a = float(input("Side of the Rhombus?"))    
            d1 = float(input("1st Diagonal of the Rhombus?"))
            d2 = float(input("2nd Diagonal of the Rhombus?"))
            rhombus(a, d1, d2)
            
        elif num == 4:
            l = float(input("Length of Parallelogram: "))
            b = float(input("Breadth of Parallelogram: "))
            h = float(input("Height of Parallelogram: "))
            pllgm(l,b,h)
            
        elif num == 5:
            r = float(input("Radius of Circle: "))  
            Circle(r)
            
        else:
            print("You need to choose a number between 1 and 5 (both inclusive)")
                
                    

    elif dim == '3d':
        print("Here are the 3-Dimensional Shapes you can choose from:")
        print("6. Cube")
        print("7. Cuboid")
        print("8. Right Circular Cone")
        print("9. Hemisphere")
        print("10. Sphere")
        print("11. Solid Cylinder")
        print("12. Hollow Cylinder")
       
        num = float(input("Choose the correct number according to the shape you want: (6/7/8/9/10/11/12) "))
        if num == 6:
            s = float(input("Side of the cube?"))
            Cube(s)
                
        elif num == 7:
            l = float(input("Length of the Cuboid?"))   
            b = float(input("Breadth of the Cuboid?"))
            h = float(input("Height of the Cuboid?"))
            Cuboid(l,b,h)
                
        elif num == 8:
            l = float(input("Slant height of the Right Circular Cone?"))    
            r = float(input("Radius of the Right Circular Cone?"))
            h = float(input("Height of the Right Circular Cone?"))
            RightCircCone(l,r,h)
                
        elif num == 9:
            r = float(input("Radius of Hemisphere?"))
            Hemisphere(r)
                
        elif num == 10:
            r = float(input("Radius of Sphere: "))  
            Sphere(r)
                
        elif num == 11:
            r = float(input("Radius of Solid Cylinder: "))
            h = float(input("Height of Solid Cylinder: "))
            SolidCylinder(r,h)
                
        elif num == 12:
            r1 = float(input("floaternal radius of Hollow Cylinder: "))
            r2 = float(input("External radius of Hollow Cylinder: "))
            h = float(input("Height of Hollow Cylinder: "))
            HollowCylinder(r1,r2,h)
        
        else:
            print("You need to choose a number between 6 and 12 (both inclusive)")       
        
    elif dim == 13:
        pass

    else:
        print("You need to choose between 2D and 3D: (2D/3D) or type 13 if you want to not answer and pass.")
                