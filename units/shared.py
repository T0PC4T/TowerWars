from interface.buttons import ButtonBase
import pygame as pg
from settings import *

src_img = pg.Surface((TILE_SIZE, TILE_SIZE))
src_img.fill(BLACK)

class Unit(ButtonBase):
    def __init__(self, game):
        ButtonBase.__init__(self)
        self.game = game
        self.set_action(self.game.menu.set_focus, self)

    def get_pos(self, center=True):
        if center:
            return pg.Vector2(self.rect.center)
        else:
            return pg.Vector2(self.rect)

    def get_tile_x_tile_y(self):
        x, y = getattr(self, "pos", pg.Vector2((0, 0)))
        return int(x//TILE_SIZE), int(y//TILE_SIZE)

    def get_options(self):
        return list()

    def get_img(self):
        return getattr(self, "src_img", src_img)

    def get_title(self):
        return "N/A"

    def get_info(self):
        return {"N/A": "N/A"}

    def get_price(self):
        return getattr(self, "price", 0)

    def get_income(self):
        return getattr(self, "income", 0)