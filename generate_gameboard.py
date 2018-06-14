from ascii_art import print_hello
print_hello("making your own game board")
a=' ---'
b='|   '
c="|"
size=input("How big do you want your game board? Use commas to tell x and y apart (x,y): ")
size2=size.split(',')
x=int(size2[0])
y=int(size2[1])
with open('gameboard.txt','w') as file:
    for i in range(y):
        file.write(a*x+'\n')
        file.write(b*x+c+'\n')
    file.write(a*x+'\n')
