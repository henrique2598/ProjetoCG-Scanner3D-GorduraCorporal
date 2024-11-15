import kivy
from panda3d_kivy.app import App
from kivy.uix.widget import Widget

from plyer import filechooser

kivy.require('2.3.0')


from kivy.uix.popup import Popup

class PopUpInstrucoes(Widget):
    pass

class PopUpCadastro(Widget):
    def SalvaDadosCadastro(self):
        print(self.ids.input_name.text)
        print(self.ids.input_idade.text)
        print(self.ids.input_peso.text)
        print(self.ids.input_altura.text)
        print(self.ids.input_sexo.text)
        print(self.ids.input_etnia.text)


# Declara a Tela do Software
class TelaSoftware(Widget):
    def select_file(self):
        filechooser.open_file(on_selection = self.selected)
    
    def selected(self, selection):
        print(selection[0])

    def spinner_clicked(self, value):
        pass
    
    def abrePopUpInstrucoes(self):
        PopUpWindow = Popup(title = 'Confira a instruções', content = PopUpInstrucoes(), size_hint=(None, None), size=(960, 540))
        PopUpWindow.open()
        
    def abrePopUpCadastro(self):
        PopUpWindow = Popup(title = 'Preencha o seu cadastro', content = PopUpCadastro(), size_hint=(None, None), size=(960, 540))
        PopUpWindow.open()
    



class Scanner_KivyAPP(App):
    def build(self):
        return TelaSoftware()