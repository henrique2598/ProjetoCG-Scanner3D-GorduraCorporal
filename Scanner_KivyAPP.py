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
        App.get_running_app().root.nome = self.ids.input_name.text
        App.get_running_app().root.idade = self.ids.input_idade.text
        App.get_running_app().root.peso = self.ids.input_peso.text
        App.get_running_app().root.altura = self.ids.input_altura.text
        App.get_running_app().root.sexo = self.ids.input_sexo.text
        App.get_running_app().root.etnia = self.ids.input_etnia.text
        App.get_running_app().root.PopUpWindow_Cadastro.dismiss()

from kivy.properties import StringProperty

# Declara a Tela do Software
class TelaSoftware(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.PopUpWindow_Cadastro = Popup(title = 'Preencha o seu cadastro', content = PopUpCadastro(), size_hint=(None, None), size=(960, 540))
        self.nome = ""
        self.idade = 0
        self.peso = 0
        self.altura = 0
        self.sexo = ""
        self.etnia = ""

    def select_file(self):
        filechooser.open_file(on_selection = self.selected)
    
    def selected(self, selection):
        print(selection[0])
    
    def gerar_relatorio(self):
        print(self.nome)
        print(self.idade)
        print(self.peso)
        print(self.altura)
        print(self.sexo)
        print(self.etnia)

    def spinner_clicked(self, value):
        pass
    
    def abrePopUpInstrucoes(self):
        PopUpWindow_Instrucoes = Popup(title = 'Confira a instruções', content = PopUpInstrucoes(), size_hint=(None, None), size=(960, 540))
        PopUpWindow_Instrucoes.open()
        
    def abrePopUpCadastro(self):
        self.PopUpWindow_Cadastro.open()
    



class Scanner_KivyAPP(App):
    def build(self):
        return TelaSoftware()