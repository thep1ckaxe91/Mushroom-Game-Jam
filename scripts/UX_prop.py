import pygame
from pygame import freetype
from pygame._sdl2.video import Texture,Image
from scripts.CONST import Game_CONST
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from main import Game

class Button:
    
    def __init__(self, path, center_pos, game : 'Game', func : 'function', args : list) -> None:
        self.game = game
        self.default = Texture.from_surface(game.renderer,pygame.image.load(path+'/default.png'))
        self.hang = Texture.from_surface(game.renderer,pygame.image.load(path+'/hang.png'))
        self.press = Texture.from_surface(game.renderer,pygame.image.load(path+'/press.png'))
        self.current_state = 0
        self.previous_state = 0
        self.center_ratio_x,self.center_ratio_y = center_pos[0]/game.window.size[0], center_pos[1]/game.window.size[1]
        self.hitbox : pygame.Rect = self.default.get_rect(center = center_pos)
        self.func = func
        self.args = args
        self.isClicking = False

    def update(self):
        self.hitbox.w = self.default.get_rect().w * Game_CONST.SCALE
        self.hitbox.h = self.default.get_rect().h * Game_CONST.SCALE
        self.hitbox.center = self.center_ratio_x * self.game.window.size[0], self.center_ratio_y * self.game.window.size[1]

        self.current_state = 0
        if self.hitbox.collidepoint(pygame.mouse.get_pos()):
            self.current_state = 1
            if pygame.mouse.get_pressed()[0]:
                self.current_state = 2

        self.isClicking = False
        if self.previous_state == 2 and self.current_state == 1:
            self.isClicking = True
            self.func(*self.args)
            
        self.previous_state = self.current_state
            
    def draw(self):
        if self.current_state == 0:
            self.default.draw(self.default.get_rect(),self.hitbox)
        elif self.current_state == 1:
            self.hang.draw(self.hang.get_rect(),self.hitbox)
        else:
            self.press.draw(self.press.get_rect(),self.hitbox)
class Text:

    def __init__(self, game: "Game", text: str, center_pos, font: str, text_color = None, bgcolor = None, font_size = 0, rotation = 0) -> None:
        self.game = game
        self.text = text
        self.font = font
        self.text_color = text_color
        self.bgcolor = bgcolor
        self.font_size = font_size
        self.rotation = rotation
        self.center_pos = center_pos
        self.text_surf,self.text_rect = freetype.Font(Game_CONST.PATH + '/assets/font/' + self.font.replace("/",""),self.font_size * Game_CONST.FONT_SCALE).render(
            text,
            text_color,
            bgcolor,
            rotation = self.rotation,
            size = self.font_size
        )
        self.texture = Texture.from_surface(game.renderer,self.text_surf)
    
    def custom_update(self, text = None ,font = None , text_color = None , bgcolor = None , font_size = None , rotation = None):
        if text is None:
            text = self.text
        if font is None:
            font = self.font
        if text_color is None:
            text_color = self.text_color
        if bgcolor is None:
            bgcolor = self.bgcolor
        if font_size is None:
            font_size = self.font_size
        if rotation is None:
            rotation = self.rotation
        self.text_surf, self.text_rect = freetype.Font(Game_CONST.PATH + '/assets/font/' + self.font.replace("/",""),self.font_size * Game_CONST.FONT_SCALE).render(
            text,
            text_color,
            bgcolor,
            rotation = rotation,
            size = font_size
        )
        self.texture.update(self.text_surf)

    def update(self):
        self.text_rect.w, self.text_rect.h = [x * Game_CONST.FONT_SCALE for x in self.texture.get_rect().size]
        self.text_rect.center = self.center_pos
    
    def draw(self):
        self.texture.draw(self.texture.get_rect(),self.text_rect)