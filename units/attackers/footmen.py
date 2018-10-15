import pygame as pg
from settings import *
from random import randint
from .shared import Attacker

class HoodWarrior(pg.sprite.Sprite, Attacker):
    def __init__(self, game):
        self.groups = game.all_sprites, game.attackers
        Attacker.__init__(self, game, 0.5)
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game

        self.image = game.hood_warrior_image
        self.rect = self.image.get_rect()
        self.rect.x = self.game.attack_center.rect.x
        self.rect.y = self.game.attack_center.rect.y

        # Defence Center variables

    def update(self):
        self.attacker_update()