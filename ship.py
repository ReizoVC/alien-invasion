# ship.py

import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """Clase para manejar la nave del jugador."""
    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        # Cargar la imagen de la nave y obtener su rectángulo
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # Colocar la nave en la parte inferior central de la pantalla
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        
        self.center = float(self.rect.centerx)
        
        
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Actualizar la posición de la nave según las flags de movimiento."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
    
    
        self.rect.centerx = self.center
    

    def blitme(self):
        """Dibujar la nave en su ubicación actual y su hitbox."""
        self.screen.blit(self.image, self.rect)
        pygame.draw.rect(self.screen, (0, 255, 0), self.rect, 2)  # Dibujar borde verde alrededor de la nave

    def center_ship(self):
        """Centrar la nave en la pantalla."""
        self.center = self.screen_rect.centerx