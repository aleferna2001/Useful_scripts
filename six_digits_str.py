import random as rd
from ascii_art import print_hello
print_hello("generating a random six digits string")
print("There it goes! If you didn't like your password, just press any key")
print()
while True:
    a='qwertyuiopasdfghjklzxcvbnm1234567890'
    b=""
    passw=rd.sample(a,6)
    for i in passw:
        b+=i
    print(b)
    input()
