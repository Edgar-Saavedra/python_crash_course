import sys
import pygame

class AlienInvasion:
  """Overal class to manage game assets and behavior."""

  def __init__(self):
    """Init the game, and create resource"""
    pygame.init()
    self.screen = pygame.display.set_mode( (1200, 800) )
    pygame.display.set_caption("Alien Invasion")

  def run_game(self):
    """Start the main loop for the game."""
    while True:
      # watch for keyboard mouse events
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()
      # make the most recently drawn screen visible
      pygame.display.flip()


if __name__ == '__main__':
  # make game instance, run it
  ai = AlienInvasion()
  ai.run_game()