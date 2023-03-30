import pygame
import pygame_gui


#Init stuffs
pygame.font.init()
pygame.init()
pygame.display.set_caption("3D RENDERERER OH YEAH!")
pack = "Default"

WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
MANAGER = pygame_gui.UIManager((WIDTH, HEIGHT))

#Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LIGHT_GREY = (155, 155, 155)

camera_pos = [0, 0, 0]


class box():
    def __init__(self, size, colour, position) -> None:
        self.size = size
        self.colour = colour
        self.position_x = position[0]
        self.position_y = position[1]
    
    def draw(self):
        #rect = pygame.Rect(self.position_x-camera_pos[0], self.position_y-camera_pos[1], self.size_x, self.size_y)
        #pygame.draw.rect(SCREEN, self.colour, rect)
        pygame.draw.lines(SCREEN, self.colour, True, [
            (self.position_x-camera_pos[0]+camera_pos[2], self.position_y-camera_pos[1]-camera_pos[2]),
            ((self.position_x+self.size[0])-camera_pos[0]-camera_pos[2],self.position_y-camera_pos[1]-camera_pos[2]),
            ((self.position_x+self.size[0])-camera_pos[0]-camera_pos[2], (self.position_y-self.size[1])-camera_pos[1]+camera_pos[2]),
            (self.position_x-camera_pos[0]+camera_pos[2], (self.position_y-self.size[1])-camera_pos[1]+camera_pos[2])
            ], 10)


def handle_camera_move(keys_pressed, speed):
    global camera_pos
    if keys_pressed[pygame.K_w]:
        camera_pos[2] -= speed
    if keys_pressed[pygame.K_s]:
        camera_pos[2] += speed
    if keys_pressed[pygame.K_a]:
        camera_pos[0] -= speed
    if keys_pressed[pygame.K_d]:
        camera_pos[0] += speed


def draw_screen(test_box):
    SCREEN.fill(WHITE)
    test_box.draw()
    MANAGER.draw_ui(SCREEN)
    pygame.display.update()


def main():
    global camera_pos
    clock = pygame.time.Clock()

    hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)),
                                             text='Say Hello',
                                             manager=MANAGER)
    test_box = box((100, 100), BLACK, (500, 500))
    camera_pos = [0, 0, 0]
    camera_speed = 5
    run = True
    while run:
        time_delta = clock.tick(60)/1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
            
            MANAGER.process_events(event)
        
        MANAGER.update(time_delta)

        keys_pressed = pygame.key.get_pressed()
        handle_camera_move(keys_pressed, camera_speed)

        draw_screen(test_box)

if __name__ == "__main__":
    main()
