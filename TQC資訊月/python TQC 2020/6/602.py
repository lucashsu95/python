#602 撲克牌總和
ary = []
card = ['J','Q','K','A']
cardValue = ['11','12','13','1']
for i in range(5):
    num = input()
    for j in range(len(card)):
        if num == card[j]:
            num = cardValue[j]
    ary.append(int(num))
print(sum(ary))       
