import pygame as pg


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BIG_BUTTON_WIDTH = 32
BIG_BUTTON_HEIGHT = 32
SMALL_BUTTON_WIDTH = 16
SMALL_BUTTON_HEIGHT = 16


class Button:
    """Button is a singular object that represents an interactable button.
    Attributes: coordinates, size, hover and click colors
    Methods allow for drawing, updating and interpreting click count and hover state"""

    def __init__(self, x: float, y: float, width: float, height: float, hover=False):
        self.hover = hover
        self.rect = pg.Rect(x, y, width, height)

    def draw(self, screen: pg.Surface, color: pg.color) -> None:
        """Puts the button on the screen in its place"""
        pg.draw.rect(screen, color, self.rect)

    def is_mouse_over(self, pos: (int, int)) -> bool:
        """Checks for mouse hover position relative to the button"""
        return self.rect.collidepoint(pos)

    def set_hover(self, hover: bool) -> None:
        """Updates the mouse hover status"""
        self.hover = hover



"""
def ui(screen: pg.Surface, mouse_state: [bool, (int, int)], buttons: list[Button]) -> None:
    Updates UI based on mouse position - comment
    for b in buttons:

        pos = mouse_state[1]
        is_mouse_over = b.is_mouse_over(pos)
        b.set_hover(is_mouse_over)

        if is_mouse_over:
            clicked = mouse_state[0]
            if clicked:
                b.next_click()

        b.draw(screen)

    pg.display.flip()


def construct_buttons() -> list[Button]:
    constructs necessary buttons to be drawn on the screen - comment
    buttons = []
    for j in range(1, 5):
        for i in range(1, 11):
            # p1 buttons
            x1 = 16 + 48 * i
            y1 = 48 * j
            buttons.append(
                Button(x1, y1, BIG_BUTTON_WIDTH, BIG_BUTTON_HEIGHT,
                       [(255, 255, 255), (255, 0, 0), (255, 255, 0), (0, 255, 0), (127, 0, 255)], (127, 127, 127)))

            # p2 buttons
            x2 = x1 + 8
            y2 = 260 + 24 * j
            buttons.append(
                Button(x2, y2, SMALL_BUTTON_WIDTH, SMALL_BUTTON_HEIGHT, [(64, 64, 64), (0, 64, 64), (255, 255, 255)],
                       (127, 127, 127)))
    return buttons


def construct_display() -> (pg.display, list[Button]):
    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pg.display.set_caption("Mastermind")

    buttons = construct_buttons()
    pg.display.flip()
    return screen, buttons
"""