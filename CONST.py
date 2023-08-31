import os
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from main import Game

class GAME_CONST:
    

    def __init__(self) -> None:
        self.PATH = os.path.abspath(os.path.dirname(__file__)).replace("\\","/")
        self.GAME_NAME = "Mushroom Adventure"
        self.MAX_FPS = 100

        self.TILE_SIZE = 16
        self.CAMERA_WIDTH,self.CAMERA_HEIGHT = 1600,900
        self.SCR_WIDTH,self.SCR_HEIGHT = 1600,900
        self.camera_screen_ratio = 1

        self.SCR_SCALE = 5
        self.SCALE = self.SCR_SCALE

    def resize_update(self,game : 'Game'):
        self.SCR_WIDTH = game.window.size[0]
        # self.CAMERA_WIDTH = self.camera_screen_ratio * self.SCR_WIDTH

    def update(self,game : 'Game'):
        self.SCR_WIDTH = int(self.SCR_WIDTH)
        self.SCR_HEIGHT = int(9*self.SCR_WIDTH/16)
        game.window.size = self.SCR_WIDTH,self.SCR_HEIGHT
        self.CAMERA_WIDTH = int(self.CAMERA_WIDTH)
        self.CAMERA_HEIGHT = int(9*self.CAMERA_WIDTH/16)

        # self.camera_screen_ratio = self.CAMERA_WIDTH/self.SCR_WIDTH

        self.SCALE = self.SCR_WIDTH/self.CAMERA_WIDTH*self.SCR_SCALE

Game_CONST = GAME_CONST()
        