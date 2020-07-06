"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""
import random
import pygame

# FPS
FPS = 10
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Position of Rectangle
rect_x = 50
rect_y = 50

# Direction and Speed
rect_change_x = 5
rect_change_y = 3

snow_list = []
for i in range(50):
    x = random.randrange(0, 700)
    y = random.randrange(0, 500)
    snow_list.append([x, y])

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here
    rect_x += rect_change_x
    rect_y += rect_change_y
    if rect_x > 649:
        rect_change_x *= -1
    if rect_y > 449:
        rect_change_y *= -1
    if rect_x < 1:
        rect_change_x *= -1
    if rect_y < 1:
        rect_change_y *= -1

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, [rect_x, rect_y, 50, 50])
    for item in snow_list:
        item[1] += 1
        pygame.draw.circle(screen, WHITE, item, 4)

        if item[1] > 500:
            item[1] = random.randrange(-20, -5)
            item[0] = random.randrange(400)

    # --- Drawing code should go here

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(FPS)

# Close the window and quit.
pygame.quit()
