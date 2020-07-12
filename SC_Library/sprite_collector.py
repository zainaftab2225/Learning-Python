import pygame
import random

# Define some colors as global constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
SKY_BLUE = (137, 196, 244)
PURPLE = (50, 0, 50)

# Screen Dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WALL_WIDTH = 10
GAME_END = -1
# BLOCK CLASS
# CREATES A SINGLE BLOCK
# REQUIRES (COLOR, BLOCK WIDTH, BLOCK HEIGHT, BLOCK MOVEMENT(1/0))


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
        self.level = 0

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


class Block(pygame.sprite.Sprite):
    """Block Class to create a Block on the screen"""

    def __init__(self, color, block_width, block_height, block_movement):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([block_width, block_height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

        if block_movement is False:
            self.rect_change_x = 0
            self.rect_change_y = 0
            self.rect.x = 10
            self.rect.y = 10
        else:
            self.move_blocks()

    def move_blocks(self):
        self.rect_change_x = random.randrange(-3, 3)
        self.rect_change_y = random.randrange(-3, 3)
        self.rect.x = random.randrange(30, SCREEN_WIDTH-30)
        self.rect.y = random.randrange(30, SCREEN_HEIGHT-30)

    def wall_bounce(self):
        if self.rect.x > SCREEN_WIDTH-30:
            self.rect_change_x *= -1
        if self.rect.y > SCREEN_HEIGHT-30:
            self.rect_change_y *= -1
        if self.rect.x < 1+WALL_WIDTH:
            self.rect_change_x *= -1
        if self.rect.y < 1+WALL_WIDTH:
            self.rect_change_y *= -1

    def update(self):
        self.rect.x += self.rect_change_x
        self.rect.y += self.rect_change_y
        self.wall_bounce()

    def change_color(self, color):
        self.image.fill(color)


class Game():

    # Game Constructor
    # Sets all Blocks in the game
    # Initializes score and Game Over flag
    def __init__(self):
        self.game_over_flag = False
        self.transition = False
        self.player = Player(100, 290)
        self.level_list = []
        self.level_list.append(Level00(self.player))
        self.level_list.append(Level01(self.player))
        self.level_list.append(Level02(self.player))
        self.level_list.append(Level03(self.player))
        self.level_list.append(Level04(self.player))
        self.level_list.append(Level05(self.player))
        self.level_list.append(Level06(self.player))
        self.current_level_no = 0
        self.player.level = self.current_level_no
        self.current_level = self.level_list[self.current_level_no]

    # Process User Events
    # Set Flag for Game Over

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            # Set the speed based on the key pressed
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.player.change_speed(-5, 0)
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.player.change_speed(5, 0)
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.player.change_speed(0, -5)
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.player.change_speed(0, 5)
                elif event.key == pygame.K_SPACE:
                    if self.game_over_flag is True:
                        self.__init__()
                    if self.transition is True:
                        self.transition = False
            # Reset speed when key goes up
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.player.change_speed(5, 0)
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.player.change_speed(-5, 0)
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.player.change_speed(0, 5)
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.player.change_speed(0, -5)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.game_over_flag is True:
                    self.__init__()
                if self.transition is True:
                    self.transition = False
        return False

    # Run Game Logic
    # Check if Game Over is false
    # If it is, then check for collisions with player objects
    # Whenever there is a collision, remove the block from the block_list
    # When all blocks removed, set game_over_flag as True
    def run_logic(self):
        if self.game_over_flag is False and self.transition is False:
            self.i = 0
            self.current_level.update()
            if self.player.level == GAME_END:
                self.game_over_flag = True
            elif self.player.level > self.current_level_no:
                self.transition = True
                self.current_level_no = self.player.level
                self.current_level = self.level_list[self.current_level_no]
        if self.player.lives == 0:
            self.game_over_flag = True

    def display_frame(self, screen):

        screen.fill(WHITE)

        if self.game_over_flag:
            self.font = pygame.font.SysFont("serif", 25)
            self.text = self.font.render("Game Over! Click or Press Space to restart.", True, BLACK)
            self.x = (SCREEN_WIDTH//2) - (self.text.get_width() // 2)
            self.y = (SCREEN_HEIGHT//2) - (self.text.get_height() // 2)
            screen.blit(self.text, [self.x, self.y])
        if self.transition:
            self.font = pygame.font.SysFont("serif", 25)
            self.text = self.font.render("TRANSITIOn", True, BLACK)
            self.x = (SCREEN_WIDTH//2) - (self.text.get_width() // 2)
            self.y = (SCREEN_HEIGHT//2) - (self.text.get_height() // 2)
            screen.blit(self.text, [self.x, self.y])
        if not self.game_over_flag and not self.transition:
            self.current_level.draw(screen)

        pygame.display.flip()


class Level():
    """ This is a generic super-class used to define a level."""

    def __init__(self, player):

        self.all_sprites_list = pygame.sprite.Group()
        self.wall_list = pygame.sprite.Group()
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
        player.walls = self.wall_list
        self.all_sprites_list.add(player)
    # Update everythign on this level

    def update(self):
        """ Update everything in this level."""
        self.all_sprites_list.update()

    def draw(self, screen):
        """ Draw everything on this level. """
        # Draw the background
        screen.fill(WHITE)
        self.all_sprites_list.draw(screen)

        # Draw all the sprite lists that we have


class Level00(Level):
    def __init__(self, player):
        super().__init__(player)

        self.remaining_count = 1
        self.player = player
        self.green_block_list = pygame.sprite.Group()
        self.block = Block(GREEN, 20, 20, False)
        self.block.rect.x = 700
        self.block.rect.y = 290
        self.green_block_list.add(self.block)
        self.all_sprites_list.add(self.block)

    def update(self):
        self.all_sprites_list.update()
        self.green_block_hit_list = pygame.sprite.spritecollide(
            self.player, self.green_block_list, True)
        for block in self.green_block_hit_list:
            self.remaining_count -= 1
            collect_green_sound.play()
        if self.remaining_count == 0:
            self.player.level = 1
            print("Player Level ", self.player.level)


class Level01(Level):
    def __init__(self, player):
        super().__init__(player)

        self.remaining_count = 3
        self.player = player
        self.green_block_list = pygame.sprite.Group()
        self.block1 = Block(GREEN, 20, 20, False)
        self.block2 = Block(GREEN, 20, 20, False)
        self.block3 = Block(GREEN, 20, 20, False)
        self.block1.rect.x = 100
        self.block1.rect.y = 145
        self.block2.rect.x = 100
        self.block2.rect.y = 290
        self.block3.rect.x = 100
        self.block3.rect.y = 435
        self.green_block_list.add(self.block1)
        self.all_sprites_list.add(self.block1)
        self.green_block_list.add(self.block2)
        self.all_sprites_list.add(self.block2)
        self.green_block_list.add(self.block3)
        self.all_sprites_list.add(self.block3)

    def update(self):
        self.all_sprites_list.update()
        self.green_block_hit_list = pygame.sprite.spritecollide(
            self.player, self.green_block_list, True)
        for block in self.green_block_hit_list:
            self.remaining_count -= 1
            collect_green_sound.play()
        if self.remaining_count == 0:
            self.player.level = 2
            print("Player Level ", self.player.level)


class Level02(Level):
    def __init__(self, player):
        super().__init__(player)

        self.remaining_count = 2
        self.player = player
        self.green_block_list = pygame.sprite.Group()
        self.red_block_list = pygame.sprite.Group()
        self.block1 = Block(GREEN, 20, 20, False)
        self.block2 = Block(RED, 20, 20, False)
        self.block3 = Block(GREEN, 20, 20, False)
        self.block1.rect.x = 700
        self.block1.rect.y = 145
        self.block2.rect.x = 700
        self.block2.rect.y = 290
        self.block3.rect.x = 700
        self.block3.rect.y = 435
        self.green_block_list.add(self.block1)
        self.all_sprites_list.add(self.block1)
        self.red_block_list.add(self.block2)
        self.all_sprites_list.add(self.block2)
        self.green_block_list.add(self.block3)
        self.all_sprites_list.add(self.block3)

    def update(self):
        self.all_sprites_list.update()
        self.green_block_hit_list = pygame.sprite.spritecollide(
            self.player, self.green_block_list, True)
        self.red_block_hit_list = pygame.sprite.spritecollide(
            self.player, self.red_block_list, True)
        for block in self.green_block_hit_list:
            self.remaining_count -= 1
            collect_green_sound.play()
        for self.block in self.red_block_hit_list:
            self.player.lives -= 1
            collect_red_sound.play()
            print("Remaining Lives: ", self.player.lives)
        if self.remaining_count == 0:
            self.player.level = 3
            print("Player Level ", self.player.level)


class Level03(Level):
    def __init__(self, player):
        super().__init__(player)

        self.remaining_count = 10
        self.player = player
        self.green_block_list = pygame.sprite.Group()
        for i in range(10):
            self.block = Block(GREEN, 20, 20, True)
            self.green_block_list.add(self.block)
            self.all_sprites_list.add(self.block)

    def update(self):
        self.all_sprites_list.update()
        self.green_block_hit_list = pygame.sprite.spritecollide(
            self.player, self.green_block_list, True)
        for self.block in self.green_block_hit_list:
            collect_green_sound.play()
            self.remaining_count -= 1
            print("Remaining Green: ", self.remaining_count)

        if self.remaining_count == 0:
            self.player.level = 4
            print("Player Level ", self.player.level)


class Level04(Level):
    def __init__(self, player):
        super().__init__(player)

        self.remaining_count = 10
        self.player = player
        self.red_block_list = pygame.sprite.Group()
        self.green_block_list = pygame.sprite.Group()
        for i in range(5):
            self.block = Block(RED, 20, 20, True)
            self.red_block_list.add(self.block)
            self.all_sprites_list.add(self.block)
        for i in range(10):
            self.block = Block(GREEN, 20, 20, True)
            self.green_block_list.add(self.block)
            self.all_sprites_list.add(self.block)

    def update(self):
        self.all_sprites_list.update()
        self.green_block_hit_list = pygame.sprite.spritecollide(
            self.player, self.green_block_list, True)
        self.red_block_hit_list = pygame.sprite.spritecollide(
            self.player, self.red_block_list, True)
        for self.block in self.green_block_hit_list:
            self.remaining_count -= 1
            collect_green_sound.play()
            print("Remaining Green: ", self.remaining_count)
        for self.block in self.red_block_hit_list:
            self.player.lives -= 1
            collect_red_sound.play()
            print("Remaining Lives: ", self.player.lives)

        if self.remaining_count == 0:
            self.player.level = 5
            print("Player Level ", self.player.level)


class Level05(Level):
    def __init__(self, player):
        super().__init__(player)

        self.remaining_count = 30
        self.player = player
        self.red_block_list = pygame.sprite.Group()
        self.green_block_list = pygame.sprite.Group()
        for i in range(15):
            self.block = Block(RED, 20, 20, True)
            self.red_block_list.add(self.block)
            self.all_sprites_list.add(self.block)
        for i in range(30):
            self.block = Block(GREEN, 20, 20, True)
            self.green_block_list.add(self.block)
            self.all_sprites_list.add(self.block)

    def update(self):
        self.all_sprites_list.update()
        self.green_block_hit_list = pygame.sprite.spritecollide(
            self.player, self.green_block_list, True)
        self.red_block_hit_list = pygame.sprite.spritecollide(
            self.player, self.red_block_list, True)
        for self.block in self.green_block_hit_list:
            self.remaining_count -= 1
            collect_green_sound.play()
            print("Remaining Green: ", self.remaining_count)
        for self.block in self.red_block_hit_list:
            self.player.lives -= 1
            collect_red_sound.play()
            print("Remaining Lives: ", self.player.lives)

        if self.remaining_count == 0:
            self.player.level = 6
            print("Player Level ", self.player.level)


class Level06(Level):
    def __init__(self, player):
        super().__init__(player)

        self.purple_flip = False
        self.player = player
        self.red_block_list = pygame.sprite.Group()
        self.green_block_list = pygame.sprite.Group()
        self.purple_block_list = pygame.sprite.Group()
        self.green_blocks_count = 4
        self.red_blocks_count = 40
        self.remaining_count = self.green_blocks_count
        for i in range(self.red_blocks_count):
            self.block = Block(RED, 20, 20, True)
            self.red_block_list.add(self.block)
            self.all_sprites_list.add(self.block)
        for i in range(self.green_blocks_count):
            self.block = Block(GREEN, 20, 20, True)
            self.green_block_list.add(self.block)
            self.all_sprites_list.add(self.block)

        self.purple_block = Block(PURPLE, 40, 40, False)
        self.purple_block.rect.x = 650
        self.purple_block.rect.y = 250
        self.purple_block_list.add(self.purple_block)
        self.all_sprites_list.add(self.purple_block)

    def update(self):
        self.all_sprites_list.update()

        if self.purple_flip is False:
            self.green_block_hit_list = pygame.sprite.spritecollide(
                self.player, self.green_block_list, True)
            self.red_block_hit_list = pygame.sprite.spritecollide(
                self.player, self.red_block_list, True)
            self.purple_block_hit_list = pygame.sprite.spritecollide(
                self.player, self.purple_block_list, True)
            for self.block in self.green_block_hit_list:
                self.green_blocks_count -= 1
                collect_green_sound.play()
                print("Remaining Green: ", self.green_blocks_count)
            for self.block in self.red_block_hit_list:
                self.red_blocks_count -= 1
                self.player.lives -= 1
                collect_red_sound.play()
                print("Remaining Lives: ", self.player.lives)
            for self.block in self.purple_block_hit_list:
                collect_purple_sound.play()
                self.purple_flip = True
            self.remaining_count = self.green_blocks_count
            if self.remaining_count == 0:
                self.player.level = GAME_END
                print("Player Level ", self.player.level)
        else:
            for self.block in self.red_block_list:
                self.block.change_color(GREEN)
            self.new_green_block_list = self.red_block_list
            for self.block in self.green_block_list:
                self.block.change_color(RED)
            self.new_red_block_list = self.green_block_list
            self.red_block_hit_list = pygame.sprite.spritecollide(
                self.player, self.new_red_block_list, True)
            self.green_block_hit_list = pygame.sprite.spritecollide(
                self.player, self.new_green_block_list, True)
            for self.block in self.red_block_hit_list:
                self.player.lives -= 1
                collect_red_sound.play()
                self.red_blocks_count -= 1
                print("Remaining Red: ", len(self.new_red_block_list))
                print("Remaining Lives: ", self.player.lives)
            for self.block in self.green_block_hit_list:
                self.green_blocks_count -= 1
                collect_green_sound.play()
                print("Remaining Green: ", len(self.new_green_block_list))

            self.remaining_count = len(self.new_green_block_list)
            if self.remaining_count == 0:
                self.player.level = GAME_END
                print("Player Level ", self.player.level)


pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()
game = Game()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("Sprite Colllector")
pygame.mixer.music.load("mythica.mp3")
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)

collect_green_sound = pygame.mixer.Sound("coin7.wav")
collect_red_sound = pygame.mixer.Sound("coin10.wav")
collect_purple_sound = pygame.mixer.Sound("coin1.wav")
# Loop until the user clicks the close button.
done = False
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
