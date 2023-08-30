import pygame
from CONST import Game_CONST
from UX_prop import *
from typing import TYPE_CHECKING

from main import Game
if TYPE_CHECKING:
    from main import Game
'''
draw func dont need clear and present, only need to pass the draw func
'''
class Scene:
    def __init__(self,game : Game):
        self.game = game
    def check_events(self): ...
    def update(self): ...
    def draw(self): ...

class Level(Scene):
    def __init__(self, game: Game):
        super().__init__(game)

class MainMenu(Scene):
    def __init__(self, game: Game):
        super().__init__(game)
        
        play_button_pos = (Game_CONST.SCR_WIDTH/2,Game_CONST.SCR_HEIGHT*2/3)
        self.play_button = Button(Game_CONST.PATH + '/assets/graphics/ux-ui/button/play',play_button_pos,self.game,print,('worked!'))
    
    def update(self):
        self.play_button.update()
    
    def draw(self):
        self.play_button.draw()
