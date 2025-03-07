# settings.py

class Settings:
    """Clase para almacenar todas las configuraciones del juego."""
    def __init__(self):
        # Configuración de la pantalla
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.background_image_path = 'images/background.png'

        # Configuración de la nave
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # Configuración de los disparos
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 255, 0)
        self.bullets_allowed = 3

        # Configuración de los alienígenas
        self.alien_speed_factor = 0.1  # Reducir la velocidad de los alienígenas
        self.fleet_drop_speed = 10
        self.fleet_direction = 1  # 1 es derecha, -1 es izquierda
        self.speedup_scale = 1.2  # Factor de incremento exponencial de la velocidad
        self.alien_bullet_speed_factor = 1  # Velocidad de las balas de los alienígenas

    def increase_speed(self):
        """Aumentar la velocidad de los alienígenas."""
        self.alien_speed_factor *= self.speedup_scale