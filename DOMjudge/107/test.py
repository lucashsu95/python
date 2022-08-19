data = input().split()
for i in range(len(data)):
    data[i] = data[i][::-1]
print(' '.join(data))