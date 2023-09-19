import pygame,os
from pygame._sdl2.video import Renderer,Texture,Image
from scripts.CONST import Game_CONST
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from main import Game

class Animation:

    def __init__(self, game: 'Game', path, frame_time = 0.1, loop = False) -> None:
        '''
        path lead to the folder contain only the animation images
        frame_time is the time between switching sprite in second
        loop determine whether the animation is looping or not
        '''
        self.game = game
        self.images: list[Image] = []
        for _,__,files in os.walk(Game_CONST.PATH + path):
            for image_name in files:
                self.images.append(
                    Image(Texture.from_surface(
                        self.game.renderer,
                        pygame.image.load(Game_CONST.PATH + path + "/" + image_name)
                    ))
                )
        self.image_id = 0
        self.frame_time = frame_time
        self.frame_time_count = 0
        
    def update(self):
        self.frame_time_count += self.game.dt
        if self.frame_time_count >= self.frame_time:
            self.image_id = (self.image_id + 1)%len(self.images)
            self.frame_time_count -= self.frame_time