answerkey = "./A2_2021519_4/Admin/AnswerKey.txt"
registeredstudents = "./A2_2021519_4/Admin/RegisteredStudents.txt"

stu_1 = "./A2_2021519_4/Student/John_1357.txt"
stu_2 = "./A2_2021519_4/Student/Ram_1211.txt"
stu_3 = "./A2_2021519_4/Student/Brock_1000.txt"
stu_4 = "./A2_2021519_4/Student/Misty_372.txt"
stu_5 = "./A2_2021519_4/Student/Ash_12.txt"

f1 = open(stu_1, 'r')
data1 = f1.readlines()
stu1 = [i.split() for i in data1]
f1.close()

f2 = open(stu_2, 'r')
data2 = f2.readlines()
stu2 = [i.split() for i in data2]
f2.close()

f3 = open(stu_3, 'r')
data3 = f3.readlines()
stu3 = [i.split() for i in data3]
f3.close()

f4 = open(stu_4, 'r')
data4 = f4.readlines()
stu4 = [i.split() for i in data4]
f4.close()

f5 = open(stu_5, 'r')
data5 = f5.readlines()
stu5 = [i.split() for i in data5]
f5.close()

f6 = open(answerkey, 'r')
data6 = f6.readlines()
answer_key = [i.split() for i in data6]
f6.close()

score1,score2,score3,score4,score5 = 0,0,0,0,0

#John_1357
for i in range(len(stu1)):
    if stu1[i][1] == answer_key[i][1]:
        score1 += 4
    elif stu1[i][1] == '-':
        score1 += 0
    else:
        score1 += -1

#Ram_1211
for i in range(len(stu2)):
    if stu2[i][1] == answer_key[i][1]:
        score2 += 4
    elif stu2[i][1] == '-':
        score2 += 0
    else:
        score2 += -1

#Brock_1000
for i in range(len(stu3)):
    if stu3[i][1] == answer_key[i][1]:
        score3 += 4
    elif stu3[i][1] == '-':
        score3 += 0
    else:
        score3 += -1

#Misty_372
for i in range(len(stu4)):
    if stu4[i][1] == answer_key[i][1]:
        score4 += 4
    elif stu4[i][1] == '-':
        score4 += 0
    else:
        score4 += -1

#Ash_12
for i in range(len(stu5)):
    if stu5[i][1] == answer_key[i][1]:
        score5 += 4
    elif stu5[i][1] == '-':
        score5 += 0
    else:
        score5 += -1

f7 = open(registeredstudents, 'r')
data7 = f7.readlines()
registered_students = [i.split() for i in data7]
f7.close()

score_1 = []
score_1.append(str(score1))
score_2 = []
score_2.append(str(score2))
score_3 = []
score_3.append(str(score3))
score_4 = []
score_4.append(str(score4))
score_5 = []
score_5.append(str(score5))

registered_students[0] = registered_students[0] + score_1
registered_students[1] = registered_students[1] + score_2
registered_students[2] = registered_students[2] + score_3
registered_students[3] = registered_students[3] + score_4
registered_students[4] = registered_students[4] + score_5

final_file = open("./A2_2021519_4/FinalReport.txt",'w')
final_file.write(' '.join(registered_students[0]))
final_file.write('\n'+(' '.join(registered_students[1])))
final_file.write('\n'+(' '.join(registered_students[2])))
final_file.write('\n'+(' '.join(registered_students[3])))
final_file.write('\n'+(' '.join(registered_students[4])))

final_file.close()