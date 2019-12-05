import pygame
from pygame import Rect

class Entity:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def rect(self):
        return Rect(self.x, self.y, self.width, self.height)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect())

def myround(x, base=5):
    return int(base * round(float(x)/base))
