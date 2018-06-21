import getpass
from ascii_art import print_hangman
from ascii_art import print_hello
from time import sleep
import random as rd
lcomidas=['arroz', 'feijão', 'macarrão', 'lasanha', 'espaguete', 'salada', 'batata-frita', 'bife', 'frango',
         'pão-com-manteiga', 'queijo', 'frutas', 'sanduíche', 'leite', 'café', 'água', 'suco', 'bife', 'bacon',
         'waffle', 'carne-bovina', 'pasta-de-amendoim', 'hambúrguer', 'panqueca', 'chá', 'sorvete', 'bolo',
         'torta', 'picolé', 'gelatina', 'chocolate']
lanimais=['abelha', 'água-viva', 'águia', 'alce', 'andorinha', 'anta', 'antílope', 'aranha', 'avestruz', 'babuíno',
         'baleia', 'barata', 'bisão', 'boi', 'borboleta', 'búfalo', 'burro', 'cabra', 'camelo', 'canguru', 'cão',
         'caracol', 'caranguejo', 'carneiro', 'castor', 'cavalo', 'chacal', 'chimpanzé', 'cisne', 'cobra', 'coelho',
         'coiote', 'coruja', 'corvo', 'crocodilo', 'doninha', 'dragão-de-komodo', 'elefante', 'enguia', 'équidna',
         'esquilo', 'estrela-do-mar', 'falcão', 'foca', 'formiga', 'frango', 'fuinha', 'furão', 'gaivota', 'ganso',
         'garça', 'gato', 'gazela', 'girafa', 'gnu', 'golfinho', 'gorila', 'guaxinim', 'hamster', 'hiena', 'hipopótamo',
         'iguana', 'jacaré', 'jaguar', 'javali', 'lagarta', 'lagarto', 'lagosta', 'leão', 'leão-marinho', 'lebre',
         'leopardo', 'lhama', 'libélula', 'lobo', 'lontra', 'lula', 'macaco', 'morcego', 'morsa', 'mosca', 'mosquito',
         'mula', 'naja', 'ostra', 'ouriço', 'ovelha', 'panda', 'pantera', 'pato', 'pavão', 'peixe-boi', 'pelicano',
         'perdiz', 'perú', 'piolho', 'pomba', 'pônei', 'porco', 'porco-espinho', 'porquinho-da-índia', 'puma', 'raposa',
         'rato', 'rena', 'rinoceronte', 'salamandra', 'sapo', 'serpente', 'suricate', 'tartaruga', 'tatu', 'texugo',
         'tigre', 'toupeira', 'tubarão', 'urso', 'veado', 'vespa', 'zebra']
print_hello('playing hangman')
print('Esse é Norberto, que foi preso por coçar a bunda com escova de dente')
print('                    O')  
print('                   \|/')
print('                    |')
print('                   / \ ')
print()
print('Apesar de tudo, Norberto é um cara legal, tenta não matar ele')
print()
while True:
    while True:
        choice=input('Quer escolher uma palavra ou gerá-la aleatoriamente? Pressione "a" para aleatório ou "e" para escolher: ')
        print()
        if choice=='a':
            print("Escolha uma categoria dentre as seguintes:")
            print()
            print("animais")
            print("comidas")
            print()
            while True:
                ctg=input("Escolha uma: ")
                print()
                if ctg=='animais' or ctg=='comidas':
                    break
                print('Digitou algo errado')
                print()
            if ctg=='animais':
                rword=rd.choice(lanimais)
            if ctg=='comidas':
                rword=rd.choice(lcomidas)
            break
        elif choice=='e':
            rword=getpass.getpass('Escreva a palavra em letras minúsculas e utilizando "-" como espaços (é normal a palavra não aparecer, só dá ENTER qnd acabar): ')
            print()
            break
        print('Rolou um erro de digitação aí')
        print()
    alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
              't', 'u', 'v', 'w', 'x', 'y', 'z','-']
    word=[]
    for i in rword:
        if i=="á" or i=="ã" or i=="â":
            word.append('a')
        elif i=="ó" or i=="õ" or i=="ô":
            word.append('o')
        elif i=="é" or i=="ê":
            word.append('e')
        elif i=="í":
            word.append('i')
        elif i=="ú":
            word.append('u')
        else:
            word.append(i)
    blank=[]
    for i in word:
        blank.append("_")
    wguesses=0
    print_hangman(0)
    print()
    print(len(word)*'_')
    print()
    while True:
        blankstr=''
        while True:
            letra=input('Digite a letra: ')
            print()
            if letra in alphabet:    
                alphabet.remove(letra)
                break
            print("Você já tentou essa letra ou isso nem letra é, digite outra")
            print()
        if letra not in word:
            print("Não tem",'"'+letra+'"','na palavra, tu quer o Norberto morto msm hein')
            print()
            wguesses+=1 
        start=0
        for i in word:
            if i==letra:
                indx=word.index(i,start)
                blank[indx]=rword[indx]
            start+=1
        for i in blank:
            blankstr+=i
        print_hangman(wguesses)
        print()
        print(blankstr)
        print()
        if wguesses==4:
            print('Krl, nem pra adivinhar uma palavra tu serve')
            print()
            sleep(4)
            break
        if blankstr==rword:
            print('Você ganhou! Parabéns xovem')
            print()
            sleep(4)
            break
