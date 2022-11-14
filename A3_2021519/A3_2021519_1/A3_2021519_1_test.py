import A3_2021519_1_functions as func

def test_matmul(A, B, true_C):
    try:
        assert func.matmul(A,B) == true_C
        return True
    except:
        return False

def test_scale(x, y, z, sx, sy, sz, true_x, true_y, true_z):
    try:
        func.scaling(x,y,z,sx,sy,sz)
        assert (x == true_x) and (y == true_y) and (z == true_z)
        return True
    except:
        return False

def test_translate(x, y, z, tx, ty, tz, true_x, true_y, true_z):
    try:
        func.translation(x,y,z,tx,ty,tz)
        assert (x == true_x) and (y == true_y) and (z == true_z)
        return True
    except:
        return False

def test_rotate(x, y, z, axis, phi, true_x, true_y, true_z):
    try:
        func.rotation(x,y,z,axis,phi)
        assert (x == true_x) and (y == true_y) and (z == true_z)
        return True
    except:
        return False

while True:
    print("--------------*****------------------")
    print("Welcome")
    print("Which of the following programs would you like to test?: ")
    print('1. Matrix Multiplication')
    print('2. Scaling')
    print('3. Translating')
    print('4. Rotating')
    print('5. Exit')
    n = int(input('Choose a number (1/2/3/4/5) for the Operation you want to Perform: '))
    if n == 1:
        RA = int(input('How many Rows in your Matrix A? '))
        CA = int(input('How many Columns in your Matrix A? '))
        A = []
        RB = int(input('How many Rows in your Matrix B? '))
        CB = int(input('How many Columns in your Matrix B? '))
        B = []
        if CA != RB:
            print('Matrix Multiplication is not Possible.')
        else:
            for i in range(RA):
                resA = [float(i) for i in input('Enter the elements of Matrix A Row-Wise as Space Separated Numbers: ').split()]
                A.append(resA)

            for i in range(RB):
                resB = [float(i) for i in input('Enter the elements of Matrix B Row-Wise as Space Separated Numbers: ').split()]
                B.append(resB)
            Row_C = RA
            Col_C = CB
            true_C = []
            for i in range(Row_C):
                resA = [float(i) for i in input('Enter the elements of the answer of Matrix formed by A.B Row-Wise as Space Separated Numbers: ').split()]
                true_C.append(resA)
            
            print(test_matmul(A, B, true_C))

    elif n == 2:
        x = [float(i) for i in input('Input all your X-coordinates as Space Separated Numbers: ').split()]
        y = [float(i) for i in input('Input all your Y-coordinates as Space Separated Numbers: ').split()]
        z = [float(i) for i in input('Input all your Z-coordinates as Space Separated Numbers: ').split()]
        sx = float(input('Input your value for sx: '))
        sy = float(input('Input your value for sy: '))
        sz = float(input('Input your value for sz: '))
        true_x = [float(i) for i in input('Input your answer of the Scaled X-Coordinates as Space Separated Numbers: ').split()]
        true_y = [float(i) for i in input('Input your answer of the Scaled Y-Coordinates as Space Separated Numbers: ').split()]
        true_z = [float(i) for i in input('Input your answer of the Scaled Z-Coordinates as Space Separated Numbers: ').split()]
        print(test_scale(x, y, z, sx, sy, sz, true_x, true_y, true_z))

    elif n == 3:
        x = [float(i) for i in input('Input all your X-coordinates as Space Separated Numbers: ').split()]
        y = [float(i) for i in input('Input all your Y-coordinates as Space Separated Numbers: ').split()]
        z = [float(i) for i in input('Input all your Z-coordinates as Space Separated Numbers: ').split()]
        tx = float(input('Input your value for tx: '))
        ty = float(input('Input your value for ty: '))
        tz = float(input('Input your value for tz: '))
        true_x = [float(i) for i in input('Input your answer of the Scaled X-Coordinates as Space Separated Numbers: ').split()]
        true_y = [float(i) for i in input('Input your answer of the Scaled Y-Coordinates as Space Separated Numbers: ').split()]
        true_z = [float(i) for i in input('Input your answer of the Scaled Z-Coordinates as Space Separated Numbers: ').split()]
        print(test_translate(x, y, z, tx, ty, tz, true_x, true_y, true_z))

    elif n == 4:
        x = [float(i) for i in input('Input all your X-coordinates as Space Separated Numbers: ').split()]
        y = [float(i) for i in input('Input all your Y-coordinates as Space Separated Numbers: ').split()]
        z = [float(i) for i in input('Input all your Z-coordinates as Space Separated Numbers: ').split()]
        axis = input('Input the Axis for the Rotation to be Performed About (x/y/z): ')
        axis.lower()
        phi = float(input('Input your Angle in Radians: '))
        true_x = [float(i) for i in input('Input your answer of the Scaled X-Coordinates as Space Separated Numbers upto 2 Decimal Points: ').split()]
        true_y = [float(i) for i in input('Input your answer of the Scaled Y-Coordinates as Space Separated Numbers upto 2 Decimal Points: ').split()]
        true_z = [float(i) for i in input('Input your answer of the Scaled Z-Coordinates as Space Separated Numbers upto 2 Decimal Points: ').split()]
        print(test_rotate(x, y, z, axis, phi, true_x, true_y, true_z))
    
    elif n == 5:
        print('Program Ended')
        break

    else:
        print('Enter Integer only from 1 to 5')