import pygame

from window import Window
from game_pane import Game
from setting import Setting
from tutorial_pane import Tutorial
import unittest
from UnitTest import Test

class Menu(Window, unittest.TestCase):
    def __init__(self, music_played):
        super().__init__("Menu")
        self.panelFont = pygame.font.SysFont('Arial', 50, bold=True)
        self.music_played = music_played
        self.playing_sfx = True
        self.menu()
        # screen = pygame.display.set_mode()

    def menu(self):
        #unit_test=Test()
        if not self.music_played: # potentially may not need the if statement
            self.sound.play_music()
            self.sound.change_volume(0.5)
            self.music_played = True
        while True:
            self.screen.fill((0, 0, 0))
            background = pygame.image.load("images/menubackground.jpg")
            background = pygame.transform.scale(background, (900, 750))
            self.screen.blit(background, (0, 0))
            self.draw_text('Scrum Simulator', self.panelFont, (0, 0, 0), self.screen, 248, 55)

            mouseX, mouseY = pygame.mouse.get_pos()

            playButton = pygame.Rect(340, 200, 200, 50)
            tutorialButton = pygame.Rect(340, 300, 200, 50)
            settingButton = pygame.Rect(340, 400, 200, 50)
            quitButton = pygame.Rect(340, 500, 200, 50)

            # drawing to screen
            pygame.draw.rect(self.screen, (71, 44, 76), playButton)
            pygame.draw.rect(self.screen, (71, 44, 76), tutorialButton)
            pygame.draw.rect(self.screen, (71, 44, 76), settingButton)
            pygame.draw.rect(self.screen, (71, 44, 76), quitButton)

            # clicking on game
            if playButton.collidepoint((mouseX, mouseY)):
                pygame.draw.rect(self.screen, (59,180,222), playButton)
                if self.click:
                    # self.test_click()
                    self.sound.play_ui_click(self.playing_sfx)
                    game_pane = Game()
                    game_pane.set_sfx(self.playing_sfx)
                    game_pane.game()

            # clicking on tutorial button
            if tutorialButton.collidepoint((mouseX, mouseY)):
                pygame.draw.rect(self.screen, (59,180,222), tutorialButton)
                if self.click:
                    self.sound.play_ui_click(self.playing_sfx)
                    tutorial_pane = Tutorial()
                    tutorial_pane.set_sfx(self.playing_sfx)
                    tutorial_pane.tutorial()

            # clicking on options
            if settingButton.collidepoint((mouseX, mouseY)):
                pygame.draw.rect(self.screen, (59,180,222), settingButton)
                if self.click:
                    self.sound.play_ui_click(self.playing_sfx)
                    settings_pane = Setting()
                    settings_pane.set_sfx(self.playing_sfx)
                    settings_pane.options()
                    self.playing_sfx = settings_pane.get_sfx()
                    print(self.playing_sfx)

            # clicking on quit
            if quitButton.collidepoint((mouseX, mouseY)):
                pygame.draw.rect(self.screen, (59,180,222), quitButton)
                if self.click:
                    self.sound.play_ui_click(self.playing_sfx)
                    exit()

            self.draw_text('PLAY', self.font, (239, 219,203), self.screen, 405, 210)
            self.draw_text('TUTORIAL', self.font, (239, 219,203), self.screen, 382, 310)
            self.draw_text('SETTING', self.font, (239, 219,203), self.screen, 388, 410)
            self.draw_text('QUIT', self.font, (239, 219 ,203), self.screen, 405, 510)

            self.handle_click()



