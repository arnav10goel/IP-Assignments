initial_grammy = list(map(int, input("Initial No of Grammys with Doja Dog and DJ Snack: ").split()))
M_N = list(map(int, input("Dimensions of FarmVille: ").split()))
num_tower = M_N[1]
lst = []
for i in range(M_N[0]):
    str_user = input()
    lst.append(list(str_user))

#We make a copy so that the list can be used later and we have a copy incase we need to refer to the original list.
lst2 = lst.copy() 

grammy_Doja = initial_grammy[0]
grammy_DJ = initial_grammy[1]

res = []
i = 0
while i < num_tower:
    sum = 0
    for j in lst:
        if j[i] == '1':
            sum += 1
    res.append(sum)
    i += 1

#We make a copy so that the list can be used later and we have a copy incase we need to refer to the original list.
res2 = res.copy()
score_Doja = 0
score_DJ = 0
nums = []

for num in range(num_tower):
    a = max(res2)
    indx = res.index(a)
    #This conditional is for the case when 2 or more skyscrapers have the same height.
    if a not in nums:
        nums.append(a)
    else:
        res[indx] = False
        indx = res.index(a)
    #This condition takes starting for Doja and goes adding repo points and changing the 1 to the required letter in that order.
    if (num+1) % 2 != 0:
        score_Doja += a*(grammy_Doja)
        for ele in lst2:
            if ele[indx] == '1':
                ele[indx] = 'D'
        res2.remove(a)
    else:
        score_DJ += a*(grammy_DJ)
        for ele in lst2:
            if ele[indx] == '1':
                ele[indx] = 'S'
        res2.remove(a)
    #After every iteration it has been given to us to each win one grammy each.
    grammy_Doja += 1
    grammy_DJ += 1

print("OUTPUT: ")
print(f'{score_Doja} {score_DJ}')
print()
for LST in lst2:
    print(''.join(LST))