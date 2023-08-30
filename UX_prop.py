import pygame
from pygame._sdl2.video import Texture,Image
from CONST import Game_CONST
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from main import Game

class Button:
    
    def __init__(self, path, center_pos, game : 'Game', func : 'function', args : tuple | list) -> None:
        self.game = game
        self.default = Texture.from_surface(game.renderer,pygame.image.load(path+'/default.png'))
        self.hang = Texture.from_surface(game.renderer,pygame.image.load(path+'/hang.png'))
        self.press = Texture.from_surface(game.renderer,pygame.image.load(path+'/press.png'))
        self.current_state = 0
        self.previous_state = 0
        self.center_pos = center_pos
        self.hitbox : pygame.Rect = self.default.get_rect(center = center_pos)
        self.func = func
        self.args = args

    def update(self):

        self.hitbox.w = self.default.get_rect().w * Game_CONST.SCALE
        self.hitbox.h = self.default.get_rect().h * Game_CONST.SCALE
        self.hitbox.center = self.center_pos

        self.current_state = 0
        if self.hitbox.collidepoint(pygame.mouse.get_pos()):
            self.current_state = 1
            if pygame.mouse.get_pressed()[0]:
                self.current_state = 2

        if self.previous_state == 2 and self.current_state == 0:
            self.func(*self.args)
            
        self.previous_state = self.current_state

            
    def draw(self):
        if self.current_state == 0:
            self.default.draw(self.default.get_rect(),self.hitbox)
        elif self.current_state == 1:
            self.hang.draw(self.hang.get_rect(),self.hitbox)
        else:
            self.press.draw(self.press.get_rect(),self.hitbox)