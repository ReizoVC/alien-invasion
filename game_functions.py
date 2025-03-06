# game_functions.py

import sys
import pygame
import random
from bullet import Bullet
from alien import Alien
from alien_bullet import AlienBullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Responder a pulsaciones de teclas."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, ship):
    """Responder a liberaciones de teclas."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    """Responder a eventos de teclas y ratón."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

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

def update_bullets(ai_settings, screen, ship, aliens, bullets):
    """Actualizar la posición de los proyectiles y eliminar los que han desaparecido."""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)

def fire_bullet(ai_settings, screen, ship, bullets):
    """Disparar un proyectil si no se ha alcanzado el límite."""
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def fire_alien_bullet(ai_settings, screen, aliens, alien_bullets):
    """Disparar un proyectil desde un alienígena aleatorio."""
    if len(alien_bullets) < 1 and len(aliens) > 0:
        alien = random.choice(aliens.sprites())
        new_bullet = AlienBullet(ai_settings, screen, alien)
        alien_bullets.add(new_bullet)

def update_alien_bullets(ai_settings, screen, stats, ship, aliens, alien_bullets):
    """Actualizar la posición de los proyectiles de los alienígenas y eliminar los que han desaparecido."""
    alien_bullets.update()
    for bullet in alien_bullets.copy():
        if bullet.rect.top >= ai_settings.screen_height:
            alien_bullets.remove(bullet)
    check_alien_bullet_ship_collisions(ai_settings, screen, stats, ship, aliens, alien_bullets)

def check_alien_bullet_ship_collisions(ai_settings, screen, stats, ship, aliens, alien_bullets):
    """Responder a colisiones entre balas de alienígenas y la nave."""
    if pygame.sprite.spritecollideany(ship, alien_bullets):
        ship_hit(ai_settings, screen, stats, ship, aliens, alien_bullets)

def create_fleet(ai_settings, screen, aliens):
    """Crear una flota de alienígenas."""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    number_aliens_x = 10 
    number_rows = 3

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Crear un alien y colocarlo en la fila correcta."""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    if row_number % 2 == 0:
        alien.x = alien_width + (alien_width + 35) * alien_number  # Primera fila
    else:
        alien.x = alien_width + (alien_width + 35) * alien_number + (alien_width // 2)  # Filas desplazadas
    alien.rect.x = alien.x
    alien.rect.y = alien_height + (alien_height + 35) * row_number  # Separación de 35px entre filas
    aliens.add(alien)

def check_fleet_edges(ai_settings, aliens):
    """Responder apropiadamente si algún alien ha alcanzado un borde."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """Bajar toda la flota y cambiar la dirección."""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
    """Responder a colisiones entre balas y alienígenas."""
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
        bullets.empty()
        ai_settings.incease_speed()
        create_fleet(ai_settings, screen, aliens)

def ship_hit(ai_settings, screen, stats, ship, aliens, bullets):
    """Responder al impacto de un alienígena en la nave."""
    if stats.ships_left > 0:
        stats.ships_left -= 1
        aliens.empty()
        bullets.empty()
        create_fleet(ai_settings, screen, aliens)
        ship.center_ship()
        pygame.time.wait(500)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings, screen, stats, ship, aliens, bullets):
    """Verificar si algún alienígena ha llegado al fondo de la pantalla."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, screen, stats, ship, aliens, bullets)
            break

def update_aliens(ai_settings, screen, stats, ship, aliens, bullets):
    """Actualizar la posición de los alienígenas."""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, stats, ship, aliens, bullets)
    check_aliens_bottom(ai_settings, screen, stats, ship, aliens, bullets)