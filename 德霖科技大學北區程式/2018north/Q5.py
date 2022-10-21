#正整數分割
n = 5
def fun(num,s,t): #num 迴圈起始值3,2,1 , s:累積的字串 t:累積值
    t1 = 0
    for i in range(num,0,-1): #4、3、2、1
        t1 = t+i
        
        if (t1<n):
            # print(f"fun({i},{s+str(i)},{t1})")
            fun(i,s+str(i),t1)
        if (t1==n):
            print(s+str(i))
            
print(n)
for i in range(n-1,0,-1):  #4、3、2、1
    fun(i,str(i),i)
    