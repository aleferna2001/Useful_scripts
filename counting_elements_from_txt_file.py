import re
from ascii_art import print_hello
print_hello("counting elements from a txt file")
with open('counting.txt','r') as file:
    d=file.read()
    a=d.lower()
b=sorted(re.split('\W+',a)) #usado para separar strs baseado em um padrão. nesse caso o "\W+" separa qualquer caracter n alfabético infinitas vezes até que a str n contenha nada além de letras

c={x:b.count(x) for x in b}
for x,v in c.items():
    print(x,v)
