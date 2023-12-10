import pygame

class Sprite(pygame.sprite.Sprite):
    def __init__(self, text, screen, posX, posY):
        super().__init__()

        self.color = (255, 255, 255)
        self.font = pygame.font.SysFont('Arial', 15)
        self.screen = screen

        self.image = self.font.render(text, True, self.color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (posX, posY)
        self.screen.blit(self.image, self.rect)















