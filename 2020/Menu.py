import sys
sys.path.insert(0, '../../')
import os
import pygame
import pygameMenu
import Stackie
import Snake

color_black = (0, 0, 0)
color_white = (255, 255, 255)
color_background = (17, 165, 240)
color_title = (29, 98, 194)
window_size = (800, 800)

surface = None

def snake():
    Snake.main()

def stackie():
    Stackie.running = True
    Stackie.main()

def main_background():
    global surface
    surface.fill((20, 20, 20))

def main():
    global surface
    pygame.init()
    surface = pygame.display.set_mode(window_size)
    pygame.display.set_caption('Project Gamezone')
    pygame.display.set_icon(pygame.image.load("images\gamezone.png"))

    #Define menu
    main_menu = pygameMenu.Menu(surface,
                                bgfun=main_background,
                                color_selected=color_white,
                                font="fonts/Norwester.otf",
                                font_color=color_black,
                                font_size=30,
                                font_size_title=40,
                                menu_alpha=100,
                                menu_color=color_background,
                                menu_color_title=color_title,
                                menu_height=int(window_size[1] * 0.7),
                                menu_width=int(window_size[0] * 0.8),
                                # User press ESC button
                                onclose=pygameMenu.events.EXIT,
                                option_shadow=False,
                                title='Main menu',
                                window_height=window_size[1],
                                window_width=window_size[0]
                                )
    main_menu.set_fps(60)
    main_menu.add_option('Snake', snake)
    main_menu.add_option('Stack1e', stackie)
    main_menu.add_option('Quit', pygameMenu.events.EXIT)

    #Main loop
    while True:
        main_background()
        main_menu.mainloop()
        pygame.display.flip()


if __name__ == '__main__':
    main()
