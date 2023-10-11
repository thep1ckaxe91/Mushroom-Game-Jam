import os
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from main import Game

class GAME_CONST:
    
    new_game_data = {
        "level" : {
            "id" : 1,
            "check_point" : 1
        }
    }
    EDGE_ADJECTION_DIR = [
        (0,1),
        (1,0),
        (0,-1),
        (-1,0)
    ]
    CORNER_ADJECTION_DIR = [
        (1,1),
        (1,-1),
        (-1,-1),
        (-1,1)
    ]
    def __init__(self) -> None:
        self.PATH = os.path.abspath(os.path.dirname(__file__)).replace("\\","/") + "/.."
        self.GAME_NAME = "Mushroom Apocalypse"
        self.MAX_FPS = 100

        self.TILE_SIZE = 16
        self.CAMERA_WIDTH,self.CAMERA_HEIGHT = 1600,900
        self.SCR_WIDTH,self.SCR_HEIGHT = 1600,900
        # self.camera_screen_ratio = 1

        self.SCR_SCALE = 5
        self.SCALE = self.SCR_SCALE

        self.BASE_FONT_SCALE = 5
        self.UI_SCALE = 1

        self.physical_assets = {}
        self.visible_assets = {}

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

        self.UI_SCALE = self.SCR_WIDTH / 1600 * self.SCR_SCALE


Game_CONST = GAME_CONST()
        