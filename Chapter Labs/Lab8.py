import pygame
import math
import time
import random

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

# Animating Lights

# Animating Snow
snow_coordinates = []
for i in range(100):
    x = random.randrange(0, 800)
    y = random.randrange(0, 600)
    snow_coordinates.append([x, y])

line_x = 700
line_y = 240
line_change_y = 1
line_change_x = 1
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
    # --- Game logic should go here
    random_light = random.randrange(0, 2)
    if line_x > 699 and line_y > 239 and line_x < 730 and line_y < 270:
        line_x += line_change_x
        line_y += line_change_y
        print("if 1")
    elif line_x > 700 and line_y < 300:
        line_x -= line_change_x
        line_y += line_change_y
        print("if 2")
    elif line_x > 670 and line_y > 270:
        line_x -= line_change_x
        line_y -= line_change_y
        print("if 3")
    elif line_x < 700 and line_y > 240:
        line_x += line_change_x
        line_y -= line_change_y
        print("if 4")
    print(line_x, line_y)
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
    for line_offset in range(40, 200, 40):
        pygame.draw.line(screen, WHITE, [600+line_offset, 350], [600+line_offset, 600], 4)
    pygame.draw.rect(screen, DARK_ORANGE, [500, 400, 170, 400])

    # Windows
    for y_offset in range(0, 600, 100):
        pygame.draw.rect(screen, YELLOW_LIGHT, [50, 330+y_offset, 50, 70])
        pygame.draw.rect(screen, YELLOW_LIGHT, [150, 330+y_offset, 50, 70])

    for y_offset in range(0, 600, 100):
        pygame.draw.rect(screen, YELLOW_LIGHT, [260, 300+y_offset, 80, 80])
        pygame.draw.rect(screen, YELLOW_LIGHT, [390, 300+y_offset, 80, 80])

    for y_offset in range(0, 600, 100):
        pygame.draw.rect(screen, YELLOW_LIGHT, [530, 420+y_offset, 30, 80])
        pygame.draw.rect(screen, YELLOW_LIGHT, [590, 420+y_offset, 50, 80])

    # Drawing Clock and Details
    pygame.draw.rect(screen, WHITE, [650, 220, 100, 100], 5)
    pygame.draw.circle(screen, WHITE, [700, 270], 40)
    pygame.draw.line(screen, BLACK, [700, 270], [line_x, line_y], 3)

    # Drawing Snow
    for coordinates in snow_coordinates:
        coordinates[1] += 5
        pygame.draw.circle(screen, DARK_GREY, coordinates, 1)

        if coordinates[1] > 600:
            coordinates[1] = random.randrange(-20, -5)
            coordinates[0] = random.randrange(800)

    # pygame.draw.ellipse(screen, WHITE, [130, 130, 5, 5])
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    # --- Limit to 60 frames per second
    clock.tick(60)

pygame.quit()
