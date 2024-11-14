import kivy
from panda3d_kivy.app import App
from kivy.uix.widget import Widget

from kivy.core.window           import Window

kivy.require('2.3.0')

from kivy.uix.popup import Popup



# Declara a Tela do Software
class TelaSoftware(Widget):
    def select_file(self):
        from plyer import filechooser
        filechooser.open_file(on_selection = self.selected)
    
    def selected(self, selection):
        print(selection[0])

class Example(App):
    def build(self):
        return TelaSoftware()