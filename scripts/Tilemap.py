from CONST import Game_CONST
from pygame._sdl2.video import Renderer
from scripts.support_func import *
from pygame import Vector2
class Tilemap:
    def __init__(self, game: 'Game',data : dict):
        self.game = game
        self.tile_size = Game_CONST.TILE_SIZE
        self.physical_tile_map = data['physical']
        self.visible_tile_map = data['visible']

    def render(self, renderer: Renderer):
        for pos in self.visible_tile_map:
            tile = self.visible_tile_map[pos]
            sheet = self.game.assets['visible'][tile["type"]]
            variant = tile["variant"]
            w_pos = Vector2(tuple(map(float,pos.split(','))))*self.tile_size
            r_area = pygame.Rect((variant%(sheet.get_width()//self.tile_size))*self.tile_size,variant*self.tile_size//sheet.get_width()*self.tile_size,self.tile_size,self.tile_size)
            renderer.blit(sheet,world_to_display_pos(self.game,w_pos),r_area)
        for pos in self.physical_tile_map:
            tile = self.physical_tile_map[pos]
            sheet = self.game.assets['physical'][tile["type"]]
            variant = tile["variant"]
            w_pos = Vector2(tuple(map(float,pos.split(','))))*self.tile_size
            r_area = pygame.Rect((variant%(sheet.get_width()//self.tile_size))*self.tile_size,variant*self.tile_size//sheet.get_width()*self.tile_size,self.tile_size,self.tile_size)
            renderer.blit(sheet,world_to_display_pos(self.game,w_pos),r_area)