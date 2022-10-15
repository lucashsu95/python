x = eval(input())
y = eval(input())
z = eval(input())

ans = z/1.6 / (x*60+y) * 60 *  60 
print(f'Speed = {ans:.1f}')