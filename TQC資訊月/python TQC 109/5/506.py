#506 一元二次方式程
import math
def compute(a, b, c):
    if b ** 2 - 4 * a * c >= 0:
        ans1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        ans2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        return ans1, ans2
    else:
        return 0
a = int(input())
b = int(input())
c = int(input())
if compute(a, b, c) != 0:
    ans1, ans2 = compute(a, b, c)
    print('{}, {}' .format(ans1, ans2))
else:
    print('Your equation has no root.')