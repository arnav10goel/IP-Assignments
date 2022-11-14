fname = './A2_2021519_1/question1_input.txt'

f = open(fname, 'r')
data = f.readlines()
lines = [i.strip() for i in data]

f.close()
#Word Count of a Specific Word by finding it in the List made by reading the Input File
def wordcount():
    num = 0
    s = input("Enter Word: ")
    for i in range(len(lines)):
        lst = lines[i].split()
        if s in lst:
            num += 1

    print(f'Word Count: {num}')

#Printing all Unique Words by checking if a word already exists in the Main List of all words or not.
def unique_words():
    res = []
    for i in range(len(lines)):
        lst = lines[i].split()
        for j in lst:
            res.append(j)
    ans = []        
    for i in res:
        if i in ans:
            pass
        else:
            ans.append(i)
    for i in ans:
        print(i, end = ' ; ')

#Keeping a count of all words by using a Dictionary
def word_counts():
    freq = {}
    res = []
    for i in lines:
        lst = [x for x in i.split()]
        for j in lst:
            res.append(j)

    for x in res:
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1
    print("Word Counts: ")
    for a,b in list(freq.items()):
        print(f'{a} :  {b}')

#Using List Indexing to replace words in the main Input Text File and rewriting that file to reflect that change PERMANENTLY.
def replace_word():
    comp = [i.split() for i in lines]
    word1 = input("What word do you want to replace in the text? ")
    word2 = input("What word do you want to replace it with in the text? ")
    for j in range(len(comp)):
        for i in range(len(comp[j])):
            if comp[j][i] == word1:
                comp[j][i] = word2
    f2 = open(fname, 'w')
    f2.write(' '.join(comp[0]))
    for i in range(1,len(comp)):
        f2.write('\n'+' '.join(comp[i]))
    f2.close()

while True:
    print("\n-------------------------------------------------------------------------------------------------------")
    print("                                         WELCOME TO WORDPLAY                                 ")
    print("Pick a number (1/2/3/4) for the corresponding operation you want to perform. Enter 5 if you want to quit.")
    print("1. Display specific word count")
    print("2. Display all Unique Words")
    print("3. Display all Word Counts")
    print("4. Replace Words")
    print("5. Quit")
    num = input("Your choice: ")
    if not num.isdigit():
        print("You need to type in an integer between 1-5 (both inclusive).")
    else:
        num = int(num)
        if num == 1:
            wordcount()
        elif num == 2:
            unique_words()
        elif num == 3:
            word_counts()
        elif num == 4:
            replace_word()
        elif num == 5:
            print("Program Ended")
            break
        else:
            print("You need to type in an integer between 1-5 (both inclusive).")