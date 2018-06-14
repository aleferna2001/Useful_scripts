def make_textfile(nome):
    with open(nome,"w") as file:
        print('Write the text. When you are done, press ".": ')
        while True:
            text=input()
            if text=='.':
                break
            file.write(text+"\n")#O "\n" indica q o texto deve ser escrito em uma nova linha.
                                 #Sem ele, o texto seria simplesmente colado no final da linha atual
#make_textfile('teste.txt')
