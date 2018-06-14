def get_num(): #como fazer uma def. Se n botar return n funciona
        return input("Passa um número ")
while True:
    n=get_num()
    if n==".":
        break
    nd=list(range(1,int(n)+1))
    ft=[]
    for b in nd:
        if int(n) % b == 0:
            ft.append(b)
    d=str(ft)
    print("os divisores dele são: "+d)