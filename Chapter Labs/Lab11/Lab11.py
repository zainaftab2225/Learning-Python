import pygame
import random


# Define some colors as global constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
SKY_BLUE = (137, 196, 244)


def main():
    """ Main function for the game. """
    pygame.init()

    # Set the width and height of the screen [width,height]
    size = [800, 600]
    screen = pygame.display.set_mode(size)
    pygame.mouse.set_visible(False)
    pygame.display.set_caption("My Game")
    player_x_coord = 10
    player_y_coord = 10
    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    win_sound = pygame.mixer.Sound("my_sound.wav")
    player_image = pygame.image.load("images/bee.png").convert_alpha()
    cloud1_image = pygame.image.load("images/cloud1.png").convert_alpha()
    final_image = pygame.image.load("images/final_image.jpg").convert()
    cloud2_image = pygame.image.load("images/cloud3.png").convert_alpha()
    coin_image = pygame.image.load("images/coinGold.png").convert_alpha()
    chain_image = pygame.image.load("images/chain.png").convert_alpha()
    plant_image = pygame.image.load("images/plant.png").convert_alpha()
    weight_image = pygame.image.load("images/weightChained.png").convert_alpha()
    box_image = pygame.image.load("images/box.png").convert_alpha()
    box_alt_image = pygame.image.load("images/boxAlt.png").convert_alpha()
    grass_image = pygame.image.load("images/grassMid.png").convert_alpha()
    grass_cliffleft_image = pygame.image.load("images/grassCliffLeft.png").convert_alpha()
    grass_cliffright_image = pygame.image.load("images/grassCliffRight.png").convert_alpha()
    liquid_water_image = pygame.image.load("images/liquidWater.png").convert()
    liquid_water_top_mid_image = pygame.image.load("images/liquidWaterTop_mid.png").convert_alpha()
    # -------- Main Program Loop -----------
    while not done:
        # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                done = True
        player_pos = pygame.mouse.get_pos()

        # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT

        # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT
        player_new_x_coord = player_pos[0]
        player_new_y_coord = player_pos[1]

        if player_new_x_coord >= 0 and player_new_x_coord + 50 <= 800:
            player_x_coord = player_new_x_coord

        if player_new_y_coord >= 0 and player_new_y_coord + 20 <= 460:
            player_y_coord = player_new_y_coord
        print(player_x_coord, player_y_coord)

        # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT

        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        screen.fill(SKY_BLUE)

        for i in range(0, 800, 100):
            screen.blit(cloud1_image, [10+i+i, 100])
            screen.blit(cloud2_image, [10+1, 100])

        for i in range(0, 280, 70):
            screen.blit(chain_image, [550, i])
        screen.blit(weight_image, [550, 280])
        screen.blit(coin_image, [700, 300])
        for x in range(0, 800, 70):
            screen.blit(liquid_water_top_mid_image, [x, 460])
        for x in range(0, 800, 70):
            screen.blit(liquid_water_image, [x, 530])

        # grass
        screen.blit(grass_cliffleft_image, [210, 460])
        screen.blit(grass_image, [280, 460])
        screen.blit(grass_cliffright_image, [350, 460])
        screen.blit(plant_image, [350, 390])

        screen.blit(box_image, [280, 390])
        screen.blit(box_image, [280, 320])
        screen.blit(box_alt_image, [280, 250])

        screen.blit(player_image, [player_x_coord, player_y_coord])
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        # Go ahead and update the screen with what we've drawn.

        if player_new_x_coord >= 670 and player_new_x_coord <= 700 and player_new_y_coord >= 300 and player_new_y_coord <= 370:
            done = True
            print("playing sound")
            win_sound.play()
            # win_sound.play()

        pygame.display.flip()

        # Limit to 60 frames per second
        clock.tick(60)

    final_done = False
    while not final_done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                final_done = True
        screen.blit(final_image, [-300, 0])
        pygame.display.flip()
        clock.tick(60)
    # Close the window and quit.
    # If you forget this line, the program will 'hang'
    # on exit if running from IDLE.
    pygame.quit()


if __name__ == "__main__":
    main()
