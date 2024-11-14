#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Imports
from Old.Telas               import *
import kivy
from kivy.app                   import App
from kivy.core.audio            import SoundLoader
from kivy.uix.screenmanager     import ScreenManager
from kivy.core.window           import Window

kivy.require('2.3.0')

from kivy.config import Config
Config.set('kivy', 'exit_on_escape', '1')

#Configurações da Tela
Window.fullscreen = 'auto'
#Window.set_icon('Assets/img/Bola.png')


# Cria o Gerenciador de Telas
screen_manager = ScreenManager()
class Scanner3D(App):

    def build(self):

        # Carrega o áudio
        sound = SoundLoader.load('Assets/audio/bg-music.mp3')

        # Verifica se houve o carregamento do áudio e o aciona
        #if sound:
        #    sound.play()

        # Adiciona as telas ao gerenciador
        screen_manager.add_widget(TelaInicial(name='inicial'))
        screen_manager.add_widget(TelaConfiguracoes(name='configuracoes'))
        screen_manager.add_widget(TelaCreditos(name='creditos'))
        screen_manager.add_widget(TelaSoftware(name="software"))

        return screen_manager

if __name__ == '__main__':
    Scanner3D().run()
