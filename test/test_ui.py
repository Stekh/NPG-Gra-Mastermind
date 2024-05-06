import pygame as pg
import pytest
from src import ui

def test_button_draw() -> None:
    """Checks if buttons were drawn properly"""
    pg.init()

    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    buttons = ui.construct_buttons()
    ui.ui(screen,[0,(0,0)],buttons)
    pg.display.flip()
    assert (255, 255, 255) == screen.get_at((65, 49))
    assert (255, 255, 255) == screen.get_at((497, 193))
    assert (0, 0 , 0) == screen.get_at((97,81))



if __name__ == '__main__':
    test_button_draw()