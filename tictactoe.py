from ascii_art import print_hello

def print_rules():
    print("Como funciona? Presta atenção poura:")
    print()
    print("Esse é o tabuleiro:")
    print("    a   b   c")
    print("1 ['0','0','0']")
    print("2 ['0','0','0']")
    print("3 ['0','0','0']")
    print()
    print('As linhas correspondem aos números "1", "2" e "3", enquanto as colunas correspondem às letras "a", "b" e "c"')
    print("Para jogar, escreva a linha e a coluna na qual deseja jogar separadas por uma vírgula (1,a por exemplo)")
    print("Ademais é jogo da velha msm, qualquer retarda sabe jogar")
    print()
    
def win_cond():
    playing=1
    f=matrix[0]
    s=matrix[1]
    t=matrix[2]
    for x in range(3):
        if f[x]==s[x] and f[x]==t[x] and f[x]!='0':
            print("Jogador",f[x],"ganhou!")
            print()
            playing=0
            return playing
    for i in matrix:
        if len(set(i))==1 and set(i)!={'0'}:
            print("Jogador",i[0],"ganhou!")
            print()
            playing=0
            return playing
    if f[0]==s[1] and f[0]==t[2] and f[0]!='0':
        print("Jogador",f[0],"ganhou!")
        print()
        playing=0
        return playing
    elif f[2]==s[1] and f[2]==t[0] and f[2]!='0':
        print("Jogador",f[2],"ganhou!")
        print()
        playing=0
        return playing
    elif '0' not in f+s+t:
        playing="velha"
        return playing

def jogada(pl):
    while True:
        while True:
            jgd=input("Faz a tua jogada, jogador "+pl+": ")
            print()
            if len(jgd)==3 and jgd[1]==",":
                jgd2=jgd.split(",")
                jgd2[0]=int(jgd[0])-1
                if jgd2[0] in range(3) and jgd2[1]=="a" or jgd2[1]=="b" or jgd2[1]=="c":
                    break
            print("Tu escreveu algo errado")
            print()
        if jgd2[1]=="a":
            col=0
        elif jgd2[1]=="b":
            col=1
        elif jgd2[1]=="c":
            col=2
        if matrix[jgd2[0]][col]=='0':
            matrix[jgd2[0]][col]=pl
            print(matrix[0])
            print(matrix[1])
            print(matrix[2])
            print()
            break
        print("Alguém já jogou aí")
        print()
		
print_hello("playing tictactoe")
print_rules()
X=0
V=0
while True:
    matrix=[['0','0','0'],
            ['0','0','0'],
            ['0','0','0']]
    while True:
        jogada('X')
        if win_cond()==0:
            X+=1
            print("Número de vitórias:")
            print('Jogador X:',X)
            print('Jogador V:',V)
	    print()
            print('Novo jogo:')
            print()
            break
        elif win_cond()=="velha":
            print("Deu velha, tio")
            print()
            print("Número de vitórias:")
            print('Jogador X:',X)
            print('Jogador V:',V)
	    print()
            print('Novo jogo:')
            print()
            break
        jogada('V')
        if win_cond()==0:
            V+=1
            print("Número de vitórias:")
            print('Jogador X:',X)
            print('Jogador V:',V)
	    print()
            print('Novo jogo:')
            print()
            break
