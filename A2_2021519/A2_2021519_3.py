#This function assigns characters to the corresponding character and base using UNICODE values.
def valueinp(char):
    if char >= '0' and char <= '9':
        return ord(char) - ord('0')
    else:
        return ord(char) - ord('A') + 10

#This function converts the given number to its decimal form by using chrs from above function.
def AnybasetoDeci(str,base):
    lenofin = len(str)
    power = 1 
    num = 0     
    for i in range(lenofin - 1, -1, -1):
        num += valueinp(str[i]) * power
        power = power * base
    return num

#This functions converts any number input to its characters again using UNICODE values.    
def reValueinp(num): 
    if (num >= 0 and num <= 9):
        return chr(num + ord('0'))
    else:
        return chr(num - 10 + ord('A'))

#Uses reValueinp to convert fromm decimal to target base.
def fromDeci(result, base, inputNum): 
    index = 0; # Initialize index of result
    while (inputNum > 0):
        result+= reValueinp(inputNum % base)
        inputNum = int(inputNum / base)
    result = result[::-1]
    return result

#This function checks the validity of the user's input and if valid performs the CONVERSION operation.
def input_validity(srcbase,tarbase,strr):
    for i in strr:
        if i.isdigit():
            if int(i) >= srcbase:
                return "Number does not exist in the mentioned Base."
        elif i.isalpha():
            if ord(i.upper())-55 >= srcbase:
                return "Number does not exist in the mentioned Base."
    answerhold = AnybasetoDeci(strr, srcbase)
    inputNum = answerhold
    result = " "
    return "Equivalent of " + str(strr) + " in Base " + str(tarbase) + " is " + str(fromDeci(result, tarbase, inputNum))

while True:
    print("\n*-*-*-*-*-*-*-*-*-*-WELCOME TO NUMBER SYSTEMS CONVERTOR-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("1. Convert Decimal to Binary")
    print("2. Convert Decimal to HexaDecimal")
    print("3. Convert Decimal to Octal")
    print("4. Convert Binary to HexaDecimal")
    print("5. Convert Binary to Octal")
    print("6. Convert HexaDecimal to Octal")
    print("7. Convert Binary to Decimal")
    print("8. Convert HexaDecimal to Decimal")
    print("9. Convert Octal to Decimal")
    print("10. Convert HexaDecimal to Binary")
    print("11. Convert Octal to Binary")
    print("12. Convert Octal to HexaDecimal")
    print("13. Universal Number System Converter")
    print("14. Exit")
    user_choice = int(input("Choose a number (1-14) for the operation you want to perform: "))
    if user_choice == 1:
        strr = input("Enter your number here: ")
        srcbase = 10
        tarbase = 2
        print(input_validity(srcbase,tarbase,strr))
    elif user_choice == 2:
        strr = input("Enter your number here: ")
        srcbase = 10
        tarbase = 16
        print(input_validity(srcbase,tarbase,strr))
    elif user_choice == 3:
        strr = input("Enter your number here: ")
        srcbase = 10
        tarbase = 8
        print(input_validity(srcbase,tarbase,strr))
    elif user_choice == 4:
        strr = input("Enter your number here: ")
        srcbase = 2
        tarbase = 16
        print(input_validity(srcbase,tarbase,strr))
    elif user_choice == 5:
        strr = input("Enter your number here: ")
        srcbase = 2
        tarbase = 8
        print(input_validity(srcbase,tarbase,strr))
    elif user_choice == 6:
        strr = input("Enter your number here: ")
        srcbase = 16
        tarbase = 8
        print(input_validity(srcbase,tarbase,strr))
    elif user_choice == 7:
        strr = input("Enter your number here: ")
        srcbase = 2
        tarbase = 10
        print(input_validity(srcbase,tarbase,strr))
    elif user_choice == 8:
        strr = input("Enter your number here: ")
        srcbase = 16
        tarbase = 10
        print(input_validity(srcbase,tarbase,strr))
    elif user_choice == 9:
        strr = input("Enter your number here: ")
        srcbase = 8
        tarbase = 10
        print(input_validity(srcbase,tarbase,strr))
    elif user_choice == 10:
        strr = input("Enter your number here: ")
        srcbase = 16
        tarbase = 2
        print(input_validity(srcbase,tarbase,strr))
    elif user_choice == 11:
        strr = input("Enter your number here: ")
        srcbase = 8
        tarbase = 2
        print(input_validity(srcbase,tarbase,strr))
    elif user_choice == 12:
        strr = input("Enter your number here: ")
        srcbase = 8
        tarbase = 16
        print(input_validity(srcbase,tarbase,strr))
    elif user_choice == 13:
        strr = input("Enter your number here: ")
        srcbase = input("Enter the Source Base(A) : ")
        tarbase = input("Enter the Target Base(B) you want to change to: ")
        if srcbase.isdigit() and tarbase.isdigit():
            print(input_validity(int(srcbase), int(tarbase), strr))
        else:
            print("RETRY, No such Base/Radix exists.")     
    elif user_choice == 14:
        print("Program Ended")
        break
    else:
        print("\nChoose from 1-14 only.")