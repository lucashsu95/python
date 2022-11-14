Lnum = input()
zero,one = 0,0
zero_max = []
one_max = []
for i in Lnum:

    zero = zero+1 if i == '0' else 0
    one = one+1 if i == '1' else 0
    zero_max.append(zero)
    one_max.append(one)
print(abs(max(zero_max) - max(one_max)))