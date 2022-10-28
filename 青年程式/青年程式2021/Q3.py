#小明的哨音
import sys
for Ln in sys.stdin.read().splitlines():
    Ln = int(Ln)
    Lcount = 0
    def fun(Lstr,Lv,Lsum): #Lstr:字串的樣子, Lv:是長音還是短音,Lsum:現在有幾秒
        # print(Lstr)
        Lsum += Lv
        Lstr += str(Lv)
        if (Lsum == Ln):
            global Lcount #宣告Lcount為全域變數
            Lcount = Lcount + 1
            # print(Lstr)
        else:
            Lsum+=1
            Lstr+="-"
            if (Lsum < Ln):
                for i in range(1,3):
                    fun(Lstr,i,Lsum)
    for i in range(1,3): #長音,短音
        fun('',i,0)
    print(Lcount)

