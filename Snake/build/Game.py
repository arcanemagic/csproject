from Scene import *
from Entity import *
import random
from pygame import gfxdraw

class mainGame(Scene):
    def __init__(self, director):
        Scene.__init__(self, director)
        self.plyronewins = False
        self.plyrtwowins = False
        self.plyrdraw = False
        self.plyronewins_txt = director.font.render("Player One Wins", True, (255, 255, 255))
        self.plyrtwowins_txt = director.font.render("Player Two Wins", True, (255, 255, 255))
        self.plyrdraw_txt = director.font.render("Draw", True, (255, 255, 255))
        self.screen_rect = director.screen.get_rect()
        self.plyr = pygame.font.Font("fonts\Condition.ttf", 20 * director.scale)
        self.txt = self.plyr.render("esc", True, (255, 255, 255))
        self.a = director.scale

        self.w, self.h = pygame.display.get_surface().get_size()
        self.dx1 = 10 * director.scale
        self.dy1 = 0
        self.dx2 = -10 * director.scale
        self.dy2 = 0

        #Snake 1
        self.head_1 = Entity(21 * director.scale, 1 * director.scale, 9 * director.scale, 9 * director.scale, (11, 27, 176))
        self.tail_1 = []

        #Snake 2
        self.head_2 = Entity(371 * director.scale, 1 * director.scale, 9 * director.scale, 9 * director.scale, (12, 120, 6))
        self.tail_2 = []

        self.apple = Entity(11 * director.scale, 11 * director.scale, 9 * director.scale, 9 * director.scale, (199, 10, 10))

        #Starting condition
        pygame.mixer.music.load("music\shake.ogg")
        pygame.mixer.music.play(-1)
        for i in range(1, 3):
            self.tail_1.append(Entity(self.head_1.x - 10 * i * director.scale, self.head_1.y * director.scale, 9 * director.scale, 9 * director.scale, self.director.p1color))
        for i in range(1, 3):
            self.tail_2.append(Entity(self.head_2.x + 10 * i * director.scale, self.head_2.y * director.scale, 9 * director.scale, 9 * director.scale, self.director.p2color))

    def on_event(self, event):
        #Snake 1 movement
        if event.type == pygame.KEYDOWN and event.key == pygame.K_w and self.dy1 == 0:
            self.dy1 = -10 * self.director.scale
            self.dx1 = 0
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s and self.dy1 == 0:
            self.dy1 = 10 * self.director.scale
            self.dx1 = 0
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a and self.dx1 == 0:
            self.dx1 = -10 * self.director.scale
            self.dy1 = 0
        if event.type == pygame.KEYDOWN and event.key == pygame.K_d and self.dx1 == 0:
            self.dx1 = 10 * self.director.scale
            self.dy1 = 0

        #Snake 2 movement
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP and self.dy2 == 0:
            self.dy2 = -10 * self.director.scale
            self.dx2 = 0
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN and self.dy2 == 0:
            self.dy2 = 10 * self.director.scale
            self.dx2 = 0
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT and self.dx2 == 0:
            self.dx2 = -10 * self.director.scale
            self.dy2 = 0
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT and self.dx2 == 0:
            self.dx2 = 10 * self.director.scale
            self.dy2 = 0

        #Reset game
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            pygame.mixer.music.stop()
            self.director.change_scene(mainGame(self.director))
            pygame.mixer.music.load("music\shake.ogg")
            pygame.mixer.music.play(-1)

        #Exit game
        if event.type == pygame.KEYDOWN and (event.key == pygame.K_ESCAPE):
            self.director.quit()

    def on_update(self):
        self.director.fps = 15

        if not self.plyronewins and not self.plyrtwowins and not self.plyrdraw:
            self.did_eat()

            #Movement: Snake 1
            for i in range(len(self.tail_1) - 1, 0, -1):
                self.tail_1[i].x = self.tail_1[i - 1].x
                self.tail_1[i].y = self.tail_1[i - 1].y
            self.tail_1[0].x, self.tail_1[0].y = (self.head_1.x, self.head_1.y)
            self.head_1.x += self.dx1
            self.head_1.y += self.dy1
            if self.head_1.x < 0:
                self.head_1.x = self.w - (9 * self.a)

            if self.head_1.x > self.w:
                self.head_1.x = self.a

            if self.head_1.y < 0:
                self.head_1.y = self.h - (9 * self.a)

            if self.head_1.y > self.h:
                self.head_1.y = self.a

            #Endgame check
            self.is_collide()
            if self.plyrdraw or self.plyronewins or self.plyrtwowins:
                return

            #Movement: Snake 2
            for i in range(len(self.tail_2) - 1, 0, -1):
                self.tail_2[i].x = self.tail_2[i - 1].x
                self.tail_2[i].y = self.tail_2[i - 1].y
            self.tail_2[0].x, self.tail_2[0].y = (self.head_2.x, self.head_2.y)
            self.head_2.x += self.dx2
            self.head_2.y += self.dy2
            if self.head_2.x < 0:
                self.head_2.x = self.w - (9 * self.a)

            if self.head_2.x > self.w:
                self.head_2.x = self.a

            if self.head_2.y < 0:
                self.head_2.y = self.h - (9 * self.a)

            if self.head_2.y > self.h:
                self.head_2.y = self.a

            #Endgame check
            self.is_collide()
            if self.plyrdraw or self.plyronewins or self.plyrtwowins:
                return

    def on_draw(self, screen):
        #Wipe screen
        self.director.screen.fill((0, 0, 0))

        self.draw_grid(screen)
        self.apple.draw(screen)
        self.head_1.draw(screen)
        self.head_2.draw(screen)
        self.print_tails(screen)

        #Player 1 wins
        if self.plyronewins:
            screen.blit(self.plyronewins_txt, self.plyronewins_txt.get_rect(center=self.screen_rect.center))
            self.gameEnd(screen)

        #Player 2 wins
        if self.plyrtwowins:
            screen.blit(self.plyrtwowins_txt, self.plyronewins_txt.get_rect(center=self.screen_rect.center))
            self.gameEnd(screen)

        #Draw
        if self.plyrdraw:
            screen.blit(self.plyrdraw_txt, self.plyrdraw_txt.get_rect(center=self.screen_rect.center))
            self.gameEnd(screen)

    def print_tails(self, screen):
        for i in range(len(self.tail_1)):
            pygame.draw.rect(screen, self.tail_1[i].color, self.tail_1[i].rect())
        for i in range(len(self.tail_2)):
            pygame.draw.rect(screen, self.tail_2[i].color, self.tail_2[i].rect())

    def draw_grid(self, screen):
        for i in range(40):
            pygame.draw.line(screen, (56, 56, 56), (i * 10 * self.director.scale, 0), (i * 10 * self.director.scale, self.h))

        for i in range(40):
            pygame.draw.line(screen, (56, 56, 56), (0, i * 10 * self.director.scale), (self.w, i * 10 * self.director.scale))

    def did_eat(self):
        spaceEmpty = True
        currX = self.apple.x
        currY = self.apple.y

        if self.head_1.x == self.apple.x and self.head_1.y == self.apple.y:
            prevX, prevY = currX, currY
            currX = myround(random.randint(0, self.w / 10 - 10 * self.director.scale), 10 * self.director.scale) * 10 + 1 * self.director.scale
            while prevX == currX:
                currX = myround(random.randint(0, self.w / 10 - 10 * self.director.scale), 10 * self.director.scale) * 10 + 1 * self.director.scale
            currY = myround(random.randint(0, self.h / 10 - 10 * self.director.scale), 10 * self.director.scale) * 10 + 1 * self.director.scale
            while prevY == currY:
                currY = myround(random.randint(0, self.h / 10 - 10 * self.director.scale), 10 * self.director.scale) * 10 + 1 * self.director.scale

            for i in self.tail_1:
                if currX == i.x and currY == i.y:
                    spaceEmpty = False
                    while not spaceEmpty and prevX != currX and prevY != currY:
                        currX = myround(random.randint(0, self.w / 10 - 10 * self.director.scale), 10 * self.director.scale) * 10 + 1 * self.director.scale
                        currY = myround(random.randint(0, self.h / 10 - 10 * self.director.scale), 10 * self.director.scale) * 10 + 1 * self.director.scale
                        for j in self.tail_1:
                            if currX == j.x and currY == j.y:
                                spaceEmpty = False
                                break
                            spaceEmpty = True

            self.tail_1.append(Entity(self.tail_1[len(self.tail_1) - 1].x * self.director.scale, self.tail_1[len(self.tail_1) - 1 * self.director.scale].y, 9 * self.director.scale, 9 * self.director.scale, self.director.p1color))

        if self.head_2.x == self.apple.x and self.head_2.y == self.apple.y:
            prevX, prevY = currX, currY
            currX = myround(random.randint(0, self.w / 10 - 10 * self.director.scale), 10 * self.director.scale) * 10 + 1 * self.director.scale
            while prevX == currX:
                currX = myround(random.randint(0, self.w / 10 - 10 * self.director.scale), 10 * self.director.scale) * 10 + 1 * self.director.scale
            currY = myround(random.randint(0, self.h / 10 - 10 * self.director.scale), 10 * self.director.scale) * 10 + 1 * self.director.scale
            while prevY == currY:
                currY = myround(random.randint(0, self.h / 10 - 10 * self.director.scale), 10 * self.director.scale) * 10 + 1 * self.director.scale
            for i in self.tail_2:
                if currX == i.x and currY == i.y:
                    spaceEmpty = False
                    while not spaceEmpty and prevX != currX and prevY != currY:
                        currX = myround(random.randint(0, self.w / 10 - 10 * self.director.scale), 10 * self.director.scale) * 10 + 1 * self.director.scale
                        currY = myround(random.randint(0, self.h / 10 - 10 * self.director.scale), 10 * self.director.scale) * 10 + 1 * self.director.scale
                        for j in self.tail_2:
                            if currX == j.x and currY == j.y:
                                spaceEmpty = False
                                break
                            spaceEmpty = True

            self.tail_2.append(Entity(self.tail_2[len(self.tail_2) - 1].x * self.director.scale, self.tail_2[len(self.tail_2) - 1 * self.director.scale].y, 9 * self.director.scale, 9 * self.director.scale, self.director.p2color))

        #Place new apple
        self.apple.x = currX
        self.apple.y = currY

    def is_collide(self): #Head-On Collision
        if self.head_1.x == self.head_2.x and self.head_1.y == self.head_2.y:
            self.plyrdraw = True
            pygame.mixer.music.stop()
            return

        for i in self.tail_1:
            if self.head_2.x == i.x and self.head_2.y == i.y:
                self.plyronewins = True
                pygame.mixer.music.stop()
                return

            if self.head_1.x == i.x and self.head_1.y == i.y:
                self.plyrtwowins = True
                pygame.mixer.music.stop()
                return

        for i in self.tail_2:
            if self.head_1.x == i.x and self.head_1.y == i.y:
                self.plyrtwowins = True
                pygame.mixer.music.stop()
                return

            if self.head_2.x == i.x and self.head_2.y == i.y:
                self.plyronewins = True
                pygame.mixer.music.stop()
                return

    def gameEnd(self, screen):
        self.txt = self.plyr.render("esc", True, (255, 255, 255))
        screen.blit(self.txt, (25 * self.director.scale, 7 * self.director.scale))
        gfxdraw.filled_trigon(screen, 5 * self.director.scale, 15 * self.director.scale, 20 * self.director.scale, 22 * self.director.scale, 20 * self.director.scale, 8 * self.director.scale, (232, 107, 35))
        gfxdraw.aatrigon(screen, 5 * self.director.scale, 15 * self.director.scale, 20 * self.director.scale, 22 * self.director.scale, 20 * self.director.scale, 8 * self.director.scale, (232, 107, 35))
