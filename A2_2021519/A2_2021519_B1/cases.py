def lengthStr(string):
    sum = 0
    for i in string:
        sum += 1
    return sum

def generateData():
    n = int(input("How many inputs do you wanna give? "))
    for i in range(n):
        str_input = input("Input the string you want the length of: ")
        filename1 = './A2_2021519_B1/Input_' + str(i+1)
        f1 = open(filename1, 'w')
        f1.write(str(str_input))
        f1.close()
        filename2 = './A2_2021519_B1/Output_' + str(i+1)
        f2 = open(filename2, 'w')
        f2.write(str(lengthStr(str_input)))
        f2.close()


generateData()   