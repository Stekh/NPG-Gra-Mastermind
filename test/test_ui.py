import pygame as pg
from src import ui

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class TestPin:
    def test_constructor(self):
        pin = ui.Pin(10, 10, 32, 32)
        assert pin.hover is False
        assert pin.rect == pg.Rect(10, 10, 32, 32)

    def test_draw(self):
        pin = ui.Pin(10, 10, 32, 32)
        screen = ui.construct_display()
        pin.draw(screen, pg.Color(100, 100, 100))
        assert pg.Color(100, 100, 100) == screen.get_at((15, 15))

    def test_is_mouse_over(self):
        pin = ui.Pin(10, 10, 32, 32)
        assert pin.is_mouse_over((30, 30)) is True
        assert pin.is_mouse_over((0, 0)) is False

    def test_set_hover(self):
        pin = ui.Pin(10, 10, 32, 32)
        pin.set_hover(True)
        assert pin.hover is True
        pin.set_hover(False)
        assert pin.hover is False


class TestUniversalButton:
    def test_constructor(self):
        pin = ui.UniversalButton(10, 10, 32, 32, pg.Color(0, 255, 0), pg.Color(255, 0, 0))
        assert pin.hover is False
        assert pin.clicked is False
        assert pin.rect == pg.Rect(10, 10, 32, 32)

    def test_draw(self):
        pin = ui.UniversalButton(10, 10, 32, 32, pg.Color(0, 255, 0), pg.Color(255, 0, 0))
        screen = ui.construct_display()
        pin.draw(screen)
        assert pg.Color(0, 255, 0) == screen.get_at((15, 15))
        pin.hover = True
        pin.draw(screen)
        assert pg.Color(255, 0, 0) == screen.get_at((15, 15))

# def test_button_draw() -> None:
#     """Checks if buttons were drawn properly"""
#     (screen, buttons) = ui.construct_display()
#     ui.ui(screen, [0, (0, 0)], buttons)
#
#     # big buttons
#     assert (255, 255, 255) == screen.get_at((65, 49))
#     assert (255, 255, 255) == screen.get_at((497, 193))
#     assert (0, 0, 0) == screen.get_at((97, 81))
#
#     # small buttons
#     assert (64, 64, 64) == screen.get_at((73, 285))
#     assert (64, 64, 64) == screen.get_at((456, 333))
#     assert (0, 0, 0) == screen.get_at((90, 287))
#
#
# def test_button_hover() -> None:
#     (screen, buttons) = ui.construct_display()
#
#     # big buttons
#     ui.ui(screen, [0, (65, 49)], buttons)
#     assert (127, 127, 127) == screen.get_at((65, 49))
#     ui.ui(screen, [0, (0, 0)], buttons)
#     assert (255, 255, 255) == screen.get_at((65, 49))
#     ui.ui(screen, [0, (497, 193)], buttons)
#     assert (127, 127, 127) == screen.get_at((497, 193))
#     ui.ui(screen, [0, (0, 0)], buttons)
#     assert (255, 255, 255) == screen.get_at((497, 193))
#
#     # small buttons
#     ui.ui(screen, [0, (73, 285)], buttons)
#     assert (127, 127, 127) == screen.get_at((73, 285))
#     ui.ui(screen, [0, (456, 333)], buttons)
#     assert (127, 127, 127) == screen.get_at((456, 333))
#     ui.ui(screen, [0, (0, 0)], buttons)
#     assert (64, 64, 64) == screen.get_at((73, 285))
#     assert (64, 64, 64) == screen.get_at((456, 333))
#
#
# def test_button_click() -> None:
#     (screen, buttons) = ui.construct_display()
#
#     # big buttons
#     ui.ui(screen, [1, (65, 49)], buttons)
#     ui.ui(screen, [0, (0, 0)], buttons)
#     assert (255, 0, 0) == screen.get_at((65, 49))
#
#     ui.ui(screen, [1, (65, 49)], buttons)
#     ui.ui(screen, [0, (0, 0)], buttons)
#     assert (255, 255, 0) == screen.get_at((65, 49))
#
#     ui.ui(screen, [1, (65, 49)], buttons)
#     ui.ui(screen, [0, (0, 0)], buttons)
#     assert (0, 255, 0) == screen.get_at((65, 49))
#
#     ui.ui(screen, [1, (65, 49)], buttons)
#     ui.ui(screen, [0, (0, 0)], buttons)
#     assert (127, 0, 255) == screen.get_at((65, 49))
#
#     ui.ui(screen, [1, (65, 49)], buttons)
#     ui.ui(screen, [0, (0, 0)], buttons)
#     assert (255, 255, 255) == screen.get_at((65, 49))
#
#     # small buttons
#     ui.ui(screen, [1, (73, 285)], buttons)
#     ui.ui(screen, [0, (0, 0)], buttons)
#     assert (0, 64, 64) == screen.get_at((73, 285))
#
#     ui.ui(screen, [1, (73, 285)], buttons)
#     ui.ui(screen, [0, (0, 0)], buttons)
#     assert (255, 255, 255) == screen.get_at((73, 285))
#
#     ui.ui(screen, [1, (73, 285)], buttons)
#     ui.ui(screen, [0, (0, 0)], buttons)
#     assert (64, 64, 64) == screen.get_at((73, 285))
