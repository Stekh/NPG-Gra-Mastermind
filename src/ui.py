import pygame as pg

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


# BIG_BUTTON_WIDTH = 32
# BIG_BUTTON_HEIGHT = 32
# SMALL_BUTTON_WIDTH = 16
# SMALL_BUTTON_HEIGHT = 16


class Pin:
    """Pin is a singular object that represents an interactable button.


    :param x: - x coordinate of the button
    :param y: - y coordinate of the button.
    :param width: - width of the button
    :param height: - height of the button.
    :param hover: - indicates whether the button is hovered over"""

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
        :return: boolean that indicates if mouse is hovering over the button"""
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


def construct_display() -> pg.Surface:  # -> (pg.display, list[Button]):
    """Constructs everything necessary to be displayed on the screen

    :return: screen -the surface to display UI elements on"""
    pg.init()
    screen: pg.Surface = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pg.display.set_caption("Mastermind")

    # buttons = construct_buttons()
    pg.display.flip()
    # return screen, buttons
    return screen


"""
"""


def draw_endscreen(screen: pg.Surface, font: pg.font.Font, end_message: str) -> None:
    """Draws given endscreen message on the screen

    :param screen: surface to draw on
    :param font: font of the message
    :param end_message: message to be displayed"""
    text = font.render(end_message, True, "white", None, 1000)
    text_block = text.get_rect()
    text_block.center = (270, 207)
    screen.blit(text, text_block)


class UniversalButton:
    """An elaboration on Pin class

    :param x: - x coordinate of the button
    :param y: - y coordinate of the button.
    :param width: - width of the button
    :param height: - height of the button.
    :param hover: - indicates whether the button is hovered over
    :param color: - color of the button
    :param hover_color: - color of the button when hovered"""

    def __init__(self, x: int, y: int, width: int, height: int, is_pure_text: bool,
                 color: pg.Color, hover_color: pg.Color,
                 hover: bool = False, text: str = None, font: pg.font.Font = None,
                 text_color: pg.Color = pg.Color("white"),
                 text_hover_color: pg.Color = pg.Color(252, 178, 50)):
        self.x: int = x
        self.y: int = y
        self.width: int = width
        self.height: int = height
        self.hover_color: pg.Color = hover_color
        self.color: pg.Color = color
        self.clicked: bool = False
        self.hover: bool = hover
        self.rect: pg.Rect = pg.Rect(x, y, width, height)
        self.text: str = text
        self.font: pg.font.Font = font
        self.is_pure_text: bool = is_pure_text
        self.text_color: pg.Color = color if is_pure_text else text_color
        self.text_hover_color: pg.Color = hover_color if is_pure_text else text_hover_color

    def draw(self, screen: pg.Surface) -> None:
        """Puts the button on the screen in its place

        :param screen: - surface on which the button is being drawn
        :return: None"""
        if self.is_pure_text == 0:
            if self.hover:
                pg.draw.rect(screen, self.hover_color, self.rect)
            else:
                pg.draw.rect(screen, self.color, self.rect)
        if self.text is not None:
            if self.hover:
                text = self.font.render(self.text, True, self.text_hover_color, None, 1000)
                text_block = self.rect
                screen.blit(text, text_block)
            else:
                text = self.font.render(self.text, True, self.text_color, None, 1000)
                text_block = self.rect
                screen.blit(text, text_block)

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


class Menu:
    """Main menu class.

    :param screen: surface to draw on
    :param font: font for buttons
    """

    def __init__(self, screen: pg.Surface, font: pg.font.Font):
        self.screen: pg.Surface = screen
        self.font: pg.font.Font = font
        self.Easy: UniversalButton = UniversalButton(370, 250, 100, 50, True, pg.Color("white"), pg.Color(21, 183, 232),
                                                     False,
                                                     "Easy", font)
        self.Medium: UniversalButton = UniversalButton(349, 300, 150, 50, True, pg.Color("white"),
                                                       pg.Color(21, 183, 232), False,
                                                       "Medium", font)
        self.Hard: UniversalButton = UniversalButton(370, 350, 100, 50, True, pg.Color("white"), pg.Color(21, 183, 232),
                                                     False,
                                                     "Hard", font)
        self.Exit: UniversalButton = UniversalButton(368, 500, 100, 50, True, pg.Color("white"), pg.Color(21, 183, 232),
                                                     False,
                                                     "Exit", pg.font.Font(None, 60))
        self.buttons = [self.Easy, self.Medium, self.Hard, self.Exit]
        self.mm_font: pg.font = pg.font.Font(None, 80)
        self.mm_text: pg.Surface = self.mm_font.render("Mastermind", False, "white", None)
        self.mm_block: pg.Rect = self.mm_text.get_rect()
        self.mm_block.center = (400, 50)
        self.start_font: pg.font = pg.font.Font(None, 60)
        self.start_text: pg.Surface = self.start_font.render("Start", False, "white", None)
        self.start_block: pg.Rect = self.start_text.get_rect()
        self.start_block.center = (400, 200)

    def update(self, mouse_state: [bool, (int, int)]) -> None:
        """Updates buttons.

        :param mouse_state: - holds full information about the mouse
        :return: None
        """
        for button in self.buttons:
            button.update(mouse_state)

    def draw(self) -> None:
        """Draws the menu.

        :return: None
        """
        for button in self.buttons:
            button.draw(self.screen)
        self.screen.blit(self.mm_text, self.mm_block)
        self.screen.blit(self.start_text, self.start_block)


class Menu2:
    """Second stage menu class.

    :param screen: surface to draw on
    :param font: font for buttons
    """

    def __init__(self, screen: pg.Surface, font: pg.font.Font, no_rounds: int = 5, guessing_status: bool = True):
        self.screen: pg.Surface = screen
        self.font: pg.font = font
        self.no_rounds: int = no_rounds
        self.mm_font: pg.font = pg.font.Font(None, 80)
        self.mm_text: pg.Surface = self.mm_font.render("Mastermind", False, "white", None)
        self.mm_block: pg.Rect = self.mm_text.get_rect()
        self.mm_block.center = (400, 50)
        self.nor_font: pg.font = font
        self.nor_text: pg.Surface = self.nor_font.render("Number of rounds:", False, "white", None)
        self.nor_block: pg.Rect = self.nor_text.get_rect()
        self.nor_block.center = (400, 150)
        self.start_as_font: pg.font = font
        self.start_as_text: pg.Surface = self.start_as_font.render("Start as:", False, "white", None)
        self.start_as_block: pg.Rect = self.start_as_text.get_rect()
        self.start_as_block.center = (400, 250)
        self.nor_num_font: pg.font = pg.font.Font(None, 50)
        self.nor_num_text: pg.Surface = self.nor_num_font.render(str(no_rounds), False, "white", None)
        self.nor_num_block: pg.Rect = self.nor_num_text.get_rect()
        self.nor_num_block.center = (400, 200)
        self.Start: UniversalButton = UniversalButton(350, 400, 100, 50, True, pg.Color("white"),
                                                      pg.Color(21, 183, 232), False, "Start!", pg.font.Font(None, 60))
        self.Exit: UniversalButton = UniversalButton(368, 500, 100, 50, True, pg.Color("white"), pg.Color(21, 183, 232),
                                                     False,
                                                     "Exit", pg.font.Font(None, 60))
        self.guessing_status: bool = guessing_status
        self.Guessing: UniversalButton = UniversalButton(250, 275, 120, 50, True,
                                                         pg.Color(21, 183, 232) if self.guessing_status else pg.Color(
                                                             "white"), pg.Color(21, 183, 232), False, "Guessing", font)
        self.Setting: UniversalButton = UniversalButton(450, 275, 120, 50, True,
                                                        pg.Color(21, 183,
                                                                 232) if not self.guessing_status else pg.Color(
                                                            "white"), pg.Color(21, 183, 232), False, "Setting", font)
        self.plus: UniversalButton = UniversalButton(350, 180, 50, 50, True, pg.Color("white"), pg.Color(21, 183, 232),
                                                     False, "+", font)
        self.minus: UniversalButton = UniversalButton(440, 180, 50, 50, True, pg.Color("white"), pg.Color(21, 183, 232),
                                                      False, "-", font)
        self.buttons = [self.Start, self.Exit, self.Guessing, self.Setting, self.plus, self.minus]

    def update(self, mouse_state: [bool, (int, int)]) -> None:
        """Updates buttons and number of rounds.

        :param mouse_state: - holds full information about the mouse
        :return: None
        """
        for button in self.buttons:
            button.update(mouse_state)
        if self.Guessing.clicked:
            self.guessing_status = True
            self.Guessing.color.update(21, 183, 232)
            self.Setting.color.update("white")
        if self.Setting.clicked:
            self.guessing_status = False
            self.Guessing.color.update("white")
            self.Setting.color.update(21, 183, 232)
        if self.no_rounds < 10:
            self.no_rounds += 1 if self.plus.clicked else 0
        if self.no_rounds > 1:
            self.no_rounds -= 1 if self.minus.clicked else 0
        self.nor_num_text = self.nor_num_font.render(str(self.no_rounds), False, "white", None)
        self.nor_num_block = self.nor_num_text.get_rect()
        self.nor_num_block.center = (400, 200)

    def draw(self) -> None:
        """Draws the menu.

        :return: None
        """
        for button in self.buttons:
            button.draw(self.screen)
        self.screen.blit(self.mm_text, self.mm_block)
        self.screen.blit(self.nor_text, self.nor_block)
        self.screen.blit(self.start_as_text, self.start_as_block)
        self.screen.blit(self.nor_num_text, self.nor_num_block)
