import pygame
import random


# Define some colors as global constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
SKY_BLUE = (137, 196, 244)
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


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([20, 20])
        self.image.fill(BLUE)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.change_x = 0
        self.change_y = 0
        self.walls = None
        self.lives = 5

    def change_speed(self, x, y):
        self.change_x += x
        self.change_y += y

    def update(self):
        self.rect.x += self.change_x

        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        self.rect.y += self.change_y
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom


class Wall(pygame.sprite.Sprite):
    """ Wall the player can run into. """

    def __init__(self, x, y, width, height):
        """ Constructor for the wall that the player can run into. """
        # Call the parent's constructor
        super().__init__()

        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(BLUE)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


class Game():
    # Game Constructor
    # Sets all Blocks in the game
    # Initializes score and Game Over flag
    def __init__(self):
        self.score = 50
        self.game_over_flag = False
        self.green_block_list = pygame.sprite.Group()
        self.red_block_list = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()
        self.wall_list = pygame.sprite.Group()

        # Make the walls. (x_pos, y_pos, width, height)
        self.wall = Wall(0, 0, 10, SCREEN_HEIGHT)
        self.wall_list.add(self.wall)
        self.all_sprites_list.add(self.wall)
        self.wall = Wall(10, 0, SCREEN_WIDTH, 10)
        self.wall_list.add(self.wall)
        self.all_sprites_list.add(self.wall)
        self.wall = Wall(0, SCREEN_HEIGHT-10, SCREEN_WIDTH, 10)
        self.wall_list.add(self.wall)
        self.all_sprites_list.add(self.wall)
        self.wall = Wall(SCREEN_WIDTH-10, 0, 10, SCREEN_HEIGHT)
        self.wall_list.add(self.wall)
        self.all_sprites_list.add(self.wall)
        # Player Initializations
        # Give the Starting Point for Player (100,100)
        # Add the wall limits for the player
        self.player = Player(100, 100)
        self.player.walls = self.wall_list
        self.all_sprites_list.add(self.player)

        self.collect_green_sound = pygame.mixer.Sound("coin7.wav")
        self.collect_red_sound = pygame.mixer.Sound("Coin10.wav")

        for i in range(20):
            self.block = Block(GREEN, 20, 20)
            self.green_block_list.add(self.block)
            self.all_sprites_list.add(self.block)

        for i in range(20):
            self.block = Block(RED, 20, 20)
            self.red_block_list.add(self.block)
            self.all_sprites_list.add(self.block)

    # Process User Events
    # Set Flag for Game Over
    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            # Set the speed based on the key pressed
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.change_speed(-5, 0)
                elif event.key == pygame.K_RIGHT:
                    self.player.change_speed(5, 0)
                elif event.key == pygame.K_UP:
                    self.player.change_speed(0, -5)
                elif event.key == pygame.K_DOWN:
                    self.player.change_speed(0, 5)
                elif event.key == pygame.K_SPACE and self.game_over_flag is True:
                    self.__init__()
            # Reset speed when key goes up
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.player.change_speed(5, 0)
                elif event.key == pygame.K_RIGHT:
                    self.player.change_speed(-5, 0)
                elif event.key == pygame.K_UP:
                    self.player.change_speed(0, 5)
                elif event.key == pygame.K_DOWN:
                    self.player.change_speed(0, -5)
            if event.type == pygame.MOUSEBUTTONDOWN:
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
            self.green_block_hit_list = pygame.sprite.spritecollide(
                self.player, self.green_block_list, True)
            for self.block in self.green_block_hit_list:
                self.score -= 1
                self.collect_green_sound.play()
                print("Remaining Green: ", self.score)
            self.red_block_hit_list = pygame.sprite.spritecollide(
                self.player, self.red_block_list, True)
            for self.block in self.red_block_hit_list:
                self.player.lives -= 1
                self.collect_red_sound.play()
                print("Remaining Lives: ", self.player.lives)
            # Game Over Condition
            if len(self.green_block_list) == 0 or self.player.lives == 0:
                self.game_over_flag = True

    def display_frame(self, screen):

        screen.fill(WHITE)

        if self.game_over_flag:
            self.font = pygame.font.SysFont("serif", 25)
            self.text = self.font.render("Game Over! Click or Press Space to restart.", True, BLACK)
            self.x = (SCREEN_WIDTH//2) - (self.text.get_width() // 2)
            self.y = (SCREEN_HEIGHT//2) - (self.text.get_height() // 2)
            screen.blit(self.text, [self.x, self.y])

        if not self.game_over_flag:
            self.font = pygame.font.SysFont("serif", 20)
            self.lives_text = self.font. render(
                "Lives: "+str(self.player.lives), True, BLACK)
            self.score_text = self.font. render(
                "Remaining Green: "+str(self.score), True, BLACK)
            self.score_text_x = 20
            self.score_text_y = 460
            self.lives_text_x = 200
            self.lives_text_y = 460
            screen.blit(self.score_text, [self.score_text_x, self.score_text_y])
            screen.blit(self.lives_text, [self.lives_text_x, self.lives_text_y])
            self.all_sprites_list.draw(screen)

        pygame.display.flip()


def main():
    """ Main function for the game. """
    pygame.mixer.pre_init(44100, 16, 2, 4096)
    pygame.init()
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    pygame.display.set_caption("My Game")

    # Loop until the user clicks the close button.
    done = False
    game = Game()
    pygame.mixer.music.load("mythica.mp3")
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1)
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
