#301 迴圈整數連加
start = int(input())
end = int(input())
total = 0
for i in range(start,end+1):
    total += i
print(total)