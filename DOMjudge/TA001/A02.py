#TA001 BMI
while 1:
    try:
        weight,height = list(map(int,input().split()))
        BMI = weight / ((height/100)**2)
        BMI = round(BMI,2)
        print(BMI)
    except:
        break