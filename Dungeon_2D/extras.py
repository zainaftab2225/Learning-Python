self.player_image_up = pygame.image.load("player_up.png").convert_alpha()
self.player_image_down = pygame.image.load("player_down.png").convert_alpha()
self.player_image_left = pygame.image.load("player_left.png").convert_alpha()
self.player_image_right = pygame.image.load("player_right.png").convert_alpha()

final_wall_list = pygame.sprite.Group()
# Bottom Walls 1
wall = Wall("bottom_left")
wall.set_wall_attributes(0, 768)
self.all_sprites_list.add(wall)
final_wall_list.add(wall)

wall = Wall("bottom_right")
wall.set_wall_attributes(768, 768)
 self.all_sprites_list.add(wall)
  final_wall_list.add(wall)

   for i in range(0, 192, 32):
        wall = Wall("bottom")
        wall.set_wall_attributes(32+i, 768)
        self.all_sprites_list.add(wall)
        final_wall_list.add(wall)

    wall = Wall("bottom_right")
    wall.set_wall_attributes(224, 768)
    self.all_sprites_list.add(wall)
    final_wall_list.add(wall)

    for i in range(512, 736, 32):
        wall = Wall("bottom")
        wall.set_wall_attributes(32+i, 768)
        self.all_sprites_list.add(wall)
        final_wall_list.add(wall)

    wall = Wall("bottom_left")
    wall.set_wall_attributes(512, 768)
    self.all_sprites_list.add(wall)
    final_wall_list.add(wall)

    for i in range(224, 480, 32):
        wall = Wall("bottom")
        wall.set_wall_attributes(32+i, 768)
        self.all_sprites_list.add(wall)
        final_wall_list.add(wall)

    # Bottom Walls 2
    wall = Wall("bottom_left")
    wall.set_wall_attributes(0, 448)
    self.all_sprites_list.add(wall)
    final_wall_list.add(wall)

    wall = Wall("bottom_right")
    wall.set_wall_attributes(768, 448)
    self.all_sprites_list.add(wall)
    final_wall_list.add(wall)

    for i in range(0, 192, 32):
        wall = Wall("bottom")
        wall.set_wall_attributes(32+i, 448)
        self.all_sprites_list.add(wall)
        final_wall_list.add(wall)

    wall = Wall("bottom_right")
    wall.set_wall_attributes(224, 448)
    self.all_sprites_list.add(wall)
    final_wall_list.add(wall)

    for i in range(512, 736, 32):
        wall = Wall("bottom")
        wall.set_wall_attributes(32+i, 448)
        self.all_sprites_list.add(wall)
        final_wall_list.add(wall)

    wall = Wall("bottom_left")
    wall.set_wall_attributes(512, 448)
    self.all_sprites_list.add(wall)
    final_wall_list.add(wall)

    # Left Walls 1
    for i in range(0, 288, 32):
        wall = Wall("left")
        wall.set_wall_attributes(0, 480+i)
        self.all_sprites_list.add(wall)
        final_wall_list.add(wall)

    for i in range(0, 288, 32):
        wall = Wall("left")
        wall.set_wall_attributes(0, 480+i)
        self.all_sprites_list.add(wall)
        final_wall_list.add(wall)
