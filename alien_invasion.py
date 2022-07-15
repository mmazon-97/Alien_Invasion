import sys

import pygame

class AlienInvasion:
    """ Overall class to manage game assests and behavior."""

    def __init__(self):
        """ Intialize game."""
        pygame.init()

        self.screen = pygame.display.set_mode(1920, 1080)
        pygame.display.set_caption("Alien Invasion")

        # Set background color 
        self.bg_color = (230, 240, 245)

    def run_game(self):
        """ Run game."""
        while True: 
            # Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through of the loop
            self.screen.fill(self.bg_color)
            
            # Make the most recently drawn screen visible: 
            pygame.display.flip()

if __name__ == '__main__':
    """ Make a game instance, and run the game."""
    ai = AlienInvasion()
    ai.run_game()