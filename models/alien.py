import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Clase que representa un alienígena en la flota."""
    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        self.x = float(self.rect.x)

    def check_edges(self):
        """Devolver True si el alien está en el borde de la pantalla."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Mover el alien a la derecha o a la izquierda."""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def blitme(self):
        """Dibujar el alien en su posición actual y su hitbox."""
        self.screen.blit(self.image, self.rect)

