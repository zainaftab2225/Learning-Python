import block_library
import pygame
import random


class BadBlock(block_library.Block):

    def update(self):
        self.rect.y += 1
        if self.rect.y > 600:
            self.rect.x = random.randrange(10, 790)
            self.rect.y = random.randrange(-50, -20)
