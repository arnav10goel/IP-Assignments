import cases

def numstr_recursion(string):
    if string:
        length = numstr_recursion(string[1:])
        return 1 + length
    else:
        return 0


def testing():
    n = int(input("How many inputs did you give for testing?: "))
    for i in range(n):
        filename1 = './A2_2021519_B1/Input_' + str(i+1)
        f1 = open(filename1, 'r')
        data = f1.readlines()
        f1.close()

        input_reading = ''.join(data)
        length1 = numstr_recursion(input_reading)

        filename2 = './A2_2021519_B1/Output_' + str(i+1)
        f2 = open(filename2, 'r')
        data2 = f2.readlines()
        f2.close()
        
        length_reading = int(''.join(data2))
        if length_reading != length1:
            return "FAILED"
    return "SUCCESS"

print(testing())