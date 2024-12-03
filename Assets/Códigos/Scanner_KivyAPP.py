import kivy
from panda3d_kivy.app import App
from kivy.uix.widget import Widget

kivy.require('2.3.0')

from kivy.properties import StringProperty, NumericProperty

from kivy.uix.popup import Popup


from jinja2 import Template


class PopUpInstrucoes(Widget):
    pass

class PopUpCadastro(Widget):
    def SalvaDadosCadastro(self):        
        App.get_running_app().root.nome = self.ids.input_name.text
        App.get_running_app().root.idade = int(self.ids.input_idade.text)
        App.get_running_app().root.idade_formatado = (self.ids.input_idade.text)+" anos"
        App.get_running_app().root.peso = int(1000.0*float(self.ids.input_peso.text))
        App.get_running_app().root.peso_formatado = str(self.ids.input_peso.text)+" kg"
        App.get_running_app().root.altura = int(self.ids.input_altura.text)
        App.get_running_app().root.altura_formatado = str(self.ids.input_altura.text)+" cm"
        App.get_running_app().root.sexo = self.ids.input_sexo.text
        App.get_running_app().root.etnia = self.ids.input_etnia.text
        App.get_running_app().root.PopUpWindow_Cadastro.dismiss()
        self.ids.input_name.text = ""
        self.ids.input_idade.text = ""
        self.ids.input_peso.text = ""
        self.ids.input_altura.text = ""
        self.ids.input_sexo.text = ""
        self.ids.input_etnia.text = ""

# Declara a Tela do Software
class TelaSoftware(Widget):
    nome = StringProperty()
    idade = NumericProperty()
    peso = NumericProperty()
    altura = NumericProperty()
    idade_formatado = StringProperty()
    peso_formatado = StringProperty()
    altura_formatado = StringProperty()
    sexo = StringProperty()
    etnia = StringProperty()
    volumeModelo3D = NumericProperty()
    gorduraCorporal = NumericProperty()
    gorduraCorporal_formatado = StringProperty()
    
    # Cria um template
    template = Template("""
<!DOCTYPE html>
<html>
<head>
<title>Resultado - {{ nome }}</title>
</head>
<body>

<h1>Gordura Corporal</h1>

<p>Nome: {{ nome }} </p>
<p>Idade: {{ idade }} </p>
<p>Peso: {{ peso }} </p>
<p>Altura: {{ altura }} </p>
<p>Sexo: {{ sexo }} </p>
<p>Etnia: {{ etnia }} </p>
<p>Gordura Corporal: {{ gordura_corporal }} </p>

</body>
</html>
""")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.PopUpWindow_Cadastro = Popup(title = 'Preencha o seu cadastro', content = PopUpCadastro(), size_hint=(None, None), size=(960, 540))
        self.PopUpWindow_Instrucoes = Popup(title = 'Confira a instruções', content = PopUpInstrucoes(), size_hint=(None, None), size=(960, 540))
        self.nome = ""
        self.idade = 0
        self.peso = 0
        self.altura = 0
        self.idade_formatado = ""
        self.peso_formatado = ""
        self.altura_formatado = ""
        self.sexo = ""
        self.etnia = ""
        self.volumeModelo3D = 0
        self.gorduraCorporal = 0
        self.gorduraCorporal_formatado = ""

    def abrePopUpInstrucoes(self):
        self.PopUpWindow_Instrucoes.open()
        
    def abrePopUpCadastro(self):
        self.PopUpWindow_Cadastro.open()

    def limpar_dados(self):
        self.nome = ""
        self.idade = 0
        self.peso = 0
        self.altura = 0
        self.idade_formatado = ""
        self.peso_formatado = ""
        self.altura_formatado = ""
        self.sexo = ""
        self.etnia = ""
        self.gorduraCorporal = 0
        self.gorduraCorporal_formatado = ""

    def select_file(self):
        print(App.get_running_app())

    def calcular_gordura(self):
        self.gorduraCorporal = 75.25
        self.gorduraCorporal_formatado = "75,25%"

    def gerar_relatorio(self):
        self.calcular_gordura()

        # Renderiza o template com os dados
        output = self.template.render(nome=self.nome,
                                 idade=self.idade_formatado,
                                 peso=self.peso_formatado,
                                 altura=self.altura_formatado,
                                 sexo=self.sexo,
                                 etnia=self.etnia,
                                 gordura_corporal=self.gorduraCorporal)

        # Salva o resultado
        with open('Outputs/Resultado.html', 'w') as f:
            f.write(output)

class Scanner_KivyAPP(App):
    def build(self):
        return TelaSoftware()