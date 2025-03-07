import pygame

def update_screen(ai_settings, screen, ship, aliens, bullets, alien_bullets):
    """Actualizar las imágenes en la pantalla y cambiar a la nueva pantalla."""
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    for alien_bullet in alien_bullets.sprites():
        alien_bullet.draw_bullet()
    ship.blitme()
    for alien in aliens.sprites():
        alien.blitme()
    pygame.display.flip()
