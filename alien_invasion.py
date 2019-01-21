import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
from bullet import Bullet

def run_game():
    pygame.init()
    ai_settings=Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("MyGame")
    ship=Ship(ai_settings,screen)
    #Make a group to store bullets in.
    bullets=Group()
    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings,screen,ship,bullets)

run_game()
