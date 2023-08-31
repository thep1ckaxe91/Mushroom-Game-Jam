import pygame, os
from pygame._sdl2.video import Window, Texture, Image, Renderer
from CONST import Game_CONST
from Scene import *

pygame.init()


class Game:
    def __init__(self):
        self.window = Window(
            Game_CONST.GAME_NAME, (Game_CONST.SCR_WIDTH, Game_CONST.SCR_HEIGHT)
        )
        self.window.position = [0,0]
        self.window.resizable = True
        self.renderer = Renderer(self.window)
        self.current_scene: Scene = MainMenu(self)

        self.dt = -1
        self.clock = pygame.time.Clock()

    def update(self):
        self.clock.tick(Game_CONST.MAX_FPS)
        self.dt = self.clock.get_time() * 0.001

        Game_CONST.update(self)
        self.current_scene.update()

    def draw(self):
        self.renderer.clear()

        self.current_scene.draw()

        self.renderer.present()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.VIDEORESIZE:
                    Game_CONST.resize_update(self)
            self.update()
            self.draw()

        pygame.quit()
        self.window.destroy()


if __name__ == "__main__":
    game = Game()
    game.run()
