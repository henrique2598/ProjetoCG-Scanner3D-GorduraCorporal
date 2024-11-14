import kivy
from panda3d_kivy.app import App
from kivy.uix.widget import Widget

from plyer import filechooser

kivy.require('2.3.0')


from kivy.uix.popup import Popup

class PopUpCadastro(Popup):
    pass

    


# Declara a Tela do Software
class TelaSoftware(Widget):
    def select_file(self):
        filechooser.open_file(on_selection = self.selected)
    
    def selected(self, selection):
        print(selection[0])

    def spinner_clicked(self, value):
        pass

    def abrePopUpCadastro(self):
        PopUpWindow = Popup(title = 'Preencha o seu cadastro' ,content = PopUpCadastro(),size_hint = (0.9,0.9))
        PopUpWindow.open()
        


class Example(App):
    def build(self):
        return TelaSoftware()