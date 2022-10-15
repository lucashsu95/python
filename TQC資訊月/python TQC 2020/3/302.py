#302 迴圈偶數連加
start = int(input())
end = int(input())
total = 0
for i in range(start,end+1):
    if i % 2 == 0:
        total += i
print(total)