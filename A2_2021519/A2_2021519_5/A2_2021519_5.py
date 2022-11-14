music_ref = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

music_dic = {1: 'C', 2: 'C#', 3: 'D', 4: 'D#', 5: 'E', 6: 'F', 7: 'F#', 8: 'G', 9: 'G#', 10: 'A', 11: 'A#', 12: 'B'}

def notes(root_note):
    lst = []
    for i in range(len(music_ref)):
        if music_ref[i] >= root_note:
            lst.append(music_ref[i])
    for j in music_ref:
        if j not in lst:
            lst.append(j)
    lst.append(root_note + "'")
    return lst

def major(root):
    #Root W W H W W W H = major
    res = [root]
    major = ['W', 'W', 'H', 'W', 'W', 'W', 'H']
    lst = notes(root)
    j = 0
    for i in range(len(major)):
        if major[i] == 'W':
            j += 2
            res.append(lst[j])
        else:
            j += 1
            res.append(lst[j])
    return res

def minor(root):
    #Root W H W W H W W = minor
    res = [root]
    major = ['W', 'H', 'W', 'W', 'H', 'W', 'W']
    lst = notes(root)
    j = 0
    for i in range(len(major)):
        if major[i] == 'W':
            j += 2
            res.append(lst[j])
        else:
            j += 1
            res.append(lst[j])
    return res

def noteCreate():
    filename1 = './A2_2021519_5/scaleMajor.txt'
    filename2 = './A2_2021519_5/scaleMinor.txt'
    f1 = open(filename1, 'w')
    f2 = open(filename2, 'w')
    f1.write(', '.join(major(music_dic[1])))
    f2.write(', '.join(minor(music_dic[1])))
    for i in range(2,13):
        f1.write('\n'+', '.join(major(music_dic[i])))
        f2.write('\n'+', '.join(minor(music_dic[i])))
    f1.close()
    f2.close()

noteCreate() #Calling this function creates the 2 required text files which has all the Major and Minor Notes for all Root Notes.

#The two functions below read the respective of the 2 text files created and print out the Major/Minor Note for the Root Note inputted by the user.

def majorNotes(root):
    filename1 = './A2_2021519_5/scaleMajor.txt'
    f1 = open(filename1, 'r')
    data = f1.readlines()
    f1.close()
    lines = [i.strip() for i in data]
    for i in lines:
        if i[0] == root:
            return i

def minorNotes(root):
    filename1 = './A2_2021519_5/scaleMinor.txt'
    f1 = open(filename1, 'r')
    data = f1.readlines()
    f1.close()
    lines = [i.strip() for i in data]
    for i in lines:
        if i[0] == root:
            return i

while True:
    print("\n*-*-*-*-*-*-*-*-*-*-WELCOME TO MUSIC THEORY-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("1. Type 1 to continue")
    print("2. Type 2 to Exit")
    n = int(input("(1/2): "))
    if n == 1:
        root_note = input("Enter Root Note in Capitals: ")
        if root_note not in list(music_dic.values()):
            print("This Root is not found. Please try again.")
        else:
            scale = input("Enter the type of scale (Major/Minor): ")
            s = scale.lower()
            if s == 'major':
                print(f'The {scale} scale in the key of {root_note} is: ' + majorNotes(root_note))
            elif s == 'minor':
                print(f'The {scale} scale in the key of {root_note} is: ' + minorNotes(root_note))
            else:
                print("Please choose between Major and Minor")
    elif n == 2:
        break
    else:
        print("Type (1/2)")