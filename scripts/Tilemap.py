
from CONST import Game_CONST
from SpriteHandler import SpriteUnit
from scripts.SpriteHandler import SpriteHandler

# class Tile(SpriteUnit):
#     def __init__(self, handler: SpriteHandler):
#         super().__init__(handler)
#         self.image = 

class Tilemap:
    def __init__(self):
        self.tile_size = Game_CONST.TILE_SIZE
        self.tile_map = {}
        self.offgrid_tiles = []