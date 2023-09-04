import pygame, json
from scripts.CONST import Game_CONST
from scripts.UX_prop import *
from typing import TYPE_CHECKING
from pygame import freetype
from scripts.support_func import *

freetype.init()

if TYPE_CHECKING:
    from main import Game
"""
draw func dont need clear and present, only need to pass the draw func

event will be pass, do the if else only
"""


class Scene:
    def __init__(self, game: "Game"):
        self.game = game

    def check_events(self, event : pygame.event.Event):
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
    del game.scene_stack[-1]

'''
  _____  _                   _     _        _                    _ 
 |  __ \| |                 | |   | |      | |                  | |
 | |__) | | __ _ _   _  __ _| |__ | | ___  | |     _____   _____| |
 |  ___/| |/ _` | | | |/ _` | '_ \| |/ _ \ | |    / _ \ \ / / _ \ |
 | |    | | (_| | |_| | (_| | |_) | |  __/ | |___|  __/\ V /  __/ |
 |_|    |_|\__,_|\__, |\__,_|_.__/|_|\___| |______\___| \_/ \___|_|
                  __/ |                                            
                 |___/                                             
'''

class Level(Scene):
    def __init__(self, game: "Game", data: dict):
        super().__init__(game)
        pass

'''
   _____      _      _____                     
  / ____|    | |    / ____|                    
 | |    _   _| |_  | (___   ___ ___ _ __   ___ 
 | |   | | | | __|  \___ \ / __/ _ \ '_ \ / _ \
 | |___| |_| | |_   ____) | (_|  __/ | | |  __/
  \_____\__,_|\__| |_____/ \___\___|_| |_|\___|
                                               
                                               
'''

class CutScene(Scene):
    def __init__(self, game: 'Game'):
        super().__init__(game)


'''
   _____ _                             _____                   ______ _ _      
  / ____| |                           / ____|                 |  ____(_) |     
 | |    | |__   ___   ___  ___  ___  | (___   __ ___   _____  | |__   _| | ___ 
 | |    | '_ \ / _ \ / _ \/ __|/ _ \  \___ \ / _` \ \ / / _ \ |  __| | | |/ _ \
 | |____| | | | (_) | (_) \__ \  __/  ____) | (_| |\ V /  __/ | |    | | |  __/
  \_____|_| |_|\___/ \___/|___/\___| |_____/ \__,_| \_/ \___| |_|    |_|_|\___|
                                                                               
                                                                               
'''

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
                self.save_datas.append(Game_CONST.new_game_data.copy())

        self.save_file_buttons: list[Button] = [
            Button(
                Game_CONST.PATH + "/assets/graphics/ux-ui/button/save_file",
                (
                    x * Game_CONST.SCR_WIDTH / 3 - Game_CONST.SCR_WIDTH / 6,
                    1.5 * Game_CONST.SCR_HEIGHT,
                ),
                self.game,
                load_scene,  # place holder
                [self.game, Level(self.game, self.save_datas[x-1])],
            )
            for x in range(1, 4)
        ]
        self.save_file_content: list[list[Texture|  pygame.Rect]] = [[],[],[]]

        self.go_back = Button(
            Game_CONST.PATH + "/assets/graphics/ux-ui/button/back",
            (Game_CONST.SCR_WIDTH / 2, Game_CONST.SCR_HEIGHT - 100),
            self.game,
            go_back_scene,
            [self.game],
        )
        # make context for save file
        for i,save_file in enumerate(self.save_datas):
            if save_file == Game_CONST.new_game_data:
                message_surf,message_rect = freetype.Font(Game_CONST.PATH + '/assets/font/basis33.ttf',Game_CONST.FONT_SCALE * 16).render(
                    "Start New Game",
                    pygame.Color("white")
                )
                message_rect.center = self.save_file_buttons[i].hitbox.center
                self.save_file_content[i] = [Texture.from_surface(self.game.renderer, message_surf),message_rect]
            else:
                pass


    def update(self):
        for save_button in self.save_file_buttons:
            save_button.update()
            save_button.center_ratio_y = lerp(
                save_button.center_ratio_y, 0.5, 5 * self.game.dt
            )
        self.go_back.update()
        for i,texture_rect in enumerate(self.save_file_content):
            texture_rect[1].center = self.save_file_buttons[i].hitbox.center
            texture_rect[1].width,texture_rect[1].height = [x * Game_CONST.FONT_SCALE for x in texture_rect[0].get_rect().size]

    def draw(self):
        self.bg.draw(
            self.bg.get_rect(),
            pygame.Rect(0, 0, self.game.window.size[0], self.game.window.size[1]),
        )
        for save_button in self.save_file_buttons:
            save_button.draw()
        for save_texture, texture_rect in self.save_file_content:
            save_texture.draw(texture_rect,texture_rect)
            print(texture_rect)
        self.go_back.draw()

    def check_events(self, event):
        if event.type == pygame.MOUSEBUTTONUP and self.go_back.hitbox.collidepoint(pygame.mouse.get_pos()):
            for save_file in self.save_file_buttons:
                save_file.center_ratio_y = 1.5



'''

  __  __       _         __  __                  
 |  \/  |     (_)       |  \/  |                 
 | \  / | __ _ _ _ __   | \  / | ___ _ __  _   _ 
 | |\/| |/ _` | | '_ \  | |\/| |/ _ \ '_ \| | | |
 | |  | | (_| | | | | | | |  | |  __/ | | | |_| |
 |_|  |_|\__,_|_|_| |_| |_|  |_|\___|_| |_|\__,_|
                                                 
                                                 

'''


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
