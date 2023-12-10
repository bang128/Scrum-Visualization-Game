import pygame
import sys
from sound_effects import SoundEffects
from pygame.locals import *

class Window():
    def __init__(self, caption):
        pygame.init()
        pygame.display.set_caption(caption)
        self.screen = pygame.display.set_mode((900, 750), 0, 32)
        self.screen.fill((0, 0, 0))
        self.font = pygame.font.SysFont('Arial', 25, bold=True)
        self.clock = pygame.time.Clock()
        self.click = False
        self.sound = SoundEffects()
        self.returnButton = pygame.Rect(10, 700, 100, 25)
        self.caption=caption

    def draw_text(self, text, font, color, surface, x, y):
        textobj = font.render(text, True, color)
        textrectangle = textobj.get_rect()
        textrectangle.topleft = (x, y)
        surface.blit(textobj, textrectangle)

    def handle_click(self):
        self.click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.click = True

        pygame.display.update()
        self.clock.tick(10)

    def createReturnButton(self):
        font = pygame.font.SysFont('Arial', 15, bold=True)
        pygame.draw.rect(self.screen, (250, 0, 0), self.returnButton)
        self.draw_text('RETURN', font, (255, 255, 255), self.screen, 27, 703)

    def getCaption(self):
        return self.caption