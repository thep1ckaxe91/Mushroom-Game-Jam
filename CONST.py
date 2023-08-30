import os
class GAME_CONST:
    PATH = os.path.abspath(os.path.dirname(__file__))
    GAME_NAME = "Mushroom Adventure"
    MAX_FPS = 100

    TILE_SIZE = 16
    CAMERA_WIDTH,CAMERA_HEIGHT = 1600,900
    SCR_WIDTH,SCR_HEIGHT = 1600,900
    SCR_SCALE = 5
    SCALE = SCR_SCALE


    def update(self):
        self.SCR_HEIGHT,self.SCR_WIDTH = int(self.SCR_HEIGHT),int(self.SCR_WIDTH)
        self.CAMERA_WIDTH,self.CAMERA_HEIGHT = int(self.CAMERA_WIDTH),int(self.CAMERA_HEIGHT)
        self.SCALE = int(self.SCR_WIDTH/self.CAMERA_WIDTH*self.SCR_SCALE)
        