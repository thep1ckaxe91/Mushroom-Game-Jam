import pygame, os
from pygame._sdl2.video import Window, Texture, Image, Renderer
from scripts.CONST import Game_CONST #import first
from scripts.Camera import Camera
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
        self.transition_stack: list[SceneTransition] = []
        
        self.camera = Camera(self,pygame.Vector2())
        self.assets = {
            
        }

        self.dt = -1
        self.clock = pygame.time.Clock()
        self.refresh_rate = 60
        self.render_time = 0

    def update(self):
        self.clock.tick(Game_CONST.MAX_FPS)
        self.dt = self.clock.get_time() * 0.001

        Game_CONST.update(self)
        self.camera.update()
        self.scene_stack[-1].update()
        if len(self.transition_stack) > 0:
            self.transition_stack[-1].update()


    def draw(self):
        self.render_time += self.dt
        if self.render_time >= 1/self.refresh_rate:
            self.render_time -= 1/self.refresh_rate
            self.renderer.clear()

            if len(self.transition_stack) == 1:
                self.transition_stack[-1].draw()
            self.scene_stack[-1].draw()
            if len(self.transition_stack) == 2:
                self.transition_stack[-1].draw()

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
