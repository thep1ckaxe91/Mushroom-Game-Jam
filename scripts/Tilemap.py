from CONST import Game_CONST
from pygame._sdl2.video import Renderer
from scripts.support_func import *
from pygame import Vector2
class Tilemap:
    def __init__(self, game: 'Game'):
        self.game = game
        self.tile_size = Game_CONST.TILE_SIZE
        self.physical_tile_map = {}
        self.visible_tile_map = {}
        self.decorative_tile_map = {}

    def render(self, renderer: Renderer):
        for pos in self.visible_tile_map:
            tile = self.visible_tile_map[pos]
            pos = Vector2(tuple(map(float,tile[0].split(','))))*Game_CONST.TILE_SIZE
            sheet = self.game.assets['visible'][tile[1]["type"]]
            variant = tile[1]["variant"]
            r_area = pygame.Rect((variant%(sheet.get_width()//Game_CONST.TILE_SIZE))*Game_CONST.TILE_SIZE,variant*Game_CONST.TILE_SIZE//sheet.get_width()*Game_CONST.TILE_SIZE,Game_CONST.TILE_SIZE,Game_CONST.TILE_SIZE)
            renderer.blit(sheet)