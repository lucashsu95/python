Ln = input()

Lsum = ''
Lans = {
    "E":'10',
    "T":'01',
    "A":'11',
    "O":'001',
    "I":'000'
}
line = 2
while True:
    if(Ln[line-2:line]) == Lans['E']:
        Lsum += "E"
        line+=2

    elif(Ln[line-2:line]) == Lans['T']:
        Lsum += "T"
        line+=2
    
    elif(Ln[line-2:line]) == Lans['A']:
        Lsum += "A"
        line+=2
    else:
        if Ln[line-2:line+1] == Lans['O']:
            Lsum+="O"
            line+=3
        elif Ln[line-2:line+1] == Lans['I']:
            Lsum+= "I"
            line+=3
        else:
            print('編碼有誤!')
            exit()
    if line >= len(Ln)+2:
        break
print(Lsum)

    