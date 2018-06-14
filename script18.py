import random as rd
from time import sleep
from ascii_art import print_hello
from ascii_art import print_butthurt
from ascii_art import print_trophy
print_hello('playing "cows and bulls"')
print("The rules are simple:")
print()
print("I will generate a numeric sequence of 4 numbers, and you have to guess the digits in it.")
print('For every existing digit in the sequence that is in the wrong place, you get a "bull". For every one in the right place, you get a "cow".')
print("The game ends when you get 4 cows!")
print()
while True:
    string_random_num=''
    random_num=rd.sample(range(9),4)
    for t in random_num:
        string_random_num+=str(t)
    guess=[]
    cowbulls=[0,0]
    while cowbulls[0]<4:
        del(guess[:])
        cowbulls[0]=0
        cowbulls[1]=0
        while True:
            string_guess=input("Guess a 4 digits number without duplicates: ")
            for i in string_guess:
                guess.append(int(i))
            if len(set(guess))==4:
                break
            else:
                del(guess[:])
                print()
                print("There cannot be two of the same number, you dense motherfucker. Try again")
                print()
        for x in range(len(guess)):
            if random_num[x]==guess[x]:
                cowbulls[0]+=1
        for i in guess:
            if i in random_num and guess.index(i)!=random_num.index(i):
                cowbulls[1]+=1
        print()
        print("You got "+str(cowbulls[0])+" cow and "+str(cowbulls[1])+" bull!")
        print()
    print("Congrats, you won!")
    print("The sequence was: "+string_random_num)
    print()
    print("Here is your trophy:")
    print()
    print_trophy()
    print()
    f=input("Do you wanna play again? Y/N: ")
    print()
    if f=="n" or f=="N":
        print_butthurt()
        sleep(7)
        break
    