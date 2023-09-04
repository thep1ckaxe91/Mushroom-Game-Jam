import pygame,os
from CONST import Game_CONST
from pygame._sdl2.video import Texture,Image
from support_func import *
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from main import Game

class SpriteHandler:
    def __init__(self, game : "Game", path : str):
        self.game = game
        self.images = load_images(game.renderer, path)
        self.group = pygame.sprite.Group()
        self.sprites = []
    
    def update(self): ...

    def draw(self): ...

class SpriteUnit(pygame.sprite.Sprite):
    def __init__(self, handler : SpriteHandler):
        self.handler = handler
        super().__init__(handler.group)
        self.image_id = len(handler.sprites) - 1
        self.image = Image(handler.images[self.image_id])
        self.rect = self.image.get_rect()
        
    def update(self): ...