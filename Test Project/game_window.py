import pygame

pygame.init()

# Define some colors
BLACK = (0,   0,   0)
WHITE = (255, 255, 255)
GREEN = (0, 255,   0)
RED = (255,   0,   0)
BLUE = (0,   0, 255)


# Fonts
font = pygame.font.Font("C:\\Windows\\Fonts\\SitkaZ.ttc", 25)

# pi defined
PI = 3.141592653


size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Zain's Cool Game")


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
    screen.fill(WHITE)

    y_offset = 0
    while y_offset < 100:
        pygame.draw.line(screen, RED, [0, 10+y_offset], [100, 110+y_offset], 5)
        y_offset = y_offset + 10

    for x in range(0, 100, 20):
        pygame.draw.line(screen, GREEN, [x, 0], [x, 100], 5)
        pygame.draw.rect(screen, BLACK, [100, 100, 100, 100], 2)
        pygame.draw.ellipse(screen, BLACK, [100, 100, 100, 100], 2)
        pygame.draw.arc(screen, BLACK, [200, 200, 200, 200], 0, PI/2, 2)
        pygame.draw.arc(screen, GREEN, [200, 200, 200, 200], PI/2, PI, 2)
        pygame.draw.arc(screen, RED, [200, 200, 200, 200], PI, 3/2 * PI, 2)
        pygame.draw.arc(screen, BLUE, [200, 200, 200, 200], 3/2 * PI, 0, 2)

        pygame.draw.polygon(screen, BLACK, [[200, 200], [300, 100], [
                            400, 200, ], [400, 400, ], [200, 400], [200, 200]], 2)

        text_you_win = font.render("YOU WIN!", True, BLACK)
        screen.blit(text_you_win, [100, 100])
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    # --- Limit to 60 frames per second
    clock.tick(60)

pygame.quit()
