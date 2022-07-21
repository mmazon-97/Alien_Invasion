class Settings: 
    """A class to store all settings for Alien Invasion"""

    def __init__(self): 
        """Initizlize game settings """
        #Screen settings 
        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_color = (0, 0, 0)

        #Bullet settings
        self.bullet_speed = 3.0
        self.bullet_width = 3 
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60) 
