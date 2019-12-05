from Director import *
from Game import *

def main():
    dire = Director()
    twop = mainGame(dire)
    dire.change_scene(twop)
    dire.loop()

pygame.init()

if __name__ == '__main__':
    main()
