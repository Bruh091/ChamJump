import pygame as pg
from random import randint
pg.init()
pg.mixer.init()
pg.font.init()
from geme_event import geme_event
from Gclass import GameSprite, GameVar, Player
#переменные
clock = pg.time.Clock()
var = GameVar()
res_label = pg.font.SysFont('verdana', 50).render('Порожение', True, (255,0,0))
a = randint(0,255)
b = randint(0,255)
c = randint(0,255)
am = -1
ap = 1
bm = -1
bp = 1
cm = -1
cp = 1
#цикл
while var.run:
    if not var.fin:
        var.frame_c += 1
        events = pg.event.get()
        var = geme_event(events, var)
        var.win.fill((a, b, c))
        var.player.move(var)
        var.player.update(var)
        for platform in var.platforms:
            if var.frame_c == 5:
                platform.rect.y += int(var.plat_s)
            platform.update(var)
            if platform.rect.y >= var.h:
                var.platforms.remove(platform)
        var.player.move(var)
        var.player.update(var)
        
        if var.frame_c == 5:
            var.frame_c = 0
        if var.platforms[-1].rect.y >= 100:
            var.spawner.spawn(var)
        var.win.blit(var.bak,(int(var.player.rect.x - 10), int(var.h*0.9)))
    else:
        events = pg.event.get()
        var = geme_event(events, var)
        var.win.fill((a, b, c))
        var.win.blit(var.bak,(int(var.player.rect.x - 10), int(var.h*0.9)))
        var.win.blit(res_label, (var.w/5,var.h/2))
    pg.display.update()
    clock.tick(60)







    if randint(0,1):
        if 1 <= a <= 254:
            a += ap
        else:
            ap *= am
            a += ap

    if randint(0,1):
        if 1 <= b <= 254:
            b += bp
        else:
            bp *= bm
            b += bp

    if randint(0,1):
        if 1 <= c <= 254:
            c += cp
        else:
            cp *= cm
            c += cp
    


    