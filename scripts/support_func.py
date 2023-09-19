import os, pygame, math
from scripts.CONST import Game_CONST
from pygame._sdl2.video import Texture, Renderer
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from main import Game


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

def fill_diagnal_square(renderer: Renderer, position: pygame.Vector2, size: float):
    renderer.draw_color = pygame.Color("black")
    renderer.fill_quad(
        *[position + pygame.Vector2(offset)*(size/math.sqrt(2)) for offset in Game_CONST.EDGE_ADJECTION_DIR]
    )

def world_to_display_pos(game: 'Game',w_pos: pygame.Vector2):
    return w_pos - game.camera.w_pos

# def is_in_sight(game: 'Game', )