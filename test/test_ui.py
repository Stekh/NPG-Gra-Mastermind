import pytest
from src import ui

def test_button_draw() -> None:
    """Checks if buttons were drawn properly"""
    pg.init()

    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    buttons = ui.construct_buttons()
    ui.ui(screen)








def test_button_mouse() -> None:
    """Checks if button states update properly"""

if __name__ == '__main__':
    button_draw_test()
    button_mouse_test()