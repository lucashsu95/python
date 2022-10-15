#501 訊息顯示
def compute(ment,id,name):
    return(f"Department: {ment}\nStudent ID: {id}]\nName: {name}")

while 1:
    try:
        ment = input()
        id = input()
        name = input()
        print(compute(ment,id,name))
    except:
        break