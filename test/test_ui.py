from src import ui

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def test_button_draw() -> None:
    """Checks if buttons were drawn properly"""
    (screen, buttons) = ui.construct_display()
    ui.ui(screen, [0, (0, 0)], buttons)

    # big buttons
    assert (255, 255, 255) == screen.get_at((65, 49))
    assert (255, 255, 255) == screen.get_at((497, 193))
    assert (0, 0, 0) == screen.get_at((97, 81))

    # small buttons
    assert (64, 64, 64) == screen.get_at((73, 285))
    assert (64, 64, 64) == screen.get_at((456, 333))
    assert (0, 0, 0) == screen.get_at((90, 287))


def test_button_hover() -> None:
    (screen, buttons) = ui.construct_display()

    # big buttons
    ui.ui(screen, [0, (65, 49)], buttons)
    assert (127, 127, 127) == screen.get_at((65, 49))
    ui.ui(screen, [0, (0, 0)], buttons)
    assert (255, 255, 255) == screen.get_at((65, 49))
    ui.ui(screen, [0, (497, 193)], buttons)
    assert (127, 127, 127) == screen.get_at((497, 193))
    ui.ui(screen, [0, (0, 0)], buttons)
    assert (255, 255, 255) == screen.get_at((497, 193))

    # small buttons
    ui.ui(screen, [0, (73, 285)], buttons)
    assert (127, 127, 127) == screen.get_at((73, 285))
    ui.ui(screen, [0, (456, 333)], buttons)
    assert (127, 127, 127) == screen.get_at((456, 333))
    ui.ui(screen, [0, (0, 0)], buttons)
    assert (64, 64, 64) == screen.get_at((73, 285))
    assert (64, 64, 64) == screen.get_at((456, 333))


def test_button_click() -> None:
    (screen, buttons) = ui.construct_display()

    # big buttons
    ui.ui(screen, [1, (65, 49)], buttons)
    ui.ui(screen, [0, (0, 0)], buttons)
    assert (255, 0, 0) == screen.get_at((65, 49))

    ui.ui(screen, [1, (65, 49)], buttons)
    ui.ui(screen, [0, (0, 0)], buttons)
    assert (255, 255, 0) == screen.get_at((65, 49))

    ui.ui(screen, [1, (65, 49)], buttons)
    ui.ui(screen, [0, (0, 0)], buttons)
    assert (0, 255, 0) == screen.get_at((65, 49))

    ui.ui(screen, [1, (65, 49)], buttons)
    ui.ui(screen, [0, (0, 0)], buttons)
    assert (127, 0, 255) == screen.get_at((65, 49))

    ui.ui(screen, [1, (65, 49)], buttons)
    ui.ui(screen, [0, (0, 0)], buttons)
    assert (255, 255, 255) == screen.get_at((65, 49))

    # small buttons
    ui.ui(screen, [1, (73, 285)], buttons)
    ui.ui(screen, [0, (0, 0)], buttons)
    assert (0, 64, 64) == screen.get_at((73, 285))

    ui.ui(screen, [1, (73, 285)], buttons)
    ui.ui(screen, [0, (0, 0)], buttons)
    assert (255, 255, 255) == screen.get_at((73, 285))

    ui.ui(screen, [1, (73, 285)], buttons)
    ui.ui(screen, [0, (0, 0)], buttons)
    assert (64, 64, 64) == screen.get_at((73, 285))
