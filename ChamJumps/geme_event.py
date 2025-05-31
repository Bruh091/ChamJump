import pygame as pg

def geme_event(events, var):
    for e in events:
        if e.type == pg.QUIT:
            var.run = False
        if e.type == pg.KEYDOWN:
            if e.key == pg.K_a:
                var.move_l = True
                if var.player_dir == 'right':
                    var.player.image = pg.transform.flip(var.player.image, True, False)
                    var.player_dir = 'left'
            if e.key == pg.K_d:
                var.move_r = True
                if var.player_dir == 'left':
                    var.player.image = pg.transform.flip(var.player.image, True, False)
                    var.player_dir = 'right'
            if e.key == pg.K_SPACE:
                var.jump = True
        if e.type == pg.KEYUP:
            if e.key == pg.K_a:
                var.move_l = False
            if e.key == pg.K_d:
                var.move_r = False
            if e.key == pg.K_SPACE:
                var.jump = False
    return var