import math
n = int(input("No of vertices in your 3D Shape: "))
x = [float(i) for i in input("Enter the X-coordinates of the vertices WITH spaces: ").split()]
y = [float(i) for i in input("Enter the Y-coordinates of the vertices WITH spaces: ").split()]
z = [float(i) for i in input("Enter the Z-coordinates of the vertices WITH spaces: ").split()]

if len(x) != n or len(y) != n or len(z) != n:
    print("Error your input for no of vertices and coordinates does not match.")
else:
    f = open('./A2_2021519_2/Q2_input_output.txt', 'w')
    f.write(f'The original X-coordinates are: {x}')
    f.write(f'\nThe original Y-coordinates are: {y}')
    f.write(f'\nThe original Z-coordinates are: {z}')

    f.close()

    q = int(input("How many transformation queries do you want to perform? "))
    queries = []
    for i in range(q):
        queries.append([i for i in input("""Queries are of three types:- (S sx sy sz)
                             (T tx ty tz)
                             (R axis & angle). What's yours? Enter entries with SPACES: """).split()])
    """ We give the user 3 types of queries here and in case he makes a fault that query will not be accepted for the transformation 
        It would also be printed out which query hasn't been included in the transformation as it is not like any of the three."""

    def scaling(x,y,z,queries,i):
        sx = float(queries[i][1])
        sy = float(queries[i][2])
        sz = float(queries[i][3])
        for k in range(len(x)):
            x[k] = (x[k]*sx)
        for k in range(len(y)):
            y[k] = (y[k]*sy)
        for k in range(len(z)):
            z[k] = (z[k]*sz)

    def translation(x,y,z,queries,i):
        tx = float(queries[i][1])
        ty = float(queries[i][2])
        tz = float(queries[i][3])
        for k in range(len(x)):
            x[k] = (x[k]+tx)
        for k in range(len(y)):
            y[k] = (y[k]+ty)
        for k in range(len(z)):
            z[k] = (z[k]+tz)

    def rotation(x,y,z,queries,i):
        axis = queries[i][1]
        angle = float(queries[i][2]) #Assuming angle to be in radians
        axis.lower()
        if axis == 'x':
            for k in range(len(y)):
                y[k] = ((y[k]*math.cos(angle))-(z[k]*math.sin(angle)))
            for k in range(len(z)):
                z[k] = ((y[k]*math.sin(angle))+(z[k]*math.cos(angle)))
        elif axis == 'y':
            for k in range(len(x)):
                x[k] = (x[k]*math.cos(angle))+(z[k]*math.sin(angle))
            for k in range(len(z)):
                z[k] = (z[k]*math.cos(angle))-(x[k]*math.sin(angle))
        elif axis == 'z':
            for k in range(len(x)):
                x[k] = ((x[k]*math.cos(angle))-(y[k]*math.sin(angle)))
            for k in range(len(x)):
                x[k] = ((y[k]*math.cos(angle))+(x[k]*math.sin(angle)))    
        else:
            print(f"{queries[i]} is incorrect and can't be used to perform a transformation.")
            pass

    for i in range(len(queries)):
        if queries[i][0] == 'S':
            scaling(x,y,z,queries,i)
        elif queries[i][0] == 'T':
            translation(x,y,z,queries,i)
        elif queries[i][0] == 'R':
            rotation(x,y,z,queries,i)
        else:
            print(f"{queries[i]} is incorrect and can't be used to perform a transformation")

    f = open('./A2_2021519_2/Q2_input_output.txt', 'a')
    f.write(f'\nThe transformed X-coordinates of the vertices are: {x}')
    f.write(f'\nThe transformed Y-coordinates of the vertices are: {y}')
    f.write(f'\nThe transformed Z-coordinates of the vertices are: {z}')

    f.close()