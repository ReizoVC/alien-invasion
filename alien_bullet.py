import pygame
from pygame.sprite import Sprite

class AlienBullet(Sprite):
    """Clase para gestionar los disparos de los alienígenas."""
    def __init__(self, ai_settings, screen, alien):
        super().__init__()
        self.screen = screen
        
        # Crear un rectángulo para el proyectil en (0,0) y luego establecer su posición correcta
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = alien.rect.centerx
        self.rect.top = alien.rect.bottom
        
        # Almacenar la posición del proyectil como un valor decimal
        self.y = float(self.rect.y)
        
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.alien_bullet_speed_factor  # Usar una configuración específica para la velocidad de las balas de los alienígenas

    def update(self):
        """Mover el proyectil hacia abajo en la pantalla."""
        self.y += self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        """Dibujar el proyectil en la pantalla."""
        pygame.draw.rect(self.screen, self.color, self.rect)
