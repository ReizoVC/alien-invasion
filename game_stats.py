class GameStats:
    """Seguimiento de estadísticas del juego Alien Invasion."""
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = True

    def reset_stats(self):
        """Inicializar estadísticas que pueden cambiar durante el juego."""
        self.ships_left = self.ai_settings.ship_limit
