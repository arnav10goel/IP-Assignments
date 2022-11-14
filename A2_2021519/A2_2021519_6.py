#2
def alternate_traversal(matrix):
    for i in range(len(matrix)):
        if (i+1)%2 == 0:
            for j in range(-1, -len(matrix[i])-1, -1):
                print(matrix[i][j], end = ' ')   
        else:
            for j in range(len(matrix[i])):
                print(matrix[i][j], end = ' ')
#1
def normal_traversal(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end = ' ')

#4
def boundary_traversal(matrix):
    for i in matrix[0]:
        print(i, end = ' ')
    for i in range(1, len(matrix)-1):
        print(matrix[i][-1], end = ' ')
    for i in range(-1, -len(matrix[len(matrix)-1])-1, -1):
        print(matrix[len(matrix)-1][i], end = ' ')
    for i in range(len(matrix)-2, 0, -1):
        print(matrix[i][0], end = ' ')

#3 - We use Boundary_travseral recursively for spiral.
def spiral_traversal(matrix):
    while len(matrix) > 1:
        boundary_traversal(matrix)
        matrix.remove(matrix[0])
        matrix.remove(matrix[-1])
        for i in matrix:
            i.remove(i[0])
            i.remove(i[-1])


#5 - We use sum of indexes being constant for right diagonal elements.
def diagonal_rl(matrix):
    freq = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            freq[matrix[i][j]] = i+j

    for k in range(2*n - 1):
        for (x,y) in freq.items():
            if k == y:
                print(x, end = ' ')

#6 - We use difference of indexes being constant for left diagonal elements.
def diagonal_lr(matrix):
    freq2 = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            freq2[matrix[i][j]] = j-i
    
    for k in range(n-1, -n, -1):
        for (x,y) in freq2.items():
            if k == y:
                print(x, end = ' ')

while True:
    print("\n***************************------MATRIX OPERATIONS-----**************************")
    print("Menu: ")
    print("1. Normal Traversal")
    print("2. Alternating Traversal")  
    print("3. Spiral Traversal")  
    print("4. Boundary Traversal")  
    print("5. Right to Left Diagonal Traversal")    
    print("6. Left to Right Diagonal Traversal") 
    print("7. Exit") 
    a = int(input("Pick a number (1/2/3/4/5/6) for the operation you want to perform on the matrix you inputted. Type in 7 if you want to exit the program "))
    if a == 1:
        n = int(input("What is the order of your Matrix?: "))
        matrix = []
        for i in range(n):
            matrix.append([float(i) for i in input("Enter your matrix entries row-wise: ").split()])
        normal_traversal(matrix)
        print(matrix)
    elif a == 2:
        n = int(input("What is the order of your Matrix?: "))
        matrix = []
        for i in range(n):
            matrix.append([float(i) for i in input("Enter your matrix entries row-wise: ").split()])
        alternate_traversal(matrix)
    elif a == 3:
        n = int(input("What is the order of your Matrix?: "))
        matrix = []
        for i in range(n):
            matrix.append([float(i) for i in input("Enter your matrix entries row-wise: ").split()])
        spiral_traversal(matrix)

        #Using boundary traversal recursively was creating problem when matrix had odd number of elements because of a single element being left in the end in case of odd numbered matrices.
        #Therefor this conditional has to be added too to handle this error.
        if (n % 2) != 0:
            for ele in matrix:
                for j in ele:    
                    print(j, end = ' ')
    elif a == 4:
        n = int(input("What is the order of your Matrix?: "))
        matrix = []
        for i in range(n):
            matrix.append([float(i) for i in input("Enter your matrix entries row-wise: ").split()])
        boundary_traversal(matrix)
    elif a == 5:
        n = int(input("What is the order of your Matrix?: "))
        matrix = []
        for i in range(n):
            matrix.append([float(i) for i in input("Enter your matrix entries row-wise: ").split()])
        diagonal_rl(matrix)
    elif a == 6:
        n = int(input("What is the order of your Matrix?: "))
        matrix = []
        for i in range(n):
            matrix.append([float(i) for i in input("Enter your matrix entries row-wise: ").split()])
        diagonal_lr(matrix)
    elif a == 7:
        break
    else:
        print("You need to type in a number between 1 and 7 (inclusive). Typing anything else will cause this message to reappear.")