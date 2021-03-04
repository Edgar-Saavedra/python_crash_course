import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
  """Overal class to manage game assets and behavior."""

  def __init__(self):
    """Init the game, and create resource"""
    pygame.init()
    self.settings = Settings()
    self.screen = pygame.display.set_mode(
      (self.settings.screen_width, self.settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")
    self.ship = Ship(self)

  def run_game(self):
    """Start the main loop for the game."""
    while True:
      # watch for keyboard mouse events
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()
      # set screen color background
      self.screen.fill(self.settings.bg_color)
      self.ship.blitme()
      # make the most recently drawn screen visible
      pygame.display.flip()


if __name__ == '__main__':
  # make game instance, run it
  ai = AlienInvasion()
  ai2 = AlienInvasion()
  ai.run_game()
  ai2.run_game()