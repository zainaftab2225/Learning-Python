import pygame
import math
import time

pygame.init()

# Define some colors
BLACK = (0,   0,   0)
WHITE = (255, 255, 255)
GREEN = (0, 255,   0)
RED = (255,   0,   0)
BLUE = (0,   0, 255)
NIGHT_BLUE = (5, 5, 55)
MOON_COLOR = (227, 227, 227)
MOON_DETAILS = (186, 186, 186)
DARK_ORANGE = (107, 62, 10)
DARK_GREY = (125, 131, 140)
YELLOW_LIGHT = (240, 247, 17)


size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Lab 5 Drawing")


# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
    # --- Game logic should go here

    # --- Drawing code should go here

    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    # Sky
    screen.fill(NIGHT_BLUE)
    # Stars

    pygame.draw.ellipse(screen, WHITE, [180, 120, 10, 10])
    pygame.draw.ellipse(screen, WHITE, [600, 100, 10, 10])
    pygame.draw.ellipse(screen, WHITE, [250, 50, 10, 10])

    for x_offset in range(0, 800, 200):
        pygame.draw.ellipse(screen, WHITE, [100+x_offset, 50, 5, 5])

    for x_offset in range(0, 800, 400):
        pygame.draw.ellipse(screen, WHITE, [140+x_offset, 100, 5, 5])

    for x_offset in range(0, 800, 250):
        pygame.draw.ellipse(screen, WHITE, [220+x_offset, 150, 5, 5])

    for x_offset in range(0, 800, 300):
        pygame.draw.ellipse(screen, WHITE, [100+x_offset, 180, 5, 5])

    # Moon
    pygame.draw.ellipse(screen, MOON_COLOR, [50, 50, 100, 100])
    pygame.draw.ellipse(screen, MOON_DETAILS, [100, 70, 20, 25])
    pygame.draw.ellipse(screen, MOON_DETAILS, [80, 80, 20, 15])
    pygame.draw.ellipse(screen, MOON_DETAILS, [100, 100, 30, 40])
    pygame.draw.ellipse(screen, MOON_DETAILS, [60, 90, 10, 5])
    pygame.draw.ellipse(screen, MOON_DETAILS, [60, 85, 5, 10])
    pygame.draw.ellipse(screen, MOON_DETAILS, [90, 55, 15, 15])

    # Buildings
    pygame.draw.rect(screen, DARK_GREY, [200, 200, 300, 400])
    pygame.draw.rect(screen, DARK_ORANGE, [0, 300, 230, 300])
    pygame.draw.rect(screen, DARK_GREY, [600, 200, 200, 400])
    pygame.draw.rect(screen, DARK_ORANGE, [500, 400, 170, 400])

    # Windows
    for y_offset in range(0, 600, 100):
        pygame.draw.rect(screen, YELLOW_LIGHT, [50, 330+y_offset, 50, 70])
        pygame.draw.rect(screen, YELLOW_LIGHT, [150, 330+y_offset, 50, 70])

    pygame.draw.rect(screen, BLACK, [50, 330, 50, 70])

    for y_offset in range(0, 600, 100):
        pygame.draw.rect(screen, YELLOW_LIGHT, [260, 300+y_offset, 80, 80])
        pygame.draw.rect(screen, YELLOW_LIGHT, [390, 300+y_offset, 80, 80])

    pygame.draw.rect(screen, BLACK, [390, 400, 80, 80])

    for y_offset in range(0, 600, 100):
        pygame.draw.rect(screen, YELLOW_LIGHT, [530, 420+y_offset, 30, 80])
        pygame.draw.rect(screen, YELLOW_LIGHT, [590, 420+y_offset, 50, 80])
    # pygame.draw.ellipse(screen, WHITE, [130, 130, 5, 5])
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    # --- Limit to 60 frames per second
    clock.tick(60)

pygame.quit()
