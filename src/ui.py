import pygame as pg

def ui(screen):
    for i in range(1, 11):
        for j in range(1, 5):
            pg.draw.rect(screen, (10 * i, 10 * i + 5 * j, 10 * i), pg.Rect(16 + 48 * i, 48 * j, 32, 32))
    pg.display.flip()
