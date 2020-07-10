import pygame
import random


# Define some colors as global constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
SKY_BLUE = (137, 196, 244)


class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()


def main():
    """ Main function for the game. """
    pygame.init()

    # Set the width and height of the screen [width,height]
    screen_width = 700
    screen_height = 500
    screen = pygame.display.set_mode([screen_width, screen_height])

    pygame.display.set_caption("My Game")

    block_list = pygame.sprite.Group()
    all_sprites_list = pygame.sprite.Group()

    for i in range(50):
        block = Block(BLACK, 20, 15)
        block.rect.x = random.randrange(screen_width-20)
        block.rect.y = random.randrange(screen_height-15)
        block_list.add(block)
        all_sprites_list.add(block)

    player = Block(RED, 30, 30)
    all_sprites_list.add(player)
    score = 0
    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while not done:
        # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        mouse_position = pygame.mouse.get_pos()
        player.rect.x = mouse_position[0]
        player.rect.y = mouse_position[1]
        # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT

        # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT
        block_hit_list = pygame.sprite.spritecollide(player, block_list, True)
        for block in block_hit_list:
            score += 1
            print(score)
        # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        screen.fill(WHITE)
        all_sprites_list.draw(screen)
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # Limit to 60 frames per second
        clock.tick(60)

    # Close the window and quit.
    # If you forget this line, the program will 'hang'
    # on exit if running from IDLE.
    pygame.quit()


if __name__ == "__main__":
    main()
