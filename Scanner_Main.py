from direct.showbase.ShowBase import ShowBase
from Scanner_KivyAPP import *
from math import pi, sin, cos
from direct.task import Task
from panda3d.core import loadPrcFileData
from direct.gui.DirectGui import *
from plyer import filechooser


ConfigData = """
window-title Scanner3D
win-size 960 540
background-color 0.41 0.41 0.41 0.0
icon-filename Btn_Voltar.png
"""

loadPrcFileData("",ConfigData) 

class PandaApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        self.kivy_app = kivy_app = Scanner_KivyAPP(self)
        kivy_app.run()

        # Add the spinCameraTask procedure to the task manager.
        self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")

    # Define a procedure to move the camera.
    def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont

    def processModel(self, Manequim):
        print("Calculando Volume")
        App.get_running_app().root.volumeModelo3D = 10



    def loadModel(self):
        try:
            self.manequim.removeNode()
        except:
            pass

        ModelPath = filechooser.open_file()[0]
        ModelPath = ModelPath[ModelPath.find('Assets'):]

        # The rest of your ShowBase code here
        # Load the environment model.
        self.manequim = self.loader.loadModel(ModelPath)
        # Reparent the model to render.
        self.manequim.reparentTo(self.render)
        # Apply scale and position transforms on the model.
        self.manequim.setHpr(0,90,0) 
        self.manequim.setScale(0.3, 0.3, 0.3)
        self.manequim.setPos(0, 0, 0)

        self.processModel(self.manequim)

app = PandaApp()

btn_loadmodel = DirectButton(text = "Inserir Modelo 3D",
                   command = app.loadModel,
                   pos = (0, 0, -0.9),
                   scale = 0.07)

app.run()