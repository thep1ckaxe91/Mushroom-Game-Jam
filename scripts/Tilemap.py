
from CONST import Game_CONST
from SpriteHandler import SpriteUnit

class Tile(SpriteUnit):
    

class Tilemap:
    def __init__(self):
        self.tile_size = Game_CONST.TILE_SIZE
        self.tile_map = {}
        self.offgrid_tiles = []