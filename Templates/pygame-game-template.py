import pygame


# Define some colors as global constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
SKY_BLUE = (137, 196, 244)
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500


class Game():
    def __init__(self):
        self.game_over_flag = False

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True

    def run_logic(self):
        print("Define Logic Here")

    def display_frame(self, screen):

        screen.fill(WHITE)

        pygame.display.flip()


def main():
    """ Main function for the game. """
    pygame.init()

    # Set the width and height of the screen [width,height]
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    game = Game()
    pygame.display.set_caption("My Game")

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


if __name__ == "__main__":
    main()
