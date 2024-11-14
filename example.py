import kivy
from panda3d_kivy.app import App
from kivy.uix.widget import Widget

from plyer import filechooser

kivy.require('2.3.0')



# Declara a Tela do Software
class TelaSoftware(Widget):
    def select_file(self):
        filechooser.open_file(on_selection = self.selected)
    
    def selected(self, selection):
        print(selection[0])

    def spinner_clicked(self, value):
        pass


class Example(App):
    def build(self):
        return TelaSoftware()