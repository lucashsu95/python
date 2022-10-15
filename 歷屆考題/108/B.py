#108B保齡球計分
n = int(input())
for _ in range(n):
    data = input().split(' ')
    Lsum = 0
    cut = 0
    for i in range(len(data)):

        if cut == 9:
            # print(data[i],data[i+1],data[i+2])
            if data[i] == 'X':
                if data[i+1] == 'X':
                    if data[i+2] == 'X':
                        Lsum += 30
                    else:
                        Lsum += 20 + int(data[i+2])
                elif data[i+2] == '/':
                    Lsum += 20
                else:
                    
                    Lsum += 10 + int(data[i+1]) + int(data[i+2])
                    
            elif data[i+1] == '/':
                if data[i+2] == 'X':
                    Lsum += 20
                else:
                    Lsum += 10 + int(data[i+2])
                    
            else:
                Lsum += int(data[i]) + int(data[i+1])

            break
        

        if data[i] == 'X':
            if data[i+1] == 'X':
                if data[i+2] == 'X':
                    Lsum += 30
                else:
                    Lsum += 20 + int(data[i+2])

            elif data[i+2] == '/':
                Lsum += 20
            else:
                Lsum += 10 + int(data[i+1]) + int(data[i+2])

        elif data[i] == '/':
            if data[i+1] == 'X':
                Lsum += 10 - int(data[i-1]) + 10
            else:
                Lsum += 10 - int(data[i-1]) + int(data[i+1])
        else:
            Lsum += int(data[i])
        
        if data[i] == 'X':
            cut += 1
        else:
            cut += 0.5
    print(Lsum)
