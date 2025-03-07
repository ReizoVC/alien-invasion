import pygame

def load_background_image(ai_settings):
    """Cargar la imagen de fondo."""
    return pygame.image.load('images/background.png')

def update_screen(ai_settings, screen, ship, aliens, bullets, alien_bullets, background_image):
    """Actualizar las imágenes en la pantalla y cambiar a la nueva pantalla."""
    for y in range(0, ai_settings.screen_height, background_image.get_height()):
        for x in range(0, ai_settings.screen_width, background_image.get_width()):
            screen.blit(background_image, (x, y))
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    for alien_bullet in alien_bullets.sprites():
        alien_bullet.draw_bullet()
    ship.blitme()
    for alien in aliens.sprites():
        alien.blitme()
    pygame.display.flip()
