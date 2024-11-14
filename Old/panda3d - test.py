from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task


class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

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


app = MyApp()
app.run()