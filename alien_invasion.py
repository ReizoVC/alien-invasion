import sys
import pygame
from settings import Settings
from models.ship import Ship
from models.bullet import Bullet
from models.alien import Alien
from controllers import game_functions as gf
from pygame.sprite import Group
from models.game_stats import GameStats
from views.screen import update_screen, load_background_image

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    stats = GameStats(ai_settings)

    ship = Ship(ai_settings, screen)
    
    bullets = Group()
    alien_bullets = Group()
    aliens = Group()

    gf.create_fleet(ai_settings, screen, aliens)
    
    background_image = load_background_image(ai_settings)
    
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, ship, aliens, bullets)
            gf.fire_alien_bullet(ai_settings, screen, aliens, alien_bullets)
            gf.update_alien_bullets(ai_settings, screen, stats, ship, aliens, alien_bullets)
        update_screen(ai_settings, screen, ship, aliens, bullets, alien_bullets, background_image)

run_game()