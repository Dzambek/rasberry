from PIL import Image
from pyzbar.pyzbar import decode
#import picamera
import serial
from kivy.uix.textinput import TextInput
from kivy.uix.textinput import TextInput
from data import key_by_num
from time import sleep
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App

Config.set('graphics', 'width', 400)
Config.set('graphics', 'height', 400)

import serial
import time

class Menu_Screen(Screen):
    def __init__(self, **kw):
        super(Menu_Screen, self).__init__(**kw)
        #self.data = str(self.data_qr[0][0][0:])[1:]
        #self.data_qr = decode(Image.open('qr_data.png'))
        bl = BoxLayout(orientation='vertical', padding=10, spacing=10, size_hint=(0.75, .75), pos=(250, 100))
        bl.add_widget(Button(text="Scan QR", on_press=lambda x: self.on_press(), size_hint=(0.3, 0.02), pos=(350, 200)))
        bl.add_widget(Button(text="Reg", on_press=lambda x: self.registr(), size_hint=(0.3, 0.02), pos=(350, 200)))
        self.add_widget(bl)
    def registr(self):
        print(1)
        set_screen("input")

    def on_press(self):
        set_screen("m_box")
       #try:
           # camera = picamera.PiCamera(resolution=(1280, 720))
           # while True:
             #   sleep(1)
              #  camera.capture('qr_data.png')
               # self.data_qr = decode(Image.open('qr_data.png'))
               # try:
                #    self.data = str(self.data_qr[0][0][0:])[1:]
               # except:
                 #   print("no")
                #if type(self.data) == str:
                    #break
        #finally:
           # camera.close()
           # print("End of program")
        #for id_man in data:

class Menu_of_box(Screen):
    def __init__(self, **kw):
        super(Menu_of_box, self).__init__(**kw)
        gl = BoxLayout(orientation='vertical', padding=10, spacing=10, size_hint=(0.75, .75), pos=(250, 100))
        gl.add_widget(Button(text="BOx_1", on_press=lambda x: self.on_press1()))
        gl.add_widget(Button(text="BOx_2", on_press=lambda x: self.on_press2()))
        gl.add_widget(Button(text="BOx_3", on_press=lambda x: self.on_press3()))
        gl.add_widget(Button(text="BOx_4", on_press=lambda x: self.on_press4()))
        gl.add_widget(Button(text="BOx_5", on_press=lambda x: self.on_press5()))
        gl.add_widget(Button(text="BOx_6", on_press=lambda x: self.on_press6()))
        gl.add_widget(Button(text="BOx_7", on_press=lambda x: self.on_press7()))
        gl.add_widget(Button(text="BOx_8", on_press=lambda x: self.on_press8()))
        gl.add_widget(Button(text="BOx_9", on_press=lambda x: self.on_press9()))
        gl.add_widget(Button(text="НАЗАД", on_press=lambda x: self.on_press()))
        self.add_widget(gl)
    def on_press(self):
        set_screen("menu")
        '''number = int(instance[-1])
        usbCom = serial.Serial('/dev/ttyACM0', 9600)
        time.sleep(2)  # <<=======================================
        usbCom.open
        time.sleep(2)
        usbCom.write(str(number).encode('utf-8'))
        usbCom.close
        key_by_num(self.qr_answer, 'ничего')
        set_screen("menu")'''
    def on_press2(self):
        number = 2
        '''usbCom = serial.Serial('/dev/ttyACM0', 9600)
        time.sleep(2)  # <<=======================================
        usbCom.open
        time.sleep(2)
        usbCom.write(str(number).encode('utf-8'))
        usbCom.close
        key_by_num(self.qr_answer, 'ничего')'''
        set_screen("menu")
    def on_press3(self):
        number = 3
        '''usbCom = serial.Serial('/dev/ttyACM0', 9600)
        time.sleep(2)  # <<=======================================
        usbCom.open
        time.sleep(2)
        usbCom.write(str(number).encode('utf-8'))
        usbCom.close
        key_by_num(self.qr_answer, 'ничего')'''
        set_screen("menu")
    def on_press4(self):
        number = 4
        '''usbCom = serial.Serial('/dev/ttyACM0', 9600)
        time.sleep(2)  # <<=======================================
        usbCom.open
        time.sleep(2)
        usbCom.write(str(number).encode('utf-8'))
        usbCom.close
        key_by_num(self.qr_answer, 'ничего')'''
        set_screen("menu")
    def on_press5(self):
        number = 5
        '''usbCom = serial.Serial('/dev/ttyACM0', 9600)
        time.sleep(2)  # <<=======================================
        usbCom.open
        time.sleep(2)
        usbCom.write(str(number).encode('utf-8'))
        usbCom.close
        key_by_num(self.qr_answer, 'ничего')'''
        set_screen("menu")
    def on_press6(self):
        number = 6
        '''usbCom = serial.Serial('/dev/ttyACM0', 9600)
        time.sleep(2)  # <<=======================================
        usbCom.open
        time.sleep(2)
        usbCom.write(str(number).encode('utf-8'))
        usbCom.close
        key_by_num(self.qr_answer, 'ничего')'''
        set_screen("menu")
    def on_press7(self):
        number = 7
        '''usbCom = serial.Serial('/dev/ttyACM0', 9600)
        time.sleep(2)  # <<=======================================
        usbCom.open
        time.sleep(2)
        usbCom.write(str(number).encode('utf-8'))
        usbCom.close
        key_by_num(self.qr_answer, 'ничего')'''
        set_screen("menu")
    def on_press8(self):
        number = 8
        '''usbCom = serial.Serial('/dev/ttyACM0', 9600)
        time.sleep(2)  # <<=======================================
        usbCom.open
        time.sleep(2)
        usbCom.write(str(number).encode('utf-8'))
        usbCom.close
        key_by_num(self.qr_answer, 'ничего')'''
        set_screen("menu")
    def on_press9(self):
        number = 9
        '''usbCom = serial.Serial('/dev/ttyACM0', 9600)
        time.sleep(2)  # <<=======================================
        usbCom.open
        time.sleep(2)
        usbCom.write(str(number).encode('utf-8'))
        usbCom.close
        key_by_num(self.qr_answer, 'ничего')'''
        set_screen("menu")
class Regestration(Screen):
    def __init__(self, **kw):
        super(Regestration, self).__init__(**kw)
        self.cols = 2
        gl = BoxLayout(orientation='vertical', padding=10, spacing=10, size_hint=(0.75, .75), pos=(250, 100))

        gl.add_widget(Label(text="First Name: "))
        self.name1 = TextInput(multiline=False)
        print (self.name1.text)
        #self.name1.bind(text = self.on_text())
        gl.add_widget(self.name1)
        gl.add_widget(Label(text="Last Name: "))
        self.lastName = TextInput(multiline=False)
        gl.add_widget(self.lastName)

        gl.add_widget(Label(text="Email: "))
        self.email = TextInput(multiline=False)
        gl.add_widget(self.email)
        self.add_widget(gl)

        gl.add_widget(Button(text="НАЗАД", on_press=lambda x: self.on_press14()))

    def on_text(instance,  value):
        print('The widget', instance, 'have:', value)
    def on_press14(self):
        set_screen("menu")

sm = ScreenManager()
sm.add_widget(Menu_Screen(name='menu'))
sm.add_widget(Menu_of_box(name='m_box'))
sm.add_widget(Regestration(name='input'))


def set_screen(name_screen):
    assert isinstance(name_screen, object)
    sm.current = name_screen


class TestApp(App):
    def build(self):
        set_screen('menu')
        return sm


if __name__ == '__main__':
    TestApp().run()
