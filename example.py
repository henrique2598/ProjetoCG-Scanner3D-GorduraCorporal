from panda3d_kivy.app import App
from kivy.uix.button import Button

class Example(App):
    def build(self):
        return Button(text='Hello, world!', size_hint= (0.233, 0.0786))
'''
            Button:
        id: Btn_Iniciar
        size_hint: 0.233, 0.0786
        pos: root.center_x - (self.width/2), root.center_y - (self.height/2)
        text:"Iniciar"
        on_release:
            root.manager.transition.direction = 'left'
            root.manager.current = 'software'
'''