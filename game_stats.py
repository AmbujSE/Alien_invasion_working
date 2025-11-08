class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
        # Load the high score from file or set to 0 if no file exists
        try:
            with open('highscore.txt', 'r') as f:
                self.high_score = int(f.read().strip())
        except:
            # High score should never be reset, but defaults to 0 if no saved score
            self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0 
        self.level = 1
    
    