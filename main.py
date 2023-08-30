import pygame,os
from pygame._sdl2.video import Window,Texture,Image,Renderer
from CONST import GAME_CONST
from Scene import *

class Game:

    def __init__(self):
        self.window = Window(GAME_CONST.GAME_NAME,(GAME_CONST.SCR_WIDTH,GAME_CONST.SCR_HEIGHT),fullscreen=True)
        self.renderer = Renderer(self.window)
        self.current_scene : Scene = MainMenu()

        self.dt = -1
        self.clock = pygame.time.Clock()

    def update(self):
        self.clock.tick(GAME_CONST.MAX_FPS)
        self.dt = self.clock.get_rawtime()*0.001
        
        self.current_scene.update(self)
        GAME_CONST.update()

    def draw(self):
        self.renderer.clear()

        self.current_scene.draw(self)

        self.renderer.present()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
            self.update()
            self.draw()

if __name__ == "__main__":
    game = Game()
    game.run()
