import pygame
from pygame._sdl2.video import Renderer,Texture,Image
from typing import TYPE_CHECKING
from main import Game
from scripts.CONST import Game_CONST
from scripts.support_func import *
from scripts.support_func import Game
if TYPE_CHECKING:
    from main import Game
class Entity:

    def __init__(self,game : 'Game', wpos) -> None:
        self.game = game
        self.wpos = wpos
        self.dpos = world_to_display_pos(self.game, wpos)
    
    def update(self):
        self.dpos = world_to_display_pos(self.wpos)

    def draw(self):...

class Player(Entity):
    def __init__(self, game: 'Game', wpos) -> None:
        super().__init__(game, wpos)
    
    def update(self):
        super().update()
    
    def draw(self):
        ...