import pygame as pg

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BIG_BUTTON_WIDTH = 32
BIG_BUTTON_HEIGHT = 32
SMALL_BUTTON_WIDTH = 16
SMALL_BUTTON_HEIGHT = 16


class Pin:
    """Pim is a singular object that represents an interactable button.


    :param x:, :param y: - coordinates of the button.
    :param width:, :param height: - size of the button.
    :param hover: - checks whether the button is hovered over"""

    def __init__(self, x: float, y: float, width: float, height: float, hover: bool = False):
        self.hover: bool = hover
        self.rect: pg.Rect = pg.Rect(x, y, width, height)

    def draw(self, screen: pg.Surface, color: pg.Color) -> None:
        """Puts the button on the screen in its place

        :param screen: - surface on which the button is being drawn
        :param color: - color of the pin
        :return: None"""

        pg.draw.rect(screen, color, self.rect)

    def is_mouse_over(self, pos: (int, int)) -> bool:
        """Checks if mouse hover position is over the button

        :param pos: - coordinates of mouse position
        :return: bool
        1 - mouse is over the button,
        0 - mouse is not over the button"""
        return self.rect.collidepoint(pos)

    def set_hover(self, hover: bool) -> None:
        """Updates the mouse hover status

        :param hover: - checks whether the button is hovered over
        :return: None"""
        self.hover = hover


"""
def ui(screen: pg.Surface, mouse_state: [bool, (int, int)], buttons: list[Button]) -> None:
    """"""Updates UI based on mouse position

    :param screen: - surface on which the button is being drawn
    :param mouse_state: - coordinates of mouse
    :param buttons: - list of buttons
    :return: None""""""

    for b in buttons:

    pos: (int, int) = mouse_state[1]
    is_mouse_over: bool = b.is_mouse_over(pos)
    b.set_hover(is_mouse_over)

    if is_mouse_over:
        clicked: bool = mouse_state[0]
        if clicked:
            b.next_click()

    b.draw(screen)


pg.display.flip()


def construct_buttons() -> list[Button]:
    """"""constructs necessary buttons to be drawn on the screen

    :return: list of buttons""""""

    buttons = []
    for j in range(1, 5):
        for i in range(1, 11):
            # p1 buttons
            x1: int = 16 + 48 * i
            y1: int = 48 * j
            buttons.append(
                Button(x1, y1, BIG_BUTTON_WIDTH, BIG_BUTTON_HEIGHT,
                       [(255, 255, 255), (255, 0, 0), (255, 255, 0), (0, 255, 0), (127, 0, 255)], (127, 127, 127)))

            # p2 buttons
            x2: int = x1 + 8
            y2: int = 260 + 24 * j
            buttons.append(
                Button(x2, y2, SMALL_BUTTON_WIDTH, SMALL_BUTTON_HEIGHT, [(64, 64, 64), (0, 64, 64), (255, 255, 255)],
                       (127, 127, 127)))
    return buttons

"""


def construct_display() -> pg.display:  # -> (pg.display, list[Button]):
    """Constructs everything necessary to be displayed on the screen

    :return: screen -the surface to display and buttons - the list of buttons"""
    pg.init()
    screen: pg.surface = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pg.display.set_caption("Mastermind")

    # buttons = construct_buttons()
    pg.display.flip()
    # return screen, buttons
    return screen


"""
"""


class UniversalButton:
    """An elaboration on Pin class

    :param x:, :param y: - coordinates of the button.
    :param width:, :param height: - size of the button.
    :param hover: - checks whether the button is hovered over
    :param color: - color of the button
    :param hover_color: - color of the button when hovered
    :param hover: - checks whether the button is hovered over"""

    def __init__(self, x: int, y: int, width: int, height: int,
                 color: pg.Color, hover_color: pg.Color, hover: bool = False):
        self.x: int = x
        self.y: int = y
        self.width: int = width
        self.height: int = height
        self.hover_color: pg.Color = hover_color
        self.color: pg.Color = color
        self.clicked: bool = False
        self.hover: bool = hover
        self.rect: pg.Rect = pg.Rect(x, y, width, height)

    def draw(self, screen: pg.Surface) -> None:
        """Puts the button on the screen in its place

        :param screen: - surface on which the button is being drawn
        :return: None"""
        if self.hover:
            pg.draw.rect(screen, self.hover_color, self.rect)
        else:
            pg.draw.rect(screen, self.color, self.rect)

    def is_mouse_over(self, pos: (int, int)) -> bool:
        """Checks for mouse hover position relative to the button

        :param pos: - coordinates of the cursor
        :return: T/F of whether mouse is hovering the button"""
        return self.rect.collidepoint(pos)

    def set_hover(self, hover: bool) -> None:
        """Updates the mouse hover status

        :param hover: - checks if cursor is over the button
        :return: None"""
        self.hover = hover

    def update(self, mouse_state: [bool, (int, int)]) -> None:
        """Updates the hover and click button status

        :param mouse_state: - holds full information about the mouse (clicked status, position)
        :return: None"""
        pos: (int, int) = mouse_state[1]
        is_mouse_over: bool = self.is_mouse_over(pos)
        self.set_hover(is_mouse_over)

        if is_mouse_over and mouse_state[0]:
            self.clicked = True
        else:
            self.clicked = False
