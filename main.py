import pygame, os
from pygame._sdl2.video import Window, Texture, Image, Renderer
from scripts.CONST import Game_CONST #import first

from scripts.Scene import *

pygame.init()


class Game:
    def __init__(self):
        self.window = Window(
            Game_CONST.GAME_NAME, (Game_CONST.SCR_WIDTH, Game_CONST.SCR_HEIGHT)
        )
        self.window.resizable = True
        self.renderer = Renderer(self.window)
        self.scene_stack: list[Scene] = [MainMenu(self)]

        self.dt = -1
        self.clock = pygame.time.Clock()

    def update(self):
        self.clock.tick(Game_CONST.MAX_FPS)
        self.dt = self.clock.get_time() * 0.001

        Game_CONST.update(self)
        self.scene_stack[-1].update()

    def draw(self):
        self.renderer.clear()

        self.scene_stack[-1].draw()

        self.renderer.present()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.VIDEORESIZE:
                    Game_CONST.resize_update(self)
                self.scene_stack[-1].check_events(event)
            self.update()
            self.draw()

        pygame.quit()
        self.window.destroy()


if __name__ == "__main__":
    game = Game()
    game.run()
