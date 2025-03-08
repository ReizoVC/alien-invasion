import pygame
from pygame.sprite import Sprite

class AlienBullet(Sprite):
    """Clase para gestionar los disparos de los alienígenas."""
    def __init__(self, ai_settings, screen, alien):
        super().__init__()
        self.screen = screen
        
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = alien.rect.centerx
        self.rect.top = alien.rect.bottom
        
        self.y = float(self.rect.y)
        
        self.color = ai_settings.balaAlien
        self.speed_factor = ai_settings.alien_bullet_speed_factor

    def update(self):
        """Mover el proyectil hacia abajo en la pantalla."""
        self.y += self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        """Dibujar el proyectil en la pantalla."""
        pygame.draw.rect(self.screen, self.color, self.rect)
