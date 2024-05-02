import pygame as pg

BUTTON_WIDTH = 32
BUTTON_HEIGHT = 32


class button:
    def __init__(self, x, y, width, height, colors, hover_color, click_count=0, hover=False):
        self.click_count = click_count
        self.hover = hover
        self.hover_color = hover_color
        self.colors = colors
        self.rect = pg.Rect(x, y, width, height)

    def draw(self, screen):
        color = self.colors[self.click_count % len(self.colors)]
        if self.hover:
            color = self.hover_color

        pg.draw.rect(screen, color, self.rect)

    def is_mouse_over(self, pos):
        return self.rect.collidepoint(pos)

    def set_hover(self, hover):
        self.hover = hover

    def next_click(self):
        self.click_count += 1


buttons = []
for j in range(1, 5):
    for i in range(1, 11):
        x = 16 + 48 * i
        y = 48 * j
        buttons.append(
            button(x, y, BUTTON_WIDTH, BUTTON_HEIGHT, [(255, 255, 255), (0, 255, 0), (0, 0, 255)], (255, 0, 0)))


def ui(screen, mouse_state):
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

# pg.draw.rect(screen, (10 * i, 10 * i + 5 * j, 10 * i), pg.Rect(16 + 48 * i, 48 * j, 32, 32))
