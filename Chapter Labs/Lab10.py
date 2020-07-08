import pygame

# Define some colors as global constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BROWN = (139, 69, 19)

# Draw Tree Function


def draw_tree(screen, x, y):
    pygame.draw.polygon(screen, GREEN, [[110-100+x, 250-150+y],
                                        [190-100+x, 250-150+y], [150-100+x, 150-150+y]])
    pygame.draw.polygon(screen, GREEN, [[100-100+x, 300-150+y],
                                        [200-100+x, 300-150+y], [150-100+x, 200-150+y]])
    pygame.draw.rect(screen, BROWN, [140-100+x, 300-150+y, 20, 100])


def draw_triangle(screen, x, y):
    pygame.draw.polygon(screen, BLACK, [[100+x, 200+y], [200+x, 200+y], [150+x, 130+y]])


def main():

    # Tree attributes
    tree_x_coord = 0
    tree_y_coord = 0
    tree_x_speed = 10
    tree_y_speed = 10

    """ Main function for the game. """
    pygame.init()
    # Set the width and height of the screen [width,height]
    size = [700, 500]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("My Game")
    pygame.mouse.set_visible(True)
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

        tree_pos = pygame.mouse.get_pos()
        # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT

        # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT
        tree_new_x_coord = tree_pos[0]
        tree_new_y_coord = tree_pos[1]

        if tree_new_x_coord >= 0 and tree_new_x_coord + 80 <= 700:
            tree_x_coord = tree_new_x_coord
        if tree_new_y_coord >= 0 and tree_new_y_coord + 245 <= 500:
            tree_y_coord = tree_new_y_coord
            # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT

            # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT

            # First, clear the screen to white. Don't put other drawing commands
            # above this, or they will be erased with this command.
        screen.fill(WHITE)
        print(tree_x_coord, tree_y_coord)
        draw_tree(screen, tree_x_coord, tree_y_coord)
        #draw_triangle(screen, tree_x_coord, tree_y_coord)
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
