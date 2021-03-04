class Ship:
  """A class to manage the ship."""

  def __init__(self, ai_game):
    """Init the ship and set it starting position"""
    self.screen = ai_game.screen
    self.screen_rect = ai_game.screen.get_rect()

    # Load the ship image and get its rect (size)
    self.image = pygame.image.load('images/ship.bmp')
    self.rect = self.image.get_rect()
  
  def blitme(self):
    """Draw the ship at its current location"""
    self.screen.blit(self.image, self.rect)