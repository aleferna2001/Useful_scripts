a=[]
b=[]
l=[]
print('Digit the elements of the 1st list one by one. Press "." when you are done: ')
while True:
    c=input()
    if c!=".":
        a.append(c)
    elif c==".":
        break
print('Digit the elements of the 2nd list one by one. Press "." when you are done: ')
while True:
    d=input()
    if d!=".":
        b.append(d)
    elif d==".":
        break
for i in (a) and (b):
    if i in a and b:
        l.append(i)
print("The values common to both lists are: "+str(l))
input()
