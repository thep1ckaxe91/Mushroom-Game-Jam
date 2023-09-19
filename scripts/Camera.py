import random
import pygame
from pygame._sdl2.video import Window,Image,Texture,Renderer
from typing import TYPE_CHECKING
from scripts.CONST import Game_CONST
if TYPE_CHECKING:
    from main import Game

class Camera:

    def __init__(self,game:'Game', topleft : pygame.Vector2) -> None:
        self.game = game
        self.w_pos = topleft
        '''world pos, all update pos should be through org_center'''
        self.camera_center: pygame.Vector2 = topleft + pygame.Vector2(Game_CONST.CAMERA_WIDTH/2,Game_CONST.CAMERA_HEIGHT/2)
        '''use to draw only'''
        self.org_center: pygame.Vector2 = self.camera_center
        '''use to update only'''
        self.width = Game_CONST.CAMERA_WIDTH
        self.height = Game_CONST.CAMERA_HEIGHT
        self.size = pygame.Vector2(self.width,self.height)
        self.screen_shake_time = 0
        '''in second'''
        self.shake_max_offset = 0

        self.follow_max_offset = 70
        '''offset of the camera relative to player's current direction'''
        self.follow_current_dir = pygame.Vector2()
        self.follow_current_len = 0
        self.follow_speed = 500
        self.rect = pygame.Rect(*self.w_pos,*self.size)

    
    def update(self):
        self.width = Game_CONST.CAMERA_WIDTH
        self.height = Game_CONST.CAMERA_HEIGHT
        self.size = pygame.Vector2(self.width,self.height)
        self.w_pos = self.org_center - self.size/2
        self.rect = pygame.Rect(*self.w_pos,*self.size)
        self.screen_shaking(self.shake_max_offset)
        self.follow_dir()

    def follow_dir(self):
        self.follow_current_len += self.follow_speed * self.game.dt * (not self.follow_current_dir == (0,0))
        pygame.math.clamp(self.follow_current_len,0,self.follow_max_offset)
        if self.follow_current_dir != (0,0):
            self.follow_current_dir.scale_to_length(self.follow_current_len)
        self.camera_center = self.org_center + self.follow_current_dir

    def screen_shaking(self, max_offset = 0):
        if self.screen_shake_time > 0:
            shake_offset = (random.randint(0,max_offset),random.randint(0,max_offset))
            self.camera_center = self.org_center + shake_offset
            self.screen_shake_time -= self.game.dt