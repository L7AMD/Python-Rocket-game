import pygame

class Ship():
    def __init__(self,ai_settings,screen):
        """Initialize the ship and set its starting position."""
        self.screen=screen
        self.ai_settings=ai_settings
        # Load the ship image and get its rect.
        self.image = pygame.image.load("images/ship.bmp")
        self.rect=self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value of the ship's center, to update ship's centre value not the rec
        self.center=float(self.rect.centerx)

        # Movement flags
        self.moving_right , self.moving_left = False,False

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image,self.rect)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right :
            self.center += self.ai_settings.speed_ship_factor
        if self.moving_left and self.rect.left > 0 :
            self.center -= self.ai_settings.speed_ship_factor

        self.rect.centerx = self.center
