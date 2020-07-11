import pygame
import random


# Define some colors as global constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
SKY_BLUE = (137, 196, 244)
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500


class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()

    def reset_pos(self):
        self.rect.y = random.randrange(-100, -20)
        self.rect.x = random.randrange(700-20)

    def update(self):
        self.rect.y += 1
        if self.rect.y > 500+15:
            self.reset_pos()
            print("gone")


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([20, 20])
        self.image.fill(RED)

        self.rect = self.image.get_rect()

    def update(self):
        mouse_position = pygame.mouse.get_pos()
        self.rect.x = mouse_position[0]
        self.rect.y = 450


class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([4, 4])
        self.image.fill(GREEN)

        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y -= 5


class Game():
    # Game Constructor
    # Sets all Blocks in the game
    # Initializes score and Game Over flag
    def __init__(self):
        self.score = 0
        self.game_over_flag = False
        self.block_list = pygame.sprite.Group()
        self.bullet_list = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()
        self.player = Player()
        self.all_sprites_list.add(self.player)

        for i in range(50):
            self.block = Block(BLACK, 20, 15)
            self.block.rect.x = random.randrange(SCREEN_WIDTH-20)
            self.block.rect.y = random.randrange(-600, -20)
            self.block_list.add(self.block)
            self.all_sprites_list.add(self.block)

    # Process User Events
    # Set Flag for Game Over
    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True

            # Whenver user fires a bullet
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.game_over_flag is False:
                    self.bullet = Bullet()
                    self.bullet.rect.x = self.player.rect.x
                    self.bullet.rect.y = self.player.rect.y
                    self.all_sprites_list.add(self.bullet)
                    self.bullet_list.add(self.bullet)
                if self.game_over_flag is True:
                    self.__init__()
        return False

    # Run Game Logic
    # Check if Game Over is false
    # If it is, then check for collisions with player objects
    # Whenever there is a collision, remove the block from the block_list
    # When all blocks removed, set game_over_flag as True
    def run_logic(self):
        if self.game_over_flag is False:
            self.all_sprites_list.update()
            for self.bullet in self.bullet_list:
                self.block_hit_list = pygame.sprite.spritecollide(
                    self.bullet, self.block_list, True)
                for self.block in self.block_hit_list:
                    self.bullet_list.remove(self.bullet)
                    self.all_sprites_list.remove(self.bullet)
                    self.score += 1
                    print(self.score)

                if self.bullet.rect.y < -10:
                    self.bullet_list.remove(self.bullet)
                    self.all_sprites_list.remove(self.bullet)
    # Game Over Condition
        if len(self.block_list) == 0:
            self.game_over_flag = True

    def display_frame(self, screen):

        screen.fill(WHITE)

        if self.game_over_flag:
            self.font = pygame.font.SysFont("serif", 25)
            self.text = self.font.render("Game Over! Click to restart.", True, BLACK)
            self.x = (SCREEN_WIDTH//2) - (self.text.get_width() // 2)
            self.y = (SCREEN_HEIGHT//2) - (self.text.get_height() // 2)
            screen.blit(self.text, [self.x, self.y])

        if not self.game_over_flag:
            self.all_sprites_list.draw(screen)

        pygame.display.flip()


def main():
    """ Main function for the game. """

    pygame.init()
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    pygame.display.set_caption("My Game")

    # Loop until the user clicks the close button.
    done = False
    game = Game()
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while not done:

        done = game.process_events()

        game.run_logic()

        game.display_frame(screen)
        # Limit to 60 frames per second
        clock.tick(60)

    # Close the window and quit.
    # If you forget this line, the program will 'hang'
    # on exit if running from IDLE.
    pygame.quit()


if __name__ == "__main__":
    main()
