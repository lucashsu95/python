#TA001 噁爛數
n = int(input())
# for i in list(map(int,n.split(' '))):

while n % 2 == 0:
    n/=2
while n%3 == 0:
    n/=3
while n%5 == 0:
    n/=5
if n == 1:
    print('True')
else:
    print('False')
