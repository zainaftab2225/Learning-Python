import pygame


# Define some colors as global constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
SKY_BLUE = (137, 196, 244)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.player_left_image = pygame.image.load('player_left.png').convert_alpha()
        self.player_right_image = pygame.image.load('player_right.png').convert_alpha()
        self.player_up_image = pygame.image.load('player_up.png').convert_alpha()
        self.player_down_image = pygame.image.load('player_down.png').convert_alpha()
        self.image = pygame.image.load('player_left.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.change_x = 0
        self.change_y = 0

    def change_sprite(self, image):
        self.image = image

    def change_speed(self, x, y):
        self.change_x += x
        self.change_y += y

    def update(self):
        old_rect_x = self.rect.x
        old_rect_y = self.rect.y
        self.rect.x += self.change_x
        self.rect.y += self.change_y

        if self.rect.x > old_rect_x:
            self.change_sprite(self.player_right_image)
        if self.rect.x < old_rect_x:
            self.change_sprite(self.player_left_image)
        if self.rect.y > old_rect_y:
            self.change_sprite(self.player_down_image)
        if self.rect.y < old_rect_y:
            self.change_sprite(self.player_up_image)

    def player_move():
        pass


class Game():
    def __init__(self):
        self.game_over_flag = False
        self.player = Player(100, 100)
        self.all_sprites_list = pygame.sprite.Group()
        self.all_sprites_list.add(self.player)

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.change_speed(-5, 0)
                elif event.key == pygame.K_RIGHT:
                    self.player.change_speed(5, 0)
                elif event.key == pygame.K_UP:
                    self.player.change_speed(0, -5)
                elif event.key == pygame.K_DOWN:
                    self.player.change_speed(0, 5)
                elif event.key == pygame.K_SPACE and self.game_over_flag is True:
                    self.__init__()
            # Reset speed when key goes up
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.player.change_speed(5, 0)
                elif event.key == pygame.K_RIGHT:
                    self.player.change_speed(-5, 0)
                elif event.key == pygame.K_UP:
                    self.player.change_speed(0, 5)
                elif event.key == pygame.K_DOWN:
                    self.player.change_speed(0, -5)

    def run_logic(self):
        print("Define Logic Here")
        self.player.update()

    def display_frame(self, screen):

        screen.fill(WHITE)
        self.all_sprites_list.draw(screen)
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
