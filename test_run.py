import pygame
import pygame.freetype as ft
import sys,math,os
from pygame._sdl2.video import Window,Texture,Image,Renderer

class App:

    def __init__(self,WIN_SIZE = [1366,768],Title = "pygame") -> None:
        self.window = Window(title=Title,size = WIN_SIZE)
        self.renderer1 = Renderer(self.window)
        self.renderer2 = Renderer(self.window)
        self.clock = pygame.time.Clock()
        self.dt = 0.0

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    def update(self):
        self.clock.tick()
        self.dt = 1/max(10**-6,self.clock.get_fps())

    def draw(self):
        rect1 = pygame.Rect(100,100,200,200)
        rect2 = pygame.Rect(200,200,300,300)
        self.renderer1.clear()
        
        self.renderer1.draw_color = pygame.Color("red")
        self.renderer1.fill_rect(rect1)

        self.renderer1.present()
        self.renderer2.clear()
        
        self.renderer1.draw_color = pygame.Color("blue")
        self.renderer1.fill_rect(rect2)

        self.renderer2.present()
    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == "__main__":
    app = App()
    app.run()