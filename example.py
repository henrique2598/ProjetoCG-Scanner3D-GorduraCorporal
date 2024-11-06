import kivy
from panda3d_kivy.app import App
from kivy.uix.widget import Widget

from kivy.core.window           import Window

kivy.require('2.3.0')



# Declara a Tela do Software
class TelaSoftware(Widget):
    pass

class Example(App):
    def build(self):
        return TelaSoftware()