#小明的哨音
import sys
for Ln in sys.stdin.read().splitlines():
    Ln = int(Ln)
    # Ln = 20
    Lcount = 0
    def fun(Lstr,Lv,Lsum): #Lstr:字串的樣子, Lv:是長音還是短音,Lsum:現在有幾秒
        print(Lstr)
        if (Lv > 0):
            Lsum += Lv
            Lstr += str(Lv)

        if (Lsum == Ln):
            global Lcount #宣告Lcount為全域變數
            Lcount = Lcount + 1
            print('V'+Lstr)
        elif (Lsum < Ln):
            if (Lsum > 0):
                Lsum+=1
                Lstr+="-"
            for i in range(1,3):
                fun(Lstr,i,Lsum)

    fun("",0,0)
    print(Lcount)