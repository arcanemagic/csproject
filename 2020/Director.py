import pygame

class Director:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 800))
        self.scale = int(pygame.display.get_surface().get_width() / 400)
        pygame.display.set_caption("Snake It Off")
        pygame.display.set_icon(pygame.image.load("images\snake.png"))
        self.font = pygame.font.Font("fonts\AD.ttf", 30 * self.scale)
        self.scene = None
        self.fps = 15
        self.quit_flag = False
        self.p1color = (16, 99, 232)
        self.p2color = (25, 232, 14)
        self.index_one = 0
        self.index_two = 1
        self.clock = pygame.time.Clock()

    def loop(self):

        while not self.quit_flag:
            time = self.clock.tick(self.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.quit()
                self.scene.on_event(event)
            self.scene.on_update()
            self.scene.on_draw(self.screen)
            pygame.display.flip()

    def change_scene(self, scene):
        self.scene = scene

    def quit(self):
        pygame.QUIT
        self.quit_flag = True
