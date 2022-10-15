#607 成績計算
for i in range(3):
    studentScore = []
    for j in range(5):
        studentScore.append(int(input()))
    print(f'Student {i+1}')
    print(f'#Sum {sum(studentScore)}')
    print(f'#Average {sum(studentScore)/len(studentScore):>.2f}')