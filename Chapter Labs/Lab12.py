import pygame
import random


# Define some colors as global constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
SKY_BLUE = (137, 196, 244)


class Rectangle():
    def __init__(self, x=0, y=0, width=10, height=10, change_x=0, change_y=0, r=0, g=0, b=0):
        self.x = random.randrange(0, 700)
        self.y = random.randrange(0, 500)
        self.width = random.randrange(20, 70)
        self.height = random.randrange(20, 70)
        self.change_x = random.randrange(-3, 3)
        self.change_y = random.randrange(-3, 3)
        self.r = random.randrange(0, 255)
        self.g = random.randrange(0, 255)
        self.b = random.randrange(0, 255)
        print("Rectangle created")

    def draw(self, screen):
        pygame.draw.rect(screen, (self.r, self.g, self.b), [
                         self.x, self.y, self.width, self.height])

    def move(self):
        self.x += self.change_x
        self.y += self.change_y

        if self.x > 700-self.width:
            self.change_x *= -1
        if self.y > 500-self.height:
            self.change_y *= -1
        if self.x < 1:
            self.change_x *= -1
        if self.y < 1:
            self.change_y *= -1


class Ellipse(Rectangle):
    def __init__(self):
        super().__init__()

    def draw(self, screen):
        pygame.draw.ellipse(screen, (self.r, self.g, self.b), [
                            self.x, self.y, self.width, self.height])


def main():
    """ Main function for the game. """
    pygame.init()

    # Set the width and height of the screen [width,height]
    size = [700, 500]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("My Game")

    # Loop until the user clicks the close button.
    done = False
    my_list = []
    for i in range(100):
        my_object = Rectangle()
        my_list.append(my_object)
    for i in range(100):
        my_object = Ellipse()
        my_list.append(my_object)
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while not done:
        # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT

        # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT

        # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT

        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        screen.fill(WHITE)
        for i in range(200):
            my_list[i].draw(screen)
            my_list[i].move()

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
