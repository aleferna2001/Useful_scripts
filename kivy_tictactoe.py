from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.properties import BooleanProperty
from kivy.properties import StringProperty
from kivy.clock import Clock
from kivy.config import Config
height=800
width=int(height*6/7)
Config.set('graphics','resizable','0')
Config.set('graphics','width',str(width))
Config.set('graphics','height',str(height))

class Square(Button):
    text_id=StringProperty()
    playing=BooleanProperty()
    def clear(self):
        self.text=''
        self.disabled=False
        

class MainWindow(GridLayout):
    sound=SoundLoader.load('tictactoe.wav')
    symbol_num=ObjectProperty(2)
    matrix=ObjectProperty([['0','0','0'],['0','0','0'],['0','0','0']])
    player_X=ObjectProperty()
    player_O=ObjectProperty()
    mid_square=ObjectProperty()
    all_disabled=BooleanProperty(False)
    game_playing=BooleanProperty(True)
    
    def place(self,instance):#place 'X' or 'O' in the square and then check() if someone won
        self.game_playing=True
        if self.symbol_num%2==0:
            self.jogada(instance,'X')
            instance.text='X'
        else:
            self.jogada(instance,'O')
            instance.text='O'
        self.symbol_num+=1
        instance.font_size=120
        instance.disabled=True
        if self.check():
            self.sound.play()
            self.all_disabled=True
            self.matrix=[['0','0','0'],['0','0','0'],['0','0','0']]
            Clock.schedule_once(self.end_game, 2)
            #should reset text of all squares children of MainWindow
    def end_game(self,time):
        self.game_playing=False
        self.all_disabled=False
                    
    def check(self): #checks for win condition and updates scoreboard if some one won
        over=False
        f=self.matrix[0]
        s=self.matrix[1]
        t=self.matrix[2]
        for x in range(3):
            if f[x]==s[x] and f[x]==t[x] and f[x]!='0':
                if f[x]=='X':
                    self.player_X.text=str(int(self.player_X.text)+1)
                elif f[x]=='O':
                    self.player_O.text=str(int(self.player_O.text)+1)
                print(1)
                over=True
                return over
        for i in self.matrix:
            if len(set(i))==1 and set(i)!={'0'}:
                if i[0]=='X':
                    self.player_X.text=str(int(self.player_X.text)+1)
                elif i[0]=='O':
                    self.player_O.text=str(int(self.player_O.text)+1)
                print(2)
                over=True
                return over
        if f[0]==s[1] and f[0]==t[2] and f[0]!='0':
            if f[0]=='X':
                self.player_X.text=str(int(self.player_X.text)+1)
            elif f[0]=='O':
                self.player_O.text=str(int(self.player_O.text)+1)
            print(3)
            over=True
            return over
        elif f[2]==s[1] and f[2]==t[0] and f[2]!='0':
            if f[2]=='X':
                self.player_X.text=str(int(self.player_X.text)+1)
            elif f[2]=='O':
                self.player_O.text=str(int(self.player_O.text)+1)
            print(4)
            over=True
            return over
        elif '0' not in f+s+t:
            print('velha')
            over=True
            return over
    
    def jogada(self,instance,value):#updates the matrix used for checking the win condition
        if instance.text_id[1]=="a":#uses the invisible white text to update matrix
            col=0
        elif instance.text_id[1]=="b":
            col=1
        elif instance.text_id[1]=="c":
            col=2
        self.matrix[int(instance.text_id[0])-1][col]=value
        print(self.matrix)
        
class TicTacToeApp(App):
    def build(self):
        return MainWindow()

if __name__=='__main__':
    TicTacToeApp().run()
