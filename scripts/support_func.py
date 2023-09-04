import os, pygame
from scripts.CONST import Game_CONST
from pygame._sdl2.video import Texture, Renderer


def lerp(a: float, b: float, weight: float) -> float:
    return a + (b - a) * weight


def load_image(renderer: Renderer, path) -> Texture:
    return Texture.from_surface(renderer, pygame.image.load(path))


def load_images(renderer: Renderer, path) -> list[Texture]:
    paths = []
    for _,_, files in os.walk(path):
        for file in files:
            paths.append(Game_CONST.PATH + "/" + file)
    return [Texture.from_surface(renderer, pygame.image.load(_path)) for _path in paths]
