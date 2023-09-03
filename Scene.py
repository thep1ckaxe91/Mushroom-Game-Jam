import pygame, json
from CONST import Game_CONST
from UX_prop import *
from typing import TYPE_CHECKING
from pygame import freetype
from support_func import lerp

if TYPE_CHECKING:
    from main import Game
"""
draw func dont need clear and present, only need to pass the draw func
"""


class Scene:
    def __init__(self, game: "Game"):
        self.game = game

    def check_events(self):
        ...

    def update(self):
        ...

    def draw(self):
        ...


def load_scene(game: "Game", scene: Scene, delay: int = 0):
    """
    Delay 'delay' ms and load a scene
    """
    pygame.time.wait(delay)
    game.scene_stack.append(scene)


def go_back_scene(game: "Game"):
    game.scene_stack.pop(-1)


class Level(Scene):
    def __init__(self, game: "Game", data: dict):
        super().__init__(game)


class SaveFileChoose(Scene):
    def __init__(self, game: "Game"):
        super().__init__(game)

        self.game = game

        mountain_bg = pygame.image.load(
            Game_CONST.PATH + "/assets/graphics/general/mountain background.png"
        )
        mountain_bg.blit(
            pygame.image.load(
                Game_CONST.PATH + "/assets/graphics/general/mushroom cliff.png"
            ),
            (0, 0),
        )
        self.bg = Texture.from_surface(game.renderer, mountain_bg)

        self.save_datas = []
        for i in range(3):
            try:
                with open(Game_CONST.PATH + f"/saves/save{i}.json") as save_file:
                    self.save_datas.append(json.load(save_file))
            except:
                self.save_datas.append({})

        self.save_file_buttons: list[Button] = [
            Button(
                Game_CONST.PATH + "/assets/graphics/ux-ui/button/save_file",
                (
                    x * Game_CONST.SCR_WIDTH / 3 - Game_CONST.SCR_WIDTH / 6,
                    1.5 * Game_CONST.SCR_HEIGHT,
                ),
                self.game,
                print,  # place holder
                [f"save {x} chose"],
            )
            for x in range(1, 4)
        ]
        self.save_file_content: list[Texture] = []

        for save_file in self.save_datas:
            if save_file == {}:
                pass
            else:
                pass

        self.go_back = Button(
            Game_CONST.PATH + "/assets/graphics/ux-ui/button/back",
            (Game_CONST.SCR_WIDTH / 2, Game_CONST.SCR_HEIGHT - 100),
            self.game,
            go_back_scene,
            [self.game],
        )

    def update(self):
        for save_button in self.save_file_buttons:
            save_button.update()
            save_button.center_ratio_y = lerp(
                save_button.center_ratio_y, 0.5, 1 * self.game.dt
            )
        self.go_back.update()

    def draw(self):
        self.bg.draw(
            self.bg.get_rect(),
            pygame.Rect(0, 0, self.game.window.size[0], self.game.window.size[1]),
        )
        for save_button in self.save_file_buttons:
            save_button.draw()
        self.go_back.draw()


class MainMenu(Scene):
    def __init__(self, game: "Game"):
        super().__init__(game)

        mountain_bg = pygame.image.load(
            Game_CONST.PATH + "/assets/graphics/general/mountain background.png"
        )
        mountain_bg.blit(
            pygame.image.load(
                Game_CONST.PATH + "/assets/graphics/general/mushroom cliff.png"
            ),
            (0, 0),
        )
        self.main_menu_bg = Texture.from_surface(game.renderer, mountain_bg)
        self.play_button = Button(
            Game_CONST.PATH + "/assets/graphics/ux-ui/button/play",
            (Game_CONST.SCR_WIDTH * 3 / 4, Game_CONST.SCR_HEIGHT * 2 / 3),
            self.game,
            load_scene,  # placeholder
            [self.game, SaveFileChoose(self.game)],
        )

        self.options_button = Button(
            Game_CONST.PATH + "/assets/graphics/ux-ui/button/options",
            (
                Game_CONST.SCR_WIDTH * 3 / 4,
                Game_CONST.SCR_HEIGHT * 2 / 3 + Game_CONST.SCR_HEIGHT / 9,
            ),
            self.game,
            print,
            ["options"],
        )

        self.quit_button = Button(
            Game_CONST.PATH + "/assets/graphics/ux-ui/button/quit",
            (
                Game_CONST.SCR_WIDTH * 3 / 4,
                Game_CONST.SCR_HEIGHT * 2 / 3 + 2 * Game_CONST.SCR_HEIGHT / 9,
            ),
            self.game,
            exit,
            [0],
        )

    def update(self):
        self.play_button.update()
        self.options_button.update()
        self.quit_button.update()

    def draw(self):
        self.main_menu_bg.draw(
            self.main_menu_bg.get_rect(),
            pygame.Rect(0, 0, self.game.window.size[0], self.game.window.size[1]),
        )
        self.play_button.draw()
        self.options_button.draw()
        self.quit_button.draw()
