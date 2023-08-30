import pygame as pg
from pygame._sdl2 import Window, Renderer, Texture

pg.init()
win = Window("My Window", resizable=True)
renderer = Renderer(win)

# Load the image as a Surface object
image_surface = pg.image.load("assets/graphics/general/mage.png")

# Create a Texture from the Surface object
image_texture = Texture.from_surface(renderer, image_surface)
