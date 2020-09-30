from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
import kivy
kivy.require('1.9.0')
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.lang.builder import Builder
from kivy.graphics import Line
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
import socket, threading
Builder.load_string("""
<hello>:
    cols: 2
    Label :
        id : one
        text: root.ids.three.text
    Button :
        id : two
        text : "send"
        on_release : root.do()
    TextInput:
        id : three
        text : "write something"
    Button:
        id : five
        text : "exit"
        on_release : root.exitw()
""")
class hello(GridLayout):
    def runningasinit(self):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.connect(("127.0.0.1",4350))
        print("connected")
    def sendd(self):
        print("in send\n")
        #while True :
        data = str(self.ids.three.text)
        self.s.send(str.encode(data,"utf-8"))
        print("sended :",data)
    def recvd(self):
        print("in recv \n")
        while True :
            data2 = self.s.recv(1024)
            print("received :",data2)
            data2 = data2.decode("utf-8")
            #if "goodbye" in data:
             #  self.clean_up()
            #else :
            l = str(data2)
            self.ids.one.text = l
    def clean_up(self):
        print("cleaning")
        #self.t1.join()
        #self.t2.join()
        self.s.close()
    def start(self):
        try :
            self.t1 = threading.Thread(target = self.sendd)
            self.t2 = threading.Thread(target = self.recvd)
            self.t1.start()
            self.t2.start()
        except Exception as e :
            self.ids.one.text = str(e)
            self.t1.join()
            self.t2.join()
            self.clean_up()
    def do(self):
        self.runningasinit()
        self.start()
        #self.clean_up()
    def exitw(self):
        exit()
#f = Builder.load_file("main.kv")
class MyApp(App):
    def build(self):
        return hello()

if __name__ == '__main__':
    MyApp().run()
