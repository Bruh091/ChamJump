import pygame as pg
from random import randint
from copy import copy
pg.init()
pg.mixer.init()
pg.font.init()
class GameSprite(pg.sprite.Sprite):
    def __init__(self,img,w,h,x,y):
        self.image = pg.transform.scale(pg.image.load(img),(w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def update(self,var):
        var.win.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def move(self,var):
        var.c_platform = list()
        for platform in var.platforms:
            if var.player.rect.colliderect(platform):
                if var.player.rect.y <= platform.rect.y - int(var.h * 0.1) + 5:
                    var.c_platform.append(True)
            if True in var.c_platform:
                    var.grav = False
            else:
                var.grav = True
        if var.grav:
            var.player.rect.y += 3
        if var.move_l:
            var.player.rect.x -= var.player.speed
        if var.move_r:
            var.player.rect.x += var.player.speed
        if var.jump and not(var.grav):
            var.jump_a = True
        if var.jump_a:

            var.player.rect.y -= 10
            var.player_jc += 1
            if var.player_jc >= 15:
                var.jump_a = False
                var.grav = True
                var.player_jc = 0
        if self.rect.y > var.h - 40:
            var.fin = True
class Spawner():
    def spawn(self, var):
        platform = GameSprite('plat.png', int(var.w * 0.3), int(var.h * 0.1), randint(0,300), var.platforms[-1].rect.y - 50)
        platform.rect.x += 0
        platform.rect.y -= 50
        var.platforms.append(platform)

        
class GameVar():
    def __init__(self):
        self.w = 400
        self.h = int(self.w/9*16)
        self.run = True
        self.fin = False
        self.start = False
        self.win = pg.display.set_mode((self.w, self.h))
        pg.display.set_caption('Прыгай по замерзшим платформам или стань мусором')
        self.bak = pg.transform.scale(pg.image.load('bak.png'),(100, 150))
        self.move_l = False
        self.move_r = False
        self.jump = False
        self.player = Player('soul.png', int(self.w * 0.2), int(self.h * 0.1), int(self.w / 2), int(self.h / 2))
        self.player.speed = 4
        self.player_dir = 'right'
        self.player_jc = 0
        self.jump_a = False
        self.platforms = list()
        self.platform = GameSprite('plat.png', int(self.w * 0.3), int(self.h * 0.1), int(self.player.rect.x), int(self.player.rect.y + 70))
        self.platforms.append(self.platform)
        self.spawner = Spawner()
        self.plat_s = 7
        self.frame_c = 0
        self.grav = False
        self.c_platform = list()

