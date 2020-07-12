import pygame
import random

# Define some colors as global constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
SKY_BLUE = (137, 196, 244)
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
ROWS = 20


class Cube(object):
    rows = ROWS
    w = SCREEN_WIDTH

    def __init__(self, start, direction_x=1, direction_y=0, color=RED):
        self.position = start
        self.direction_x = 1
        self.direction_y = 0
        self.color = color

    def move(self, direction_x, direction_y):
        self.direction_x = direction_x
        self.direction_y = direction_y
        self.position = (self.position[0] + self.direction_x, self.position[1] + self.direction_y)

    def draw(self, screen, eyes=False):
        distance = SCREEN_WIDTH // ROWS
        i = self.position[0]
        j = self.position[1]

        pygame.draw.rect(screen, self.color, (i*distance+1, j*+distance+1, distance-2, distance-2))
        if eyes:
            centre = distance//2
            radius = 3
            circleMiddle = (i*distance+centre-radius, j*distance+8)
            circleMiddle2 = (i*distance + distance - radius*2, j*distance+8)
            pygame.draw.circle(screen, BLACK, circleMiddle, radius)
            pygame.draw.circle(screen, BLACK, circleMiddle2, radius)


class Snake(object):
    body = []
    turns = {}

    def __init__(self, color, position):
        self.color = color
        self.head = Cube(position)
        self.body.append(self.head)
        self.direction_x = 0
        self.direction_y = 1

    def change_left(self):
        self.direction_x = -1
        self.direction_y = 0
        self.turns[self.head.position[:]] = [self.direction_x, self.direction_y]

    def change_right(self):
        self.direction_x = 1
        self.direction_y = 0
        self.turns[self.head.position[:]] = [self.direction_x, self.direction_y]

    def change_up(self):
        self.direction_x = 0
        self.direction_y = -1
        self.turns[self.head.position[:]] = [self.direction_x, self.direction_y]

    def change_down(self):
        self.direction_x = 0
        self.direction_y = 1
        self.turns[self.head.position[:]] = [self.direction_x, self.direction_y]

    def move(self):
        for i, c in enumerate(self.body):
            p = c.position[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0], turn[1])
                if i == len(self.body)-1:
                    self.turns.pop(p)
            else:
                if c.direction_x == -1 and c.position[0] <= 0:
                    c.position = (c.rows-1, c.position[1])
                elif c.direction_x == 1 and c.position[0] >= c.rows-1:
                    c.position = (0, c.position[1])
                elif c.direction_y == 1 and c.position[1] >= c.rows-1:
                    c.position = (c.position[0], 0)
                elif c.direction_y == -1 and c.position[1] <= 0:
                    c.position = (c.position[0], c.rows-1)
                else:
                    c.move(c.direction_x, c.direction_y)

    def reset(self, position):
        self.head = Cube(position)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.direction_x = 0
        self.direction_y = 1

    def add_cube(self):
        tail = self.body[-1]
        dir_x, dir_y = tail.direction_x, tail.direction_y

        if dir_x == 1 and dir_y == 0:
            self.body.append(Cube((tail.position[0]-1, tail.position[1])))
        elif dir_x == -1 and dir_y == 0:
            self.body.append(Cube((tail.position[0]+1, tail.position[1])))
        elif dir_x == 0 and dir_y == 1:
            self.body.append(Cube((tail.position[0], tail.position[1]-1)))
        elif dir_x == 0 and dir_y == -1:
            self.body.append(Cube((tail.position[0], tail.position[1]+1)))

        self.body[-1].direction_x = dir_x
        self.body[-1].direction_y = dir_y

    def draw(self, screen):
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(screen, True)
            else:
                c.draw(screen)


class Game():
    def __init__(self):
        self.game_over_flag = False
        self.snake = Snake(RED, (10, 10))
        self.snack = Cube(self.random_snack(self.snake), color=GREEN)

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            keys = pygame.key.get_pressed()

            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.snake.change_left()
                elif keys[pygame.K_RIGHT]:
                    self.snake.change_right()
                elif keys[pygame.K_UP]:
                    self.snake.change_up()
                elif keys[pygame.K_DOWN]:
                    self.snake.change_down()
            self.snake.move()

    def run_logic(self):
        self.snake.move()
        if self.snake.body[0].position == self.snack.position:
            self.snake.add_cube()
            self.snack = Cube(self.random_snack(self.snake), color=GREEN)

        for x in range(len(self.snake.body)):
            if self.snake.body[x].position in list(map(lambda z: z.position, self.snake.body[x+1:])):
                print("Score ", len(self.snake.body))
                self.snake.reset((10, 10))
                break

    def display_frame(self, screen):

        screen.fill(BLACK)
        self.draw_grid(screen)
        self.snack.draw(screen)
        self.snake.draw(screen)
        pygame.display.flip()

    def random_snack(self, item):
        positions = item.body
        while True:
            x = random.randrange(ROWS)
            y = random.randrange(ROWS)
            if len(list(filter(lambda z: z.position == (x, y), positions))) > 0:
                continue
            else:
                break
        return(x, y)

    def draw_grid(self, screen):
        size_between = SCREEN_WIDTH // ROWS
        x = 0
        y = 0
        for i in range(ROWS):
            x = x+size_between
            y = y+size_between
            pygame.draw.line(screen, BLACK, (x, 0), (x, SCREEN_WIDTH))
            pygame.draw.line(screen, BLACK, (0, y), (SCREEN_HEIGHT, y))


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
        pygame.time.delay(50)
        clock.tick(10)

    # Close the window and quit.
    # If you forget this line, the program will 'hang'
    # on exit if running from IDLE.
    pygame.quit()


if __name__ == "__main__":
    main()
