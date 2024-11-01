from direct.showbase.ShowBase import ShowBase
from example import *


from math import pi, sin, cos

from direct.task import Task


class PandaApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        display_region = self.win.make_display_region(0, 0.25, 0, 1)

        self.kivy_app = kivy_app = Example(self)
        kivy_app.run()

        # The rest of your ShowBase code here
        # Load the environment model.
        self.manequim = self.loader.loadModel("manequim.obj")
        # Reparent the model to render.
        self.manequim.reparentTo(self.render)
        # Apply scale and position transforms on the model.
        self.manequim.setHpr(0,90,0) 
        self.manequim.setScale(0.3, 0.3, 0.3)
        self.manequim.setPos(0, 0, 0)
        
        # Add the spinCameraTask procedure to the task manager.
        self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")

    # Define a procedure to move the camera.
    def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont

app = PandaApp()
app.run()

