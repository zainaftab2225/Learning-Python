import pygame


# Define some colors as global constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
SKY_BLUE = (137, 196, 244)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
ROWS = 25
COLS = 25


class Wall(pygame.sprite.Sprite):
    """ Wall the player can run into. """

    def __init__(self, wall_choice):
        """ Constructor for the wall that the player can run into. """
        # Call the parent's constructor
        super().__init__()

        # Make a blue wall, of the size specified in the parameters
        self.wall_choice = wall_choice

    def set_wall_attributes(self, x, y):
        if self.wall_choice == "bottom_left":
            self.image = pygame.transform.scale(
                pygame.image.load('wall_bottom_left.png').convert_alpha(), (32, 32))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
        elif self.wall_choice == "bottom_right":
            self.image = pygame.transform.scale(
                pygame.image.load('wall_bottom_right.png').convert_alpha(), (32, 32))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
        elif self.wall_choice == "bottom":
            self.image = pygame.transform.scale(
                pygame.image.load('wall_bottom.png').convert_alpha(), (32, 32))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
        elif self.wall_choice == "top_left":
            self.image = pygame.transform.scale(
                pygame.image.load('wall_top_left.png').convert_alpha(), (32, 32))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
        elif self.wall_choice == "top_right":
            self.image = pygame.transform.scale(
                pygame.image.load('wall_top_right.png').convert_alpha(), (32, 32))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
        elif self.wall_choice == "top":
            self.image = pygame.transform.scale(
                pygame.image.load('wall_top.png').convert_alpha(), (32, 32))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
        elif self.wall_choice == "left":
            self.image = pygame.transform.scale(
                pygame.image.load('wall_left.png').convert_alpha(), (32, 32))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
        elif self.wall_choice == "right":
            self.image = pygame.transform.scale(
                pygame.image.load('wall_right.png').convert_alpha(), (32, 32))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y


class Door(pygame.sprite.Sprite):
    def __init__(self, x, y):
        """ Constructor for the wall that the player can run into. """
        # Call the parent's constructor
        super().__init__()
        self.door_open = False
        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.transform.scale(
            pygame.image.load('door.png').convert_alpha(), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def unlock(self, all_sprites_list, all_doors_list, player, door):
        all_sprites_list.remove(door)
        all_doors_list.remove(door)


class Floor(pygame.sprite.Sprite):
    """ Wall the player can run into. """

    def __init__(self, x, y):
        """ Constructor for the wall that the player can run into. """
        # Call the parent's constructor
        super().__init__()
        self.image = pygame.transform.scale(
            pygame.image.load('floor.png').convert_alpha(), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Grass(pygame.sprite.Sprite):
    """ Wall the player can run into. """

    def __init__(self, x, y):
        """ Constructor for the wall that the player can run into. """
        # Call the parent's constructor
        super().__init__()
        self.image = pygame.transform.scale(
            pygame.image.load('grass.png').convert_alpha(), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.player_left_image = pygame.transform.scale(
            pygame.image.load('player_left.png').convert_alpha(), (32, 32))
        self.player_right_image = pygame.transform.scale(
            pygame.image.load('player_right.png').convert_alpha(), (32, 32))
        self.player_up_image = pygame.transform.scale(
            pygame.image.load('player_up.png').convert_alpha(), (32, 32))
        self.player_down_image = pygame.transform.scale(
            pygame.image.load('player_down.png').convert_alpha(), (32, 32))
        self.image = pygame.transform.scale(pygame.image.load(
            'player_left.png').convert_alpha(), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.change_x = 0
        self.change_y = 0
        self.walls = None
        self.doors = None

    def change_sprite(self, image):
        self.image = image

    def change_speed(self, x, y):
        self.change_x += x
        self.change_y += y

    def update(self):

        old_rect_x = self.rect.x
        old_rect_y = self.rect.y

        self.rect.x += self.change_x
        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if self.change_x > 0:
                print(block.rect.left, " ", block.rect.right, " ", self.rect.right)
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right


        door_hit_list = pygame.sprite.spritecollide(self, self.doors, False)
        for door in door_hit_list:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if self.change_x > 0:
                self.rect.right = door.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = door.rect.right

        self.rect.y += self.change_y
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom

        door_hit_list = pygame.sprite.spritecollide(self, self.doors, False)
        for door in door_hit_list:
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = door.rect.top
            else:
                self.rect.top = door.rect.bottom

        if self.rect.x > old_rect_x:
            self.change_sprite(self.player_right_image)
        if self.rect.x < old_rect_x:
            self.change_sprite(self.player_left_image)
        if self.rect.y > old_rect_y:
            self.change_sprite(self.player_down_image)
        if self.rect.y < old_rect_y:
            self.change_sprite(self.player_up_image)


class Game():
    def __init__(self):
        self.all_sprites_list = pygame.sprite.Group()
        self.game_over_flag = False
        self.player = Player(100, 100)
        self.create_floor()
        self.create_grass()
        self.door = Door(385, 160)
        self.all_door_list = pygame.sprite.Group()
        self.all_door_list.add(self.door)

        self.wall_list = self.create_walls()
        self.player.walls = self.wall_list
        self.player.doors = self.all_door_list
        self.all_sprites_list.add(self.door)
        self.all_sprites_list.add(self.player)

    def create_walls(self):
        final_wall_list = pygame.sprite.Group()

        for i in range(192, SCREEN_HEIGHT, 32):
            wall = Wall("left")
            wall.set_wall_attributes(0, i)
            self.all_sprites_list.add(wall)
            final_wall_list.add(wall)

        for i in range(192, SCREEN_HEIGHT, 32):
            wall = Wall("right")
            wall.set_wall_attributes(768, i)
            self.all_sprites_list.add(wall)
            final_wall_list.add(wall)

        for i in range(0, SCREEN_WIDTH, 32):
            wall = Wall("bottom")
            wall.set_wall_attributes(i, 768)
            self.all_sprites_list.add(wall)
            final_wall_list.add(wall)

        for i in range(0, SCREEN_WIDTH//2-32,32):
            wall = Wall("top")
            wall.set_wall_attributes(i, 192)
            self.all_sprites_list.add(wall)
            final_wall_list.add(wall)

        # balcony opening
        for i in range(SCREEN_WIDTH//2+18, SCREEN_WIDTH, 32):
            wall = Wall("top")
            wall.set_wall_attributes(i, 192)
            self.all_sprites_list.add(wall)
            final_wall_list.add(wall)

        for i in range(192, SCREEN_HEIGHT//2, 32):
            wall = Wall("right")
            wall.set_wall_attributes(256, i)
            self.all_sprites_list.add(wall)
            final_wall_list.add(wall)

        for i in range(SCREEN_HEIGHT//2+96, SCREEN_HEIGHT, 32):
            wall = Wall("right")
            wall.set_wall_attributes(256, i)
            self.all_sprites_list.add(wall)
            final_wall_list.add(wall)

        for i in range(96, SCREEN_HEIGHT//2-128, 32):
            wall = Wall("top")
            wall.set_wall_attributes(i, 488)
            self.all_sprites_list.add(wall)
            final_wall_list.add(wall)

        wall = Wall("bottom_left")
        wall.set_wall_attributes(0, 768)
        self.all_sprites_list.add(wall)
        final_wall_list.add(wall)

        wall = Wall("bottom_right")
        wall.set_wall_attributes(768, 768)
        self.all_sprites_list.add(wall)
        final_wall_list.add(wall)

        wall = Wall("top_left")
        wall.set_wall_attributes(0, 192)
        self.all_sprites_list.add(wall)
        final_wall_list.add(wall)

        wall = Wall("top_right")
        wall.set_wall_attributes(768, 192)
        self.all_sprites_list.add(wall)
        final_wall_list.add(wall)

        wall = Wall("top_right")
        wall.set_wall_attributes(256, 192)
        self.all_sprites_list.add(wall)
        final_wall_list.add(wall)

        wall = Wall("bottom_right")
        wall.set_wall_attributes(256, 768)
        self.all_sprites_list.add(wall)
        final_wall_list.add(wall)

        wall = Wall("top_right")
        wall.set_wall_attributes(256, 488)
        self.all_sprites_list.add(wall)
        final_wall_list.add(wall)

        return final_wall_list

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.change_speed(-3, 0)
                elif event.key == pygame.K_RIGHT:
                    self.player.change_speed(3, 0)
                elif event.key == pygame.K_UP:
                    self.player.change_speed(0, -3)
                elif event.key == pygame.K_DOWN:
                    self.player.change_speed(0, 3)
                elif event.key == pygame.K_e:
                    self.door.unlock(self.all_sprites_list, self.all_door_list,
                                     self.player, self.door)
                elif event.key == pygame.K_SPACE and self.game_over_flag is True:
                    self.__init__()
            # Reset speed when key goes up
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.player.change_speed(3, 0)
                elif event.key == pygame.K_RIGHT:
                    self.player.change_speed(-3, 0)
                elif event.key == pygame.K_UP:
                    self.player.change_speed(0, 3)
                elif event.key == pygame.K_DOWN:
                    self.player.change_speed(0, -3)

    def create_grass(self):
        for i in range(0, SCREEN_WIDTH, 32):
            for j in range(0, 192, 32):
                grass = Grass(i, j)
                self.all_sprites_list.add(grass)

    def create_floor(self):
        for i in range(0, SCREEN_WIDTH, 32):
            for j in range(192, SCREEN_HEIGHT, 32):
                floor = Floor(i, j)
                self.all_sprites_list.add(floor)

    def draw_grid(self, screen):
        size_between = SCREEN_WIDTH // ROWS
        x = 0
        y = 0
        for i in range(ROWS):
            x = x+size_between
            y = y+size_between
            pygame.draw.line(screen, BLACK, (x, 0), (x, SCREEN_WIDTH))
            pygame.draw.line(screen, BLACK, (0, y), (SCREEN_HEIGHT, y))

    def run_logic(self):
        self.player.update()

    def display_frame(self, screen):

        screen.fill(WHITE)
        self.draw_grid(screen)
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
