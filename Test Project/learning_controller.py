# Import a library of functions called 'pygame'
import pygame

BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
RED = [255, 0, 0]


def draw_snowman(screen, x, y):
    """ --- Function for a snowman ---
    Define a function that will draw a snowman at a certain location.
    """
    pygame.draw.ellipse(screen, WHITE, [35 + x, 0 + y, 25, 25])
    pygame.draw.ellipse(screen, WHITE, [23 + x, 20 + y, 50, 50])
    pygame.draw.ellipse(screen, WHITE, [0 + x, 65 + y, 100, 100])


def draw_stick_figure(screen, x, y):
    # Head
    pygame.draw.ellipse(screen, BLACK, [1+x, y, 10, 10], 0)

    # Legs
    pygame.draw.line(screen, BLACK, [5+x, 17+y], [10+x, 27+y], 3)
    pygame.draw.line(screen, BLACK, [5+x, 17+y], [x, 27+y], 3)

    # Body
    pygame.draw.line(screen, RED, [5+x, 17+y], [5+x, 7+y], 3)

    # Arms
    pygame.draw.line(screen, RED, [5+x, 7+y], [9+x, 17+y], 3)
    pygame.draw.line(screen, RED, [5+x, 7+y], [1+x, 17+y], 3)


# Initialize the game engine
pygame.init()

# Set the height and width of the screen
size = [400, 500]
screen = pygame.display.set_mode(size)

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)

# Speed in pixels per frame
x_speed = 0
y_speed = 0

# Current position
x_coord = 10
y_coord = 10

pygame.key.set_repeat(3, 8)
joystick_count = pygame.joystick.get_count()
if joystick_count == 0:
    # No joysticks!
    print("Error, I didn't find any joysticks.")
else:
    # Use joystick #0 and initialize it
    my_joystick = pygame.joystick.Joystick(0)
    my_joystick.init()
    print("PS4 Connceted.")

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
            if event.key == pygame.K_LEFT:
                x_speed = -10
            elif event.key == pygame.K_RIGHT:
                x_speed = 10
            elif event.key == pygame.K_UP:
                y_speed = -10
            elif event.key == pygame.K_DOWN:
                y_speed = 10
        # User let up on a key
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0

        if joystick_count != 0:

            # This gets the position of the axis on the game controller
            # It returns a number between -1.0 and +1.0
            horiz_axis_pos = my_joystick.get_axis(0)
            vert_axis_pos = my_joystick.get_axis(1)

            # Move x according to the axis. We multiply by 10 to speed up the movement.
            # Convert to an integer because we can't draw at pixel 3.5, just 3 or 4.
            new_x = x_coord + int(horiz_axis_pos * 10)
            if new_x >= 0 and new_x + 10 <= 400:
                x_coord = x_coord + int(horiz_axis_pos * 10)
            new_y = y_coord + int(vert_axis_pos * 10)
            if new_y >= 0 and new_y + 30 <= 500:
                y_coord = y_coord + int(vert_axis_pos * 10)

        # Move the object according to the speed vector.
        x_coord += x_speed
        y_coord += y_speed

        pos = pygame.mouse.get_pos()
        x = pos[0]
        y = pos[1]
        # Clear the screen and set the screen background
        screen.fill(WHITE)

        # Go ahead and update the screen with what we've drawn.
        draw_stick_figure(screen, x_coord, y_coord)
        # This MUST happen after all the other drawing commands.
        pygame.display.flip()

        # This limits the while loop to a max of 60 times per second.
        # Leave this out and we will use all CPU we can.
        clock.tick(60)


# Be IDLE friendly
pygame.quit()
