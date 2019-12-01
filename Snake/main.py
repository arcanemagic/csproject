from Director import *
from Game import *

def main():
    dire = Director()
    twop = mainGame(dire)
    dire.change_scene(twop)
    dire.loop()

if __name__ == '__main__':
    pygame.init()
    main()
