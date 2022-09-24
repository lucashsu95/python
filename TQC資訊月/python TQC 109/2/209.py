#209 距離判斷
import math
point = int(input())
point2 = int(input())
if math.sqrt((point - 5) ** 2 + (point2 - 6) ** 2 )<= 15:
    print('Inside')
else:
    print('Outside')