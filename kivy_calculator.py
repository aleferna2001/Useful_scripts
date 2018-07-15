from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.config import Config
import string
Config.set('graphics','resizable','0')#config é melhor qnd n tem planos de redefinir o tamanho
Config.set('graphics','width','250')
Config.set('graphics','height','265')
class MainWindow(GridLayout):#a janela principal é um layout grid que contém 4 layouts box
    def __init__(self,**kwargs):
        super(MainWindow,self).__init__(**kwargs)
        self.rows=5
        self.padding=5#padding é o espaço entre as childs do widget e as paredes
        self.spacing=5#spacing é o espaço das childs de widget entre si
        self.entry=TextInput(font_size=30,multiline=False,cursor_color=(0,0,0,1))
        self.add_widget(self.entry)
        self.entry.bind(text=self.on_text)
        #criando os layouts box
        self.box1 = Box1()
        self.box1.button1.bind(on_press=self.add_text)#a função só é setada aki porque n se pode acessar propriedades de classes a partir de outras classes
        self.box1.button2.bind(on_press=self.add_text)#bindar o on_press diretamente na confecção do botão n daria certo pq n ia dar pra escrever "MainWindow.entry.text=..."
        self.box1.button3.bind(on_press=self.add_text)#na vdd tem um jeito, que é referenciando o app q está rodando, como em "App.get_running_app().root.entry.text = ...", mas eu optei por bindar td no widget 'MainWindow', onde as propriedades de 'self.entry' podem ser acessadas
        self.box1.button4.bind(on_press=self.add_text)
        
        self.box2 = Box2()
        self.box2.button1.bind(on_press=self.add_text)
        self.box2.button2.bind(on_press=self.add_text)
        self.box2.button3.bind(on_press=self.add_text)
        self.box2.button4.bind(on_press=self.add_text)
        
        self.box3 = Box3()
        self.box3.button1.bind(on_press=self.add_text)
        self.box3.button2.bind(on_press=self.add_text)
        self.box3.button3.bind(on_press=self.add_text)
        self.box3.button4.bind(on_press=self.add_text)

        self.box4=Box4()
        self.box4.button1.bind(on_press=self.clear_text)
        self.box4.button2.bind(on_press=self.add_text)
        self.box4.button3.bind(on_press=self.calculate)
        self.box4.button4.bind(on_press=self.add_text)

        
        self.add_widget(self.box1)
        self.add_widget(self.box2)
        self.add_widget(self.box3)
        self.add_widget(self.box4)


    def on_text(self,instance,value):#self é MainWindow, instance é self.entry e value é self.entry.text
        instance.foreground_color=(0,0,0,1)

    def add_text(self,instance):
        self.entry.text+=instance.text

    def clear_text(self,instance):
        self.entry.text=''

    def output_error(self):
        self.entry.text='TypeError'
        self.entry.foreground_color=(1,0,0,1)

    def calculate(self,instance):#IF OTHERS CAN INPUT DATA, USING EVAL IS SUPER DANGEROUS, AS PEOPLE CAN RUN COMMANDS THROUGH YOUR SCRIPT
        if any(i in self.entry.text for i in string.ascii_lowercase):
            self.output_error()
        else:
            if any(t==self.entry.text[-1] for t in ['+','-','*','/']):
                self.output_error()
            else:
                if '*/' in self.entry.text or '/*' in self.entry.text:
                    self.output_error()
                else:
                    self.entry.text=str(eval(self.entry.text))

class NumBox(BoxLayout):#definindo um padrão para as box que contém 3 números e um sinal
    def __init__(self,x=0,**kwargs):#o x se refere a uma soma para que o texto dos botões estejam corretos
        super().__init__(spacing=5,
                         **kwargs)
        for i in range(1,4):#setattr faz com que setattr(x,'atributo',123) seja igual à x.atributo=123
            setattr(self,'button'+str(i),CustButton(text=str(i+x)))#aki o 'i' é somado ao 'x'
        self.add_widget(self.button1)
        self.add_widget(self.button2)
        self.add_widget(self.button3)

#definindo tds as boxes derivadas de NumBox
class Box1(NumBox):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.button4=CustButton(text='+')#o quarto botão n pode ser generalizado pois se refere aos sinais de operação
        self.add_widget(self.button4)
class Box2(NumBox):
    def __init__(self,**kwargs):
        super().__init__(x=3,**kwargs)#por exemplo, aki x=3 para que os botões tenham texto '4','5','6'
        self.button4=CustButton(text='-')
        self.add_widget(self.button4)
class Box3(NumBox):
    def __init__(self,**kwargs):
        super().__init__(x=6,**kwargs)
        self.button4=CustButton(text='*')
        self.add_widget(self.button4)
        
class Box4(BoxLayout):# a Box4 é diferente das outras, e descende diretamente de BoxLayout, ao invés de NumBox
    def __init__(self,**kwargs):
        super().__init__(spacing=5,
                         **kwargs)
        self.button1=CustButton(text='AC')#apesar dos botões button2 e button4 serem iguais aos demais, o 1 e 3 diferem em comando
        self.button2=CustButton(text='0')
        self.button3=CustButton(text='=')
        self.button4=CustButton(text='/')
        self.add_widget(self.button1)
        self.add_widget(self.button2)
        self.add_widget(self.button3)
        self.add_widget(self.button4)


class CustButton(Button):
    def __init__(self,**kwargs):
        super(CustButton,self).__init__(font_size=32,**kwargs)


class Calculator(App):
    def build(self):
        return MainWindow()

if __name__=='__main__':
    Calculator().run()
