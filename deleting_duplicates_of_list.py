from ascii_art import print_hello
print_hello("deleting duplicates of your list")
while True:
    d=[]
    f=[]
    print('Digit the elements of the list separated by commas("x,y,z"). Press "." when you are done: ')
    a=input()
    c=a.split(",")
    for i in c:
        d.append(int(i))
    b=set(d) #set n contém elementos repetidos ou numerados, só "elementos"
    print(sorted(b))
    print()
    break
