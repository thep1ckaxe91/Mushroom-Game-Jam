import pygame
from CONST import GAME_CONST
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
    
    def check_events(self):
        for event in pygame.event.get():
            pass