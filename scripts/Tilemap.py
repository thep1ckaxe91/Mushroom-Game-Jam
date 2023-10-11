
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
        self.physical_tile_map = {}
        self.visible_tile_map = {}
        '''template'''
        '''
        {
            "16,59" : {
                "type" : 
            }
        }
        '''

        self.offgrid_tiles = []