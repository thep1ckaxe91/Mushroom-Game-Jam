import pygame
from CONST import Game_CONST
from UX_prop import *
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from main import Game
'''
draw func dont need clear and present, only need to pass the draw func
'''
class Scene:
    def __init__(self,game : 'Game'):
        self.game = game
    def check_events(self): ...
    def update(self): ...
    def draw(self): ...

class Level(Scene):
    def __init__(self, game: 'Game'):
        super().__init__(game)

class MainMenu(Scene):
    def __init__(self, game: 'Game'):
        super().__init__(game)
        
        self.main_menu_bg = Texture.from_surface(game.renderer,pygame.image.load(Game_CONST.PATH + '/assets/graphics/general/main_menu_background.png'))
        self.play_button = Button(Game_CONST.PATH + '/assets/graphics/ux-ui/button/play',(Game_CONST.SCR_WIDTH/2,Game_CONST.SCR_HEIGHT*2/3),self.game,print,['worked!'])
        self.options_button = Button(Game_CONST.PATH + '/assets/graphics/ux-ui/button/options')    


    def update(self):
        self.play_button.update()


    def draw(self):
        self.main_menu_bg.draw(self.main_menu_bg.get_rect(),pygame.Rect(0,0,self.game.window.size[0], self.game.window.size[1]))
        self.play_button.draw()
