from random import randint
import pygame,math,sys,time,os,json
from scripts.CONST import Game_CONST
from scripts.support_func import *
from pygame import Vector2
from main import Game
pygame.init()
WIDTH,HEIGHT = 1366,768
window = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
CAMERA_CENTER = pygame.Vector2(WIDTH/2,HEIGHT/2)

level_id = int(input("level id (0->n): "))
level_dir = (Game_CONST.PATH + f"/assets/levels_map/level{level_id}")
physical_assets = {}
visible_assets = {}
temp_game = Game()
'''
Dictionary of all tiles that sliced from all sheet
'''
def load_json(directory, filename):
    filepath = os.path.join(directory, filename)
    if os.path.exists(filepath) and os.path.getsize(filepath) > 0:
        with open(filepath, 'r') as f:
            return json.load(f)
    else:
        return {}
pygame.mouse.set_visible(False)
os.makedirs(level_dir, exist_ok=True)

physical_dir = os.path.join(level_dir, "physical")
os.makedirs(physical_dir, exist_ok=True)
physical_tiles = load_json(physical_dir, "physical.json")

visible_dir = os.path.join(level_dir, "visible")
os.makedirs(visible_dir, exist_ok=True)
visible_tiles = load_json(visible_dir, "visible.json")

#current choosing to draw tile
cur_type = "grass"
cur_variant = 0
cur_tile_physic = "physical"
scroll = Vector2(0,0)
#load assets
for root, dirs, files in os.walk(Game_CONST.PATH + ('/assets/graphics/tiles')):
    if root == Game_CONST.PATH + ('/assets/graphics/tiles'):
        for dir in dirs:
            try:
                physical_assets[dir]: pygame.Surface = pygame.image.load(Game_CONST.PATH + (f'/assets/graphics/tiles/{dir}/physical/sheet.png')).convert()
            except:
                pass
            try:
                visible_assets[dir]: pygame.Surface = pygame.image.load(Game_CONST.PATH + (f'/assets/graphics/tiles/{dir}/visible/sheet.png')).convert()
            except:
                pass

def save():
    try:
        os.mkdir(level_dir+"/physical")
    except:
        print("physical dir existed")
    try:
        os.mkdir(level_dir+"/visible")
    except:
        print("visible dir existed")
    with open(level_dir+"/physical/physical.json",'w') as f:
        json.dump(physical_tiles,f)
        
    with open(level_dir+"/visible/visible.json",'w') as f:
        json.dump(visible_tiles,f)
pressing = False
def update():
    global scroll,pressing
    if pygame.mouse.get_pressed()[0]:
        mp = pygame.mouse.get_pos()
        wmp = display_to_world_pos(temp_game,mp)
        wmp.x//=Game_CONST.TILE_SIZE
        wmp.y//=Game_CONST.TILE_SIZE
        tile_pos=str(wmp.x)+','+str(wmp.y)
        if cur_tile_physic == "physical":
            physical_tiles[tile_pos]={"type": cur_type, "variant": cur_variant}
        else:
            visible_tiles[tile_pos]={"type": cur_type, "variant": cur_variant}
    elif pygame.mouse.get_pressed()[2] and not pressing:
        pressing = True
        pygame.mouse.get_rel()
    elif pygame.mouse.get_pressed()[2] and pressing:
        scroll += Vector2(pygame.mouse.get_rel())

def draw_tile(tile: (str,dict),assets: dict):
    pos = Vector2(tuple(map(float,tile[0].split(','))))*Game_CONST.TILE_SIZE
    pos += scroll
    sheet = assets[tile[1]["type"]]
    variant = tile[1]["variant"]
    r_area = pygame.Rect((variant%(sheet.get_width()//Game_CONST.TILE_SIZE))*Game_CONST.TILE_SIZE,variant*Game_CONST.TILE_SIZE//sheet.get_width()*Game_CONST.TILE_SIZE,Game_CONST.TILE_SIZE,Game_CONST.TILE_SIZE)
    window.blit(sheet,pos,r_area)

def draw_tiles(tiles: dict, assets: dict):
    for tile in tiles.items():
        draw_tile(tile,assets)
def draw():
    window.fill("black")
    #draw map
    draw_tiles(physical_tiles,physical_assets)
    draw_tiles(visible_tiles,visible_assets)
    #draw cursor
    mp = pygame.mouse.get_pos()
    wmp = display_to_world_pos(temp_game,mp)
    wmp.x//=Game_CONST.TILE_SIZE
    wmp.y//=Game_CONST.TILE_SIZE
    tile_pos=str(wmp.x)+','+str(wmp.y)
    if cur_tile_physic == "physical":
        #cursor
        draw_tile((tile_pos,{"type" : cur_type, "variant" : cur_variant}), physical_assets)
        #cur tile
        sheet = physical_assets[cur_type]
        r_area = pygame.Rect((cur_variant%(sheet.get_width()//Game_CONST.TILE_SIZE))*Game_CONST.TILE_SIZE,cur_variant*Game_CONST.TILE_SIZE//sheet.get_width()*Game_CONST.TILE_SIZE,Game_CONST.TILE_SIZE,Game_CONST.TILE_SIZE)
        pos = (10,10)
        tmp_surf = pygame.Surface((Game_CONST.TILE_SIZE,Game_CONST.TILE_SIZE),pygame.SRCALPHA)
        tmp_surf.set_alpha(100)
        tmp_surf.blit(sheet,(0,0),r_area)
        tmp_surf = pygame.transform.scale_by(tmp_surf,3)
        window.blit(tmp_surf,pos)
    else:
        #cursor
        draw_tile((tile_pos,{"type" : cur_type, "variant" : cur_variant}), visible_assets)
        #cur tile
        sheet = visible_assets[cur_type]
        r_area = pygame.Rect((cur_variant%(sheet.get_width()//Game_CONST.TILE_SIZE))*Game_CONST.TILE_SIZE,cur_variant*Game_CONST.TILE_SIZE//sheet.get_width()*Game_CONST.TILE_SIZE,Game_CONST.TILE_SIZE,Game_CONST.TILE_SIZE)
        pos = (10,10)
        tmp_surf = pygame.Surface((Game_CONST.TILE_SIZE,Game_CONST.TILE_SIZE),pygame.SRCALPHA)
        tmp_surf.set_alpha(100)
        tmp_surf.blit(sheet,(0,0),r_area)
        tmp_surf = pygame.transform.scale_by(tmp_surf,3)
        window.blit(tmp_surf,pos)
    pygame.display.flip()

if __name__ == "__main__":
    while True:
        for event in pygame.event.get():    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSLASH:
                    save()
                    print("saved")
                elif event.key == pygame.K_0:
                    save()
                    print("level saved")
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_p:
                    cur_tile_physic = "physical"
                    cur_variant = 0
                elif event.key == pygame.K_v:
                    cur_tile_physic = "visible"
                    cur_variant = 0
                elif event.key == pygame.K_a or event.key == pygame.K_d:
                    keys = pygame.key.get_pressed()
                    cur_variant += keys[pygame.K_d] - keys[pygame.K_a]
                    if cur_tile_physic == "physical":
                        w = physical_assets[cur_type].get_width()//Game_CONST.TILE_SIZE
                        h = physical_assets[cur_type].get_height()//Game_CONST.TILE_SIZE
                    else:
                        w = visible_assets[cur_type].get_width()//Game_CONST.TILE_SIZE
                        h = visible_assets[cur_type].get_height()//Game_CONST.TILE_SIZE
                    cur_variant = int(pygame.math.clamp(cur_variant,0,w*h-1))
            elif event.type == pygame.MOUSEBUTTONUP:
                pressing = False

        update()
        draw()
        pygame.display.flip()
        clock.tick(100)

'''
A/D to change tile
V and P to switch between visible and physical
Left mouse to draw
Right mouse to drag
'''