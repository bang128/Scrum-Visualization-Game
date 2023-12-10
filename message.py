import pygame
import sys
from sound_effects import SoundEffects
from pygame.locals import *


class Message():
    def __init__(self, screen, x, y, w, h):
        self.screen = screen
        self.xPos = x
        self.yPos = y

        self.panel = pygame.Rect(self.xPos, self.yPos, w, h)
        self.clock = pygame.time.Clock()
        self.textColor = (0, 0, 0)
        pygame.draw.rect(self.screen, (153, 204, 255), self.panel)

        # create close button
        self.closeButton = pygame.Rect(self.xPos + w - 90, self.yPos + h - 45, 70, 25)
        pygame.draw.rect(screen, (51, 153, 255), self.closeButton)
        font = pygame.font.SysFont('Arial', 15, bold=True)
        self.draw_text('Close', font, self.textColor, self.screen, self.xPos + w - 75, self.yPos + h - 42)

        self.click = False
        self.running = True
        self.sound = SoundEffects()
        self.playing_sfx = True

        self.salaryMessage = None

        # self.action(["This is a message.", "This is the second line."])

    def action(self, messages):
        while self.running:
            self.writeMessage(messages)
            self.handleCloseButton()
            self.handleClick()

            pygame.display.update()
            self.clock.tick(60)

    def draw_text(self, text, font, color, surface, x, y):
        textobj = font.render(text, True, color)
        textrectangle = textobj.get_rect()
        textrectangle.topleft = (x, y)
        surface.blit(textobj, textrectangle)

    def writeMessage(self, messages):
        if messages:
            i = 0
            font = pygame.font.SysFont('Arial', 20, bold=False)
            for m in messages:
                self.draw_text(m, font, self.textColor, self.screen, self.xPos + 50, self.yPos + 50 + 40 * i)
                i += 1

            if self.salaryMessage:
                self.draw_text("Current salary: $" + str(self.salaryMessage[0]), font, self.textColor, self.screen,
                               self.xPos + 50, self.yPos + 50 + 40 * i)
                i += 1
                if self.salaryMessage[1] != 0:
                    self.draw_text("New salary: $" + str(self.salaryMessage[1]), font, self.textColor, self.screen,
                                   self.xPos + 50, self.yPos + 50 + 40 * i)
                else: self.draw_text("Not enough money for upgrade", font, self.textColor, self.screen,
                                   self.xPos + 50, self.yPos + 50 + 40 * i)

    def handleCloseButton(self):
        mouseX, mouseY = pygame.mouse.get_pos()
        if self.closeButton.collidepoint((mouseX, mouseY)):
            if self.click:
                self.sound.play_ui_click(self.playing_sfx)
                print("Close")
                self.running = False

    def handleClick(self):
        self.click = False
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.click = True
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

    def set_sfx(self, isPlaying):
        self.playing_sfx = isPlaying

    def setSalaryMessage(self, salaryMessage):
        self.salaryMessage = salaryMessage
