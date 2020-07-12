import random
import pygame

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500


class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect_change_x = random.randrange(-3, 3)
        self.rect_change_y = random.randrange(-3, 3)
        self.rect.x = random.randrange(30, SCREEN_WIDTH-30)
        self.rect.y = random.randrange(30, SCREEN_HEIGHT-30)

    def wall_bounce(self):
        if self.rect.x > 670:
            self.rect_change_x *= -1
        if self.rect.y > 470:
            self.rect_change_y *= -1
        if self.rect.x < 11:
            self.rect_change_x *= -1
        if self.rect.y < 11:
            self.rect_change_y *= -1

    def update(self):
        self.rect.x += self.rect_change_x
        self.rect.y += self.rect_change_y
        self.wall_bounce()
