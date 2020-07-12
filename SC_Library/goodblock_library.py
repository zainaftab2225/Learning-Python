import block_library
import pygame
import random


class GoodBlock(block_library.Block):

    def update(self):
        self.rect.x += random.randrange(-3, 4)
        self.rect.y += random.randrange(-3, 4)

        if self.rect.x > 790 or self.rect.x < 10:
            self.rect.x *= -1
        if self.rect.y > 590 or self.rect.y < 10:
            self.rect.y *= -1
