#TL001 將英文字母轉為小寫
import sys
for data in sys.stdin.read().splitlines():
    print(data.lower())