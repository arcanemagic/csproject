from pygame import *

class Scene:
    def __init__(self, director):
        self.director = director

    def on_update(self):
        raise NotImplementedError("on_update abstract method must be defined in subclass")

    def on_event(self, event):
        raise NotImplementedError("on_event abstract method must be defined in subclass")

    def on_draw(self, screen):
        raise NotImplementedError("on_Draw abstract method must be defined in subclass")
