from window import Window
import pygame
from panel import Sprite
import game_pane

class GameOver(Window):
    def __init__(self, score, cs, project):
        super().__init__("Gameover")
        # self.textColor = (0, 0, 0)
        self.panelFont = pygame.font.SysFont('Arial', 15, bold=True)
        self.panelColor = (250, 0, 0)
        self.textColor = (255, 255, 255)

        self.doneProject = project
        self.customerSatisfaction = cs
        self.score = score

        self.playing_sfx = True
        self.gameover()

    def gameover(self):
        running = True
        music_playing = self.sound.get_music_status()
        while running:
            self.screen.fill((0, 0, 0))

            # setting background image
            background = pygame.image.load("images/menubackground.jpg")
            background = pygame.transform.scale(background, (900, 750))
            self.screen.blit(background, (0, 0))

            self.createReturnButton()
            quitButton = self.createGameButton(120, 700, 100, 25, 'QUIT', 150, 703)
            mouseX, mouseY = pygame.mouse.get_pos()

            # clicking on return button
            if self.returnButton.collidepoint((mouseX, mouseY)):
                if self.click:
                    running = False

            # clicking on quit
            if quitButton.collidepoint((mouseX, mouseY)):
                if self.click:
                    self.sound.play_ui_click(self.playing_sfx)
                    print("Quit\n")
                    exit()

            self.draw_text('Total Projects: ', self.font, (255, 255, 255), self.screen, 350, 210)
            self.draw_text(str(self.doneProject), self.font, (255, 255, 255), self.screen, 500, 210)
            self.draw_text('Satisfaction%: ', self.font, (255, 255, 255), self.screen, 350, 230)
            self.draw_text(str(self.customerSatisfaction), self.font, (255, 255, 255), self.screen, 500, 230)
            self.draw_text('Score: ', self.font, (255, 255, 255), self.screen, 350, 250)
            self.draw_text(str(self.score), self.font, (255, 255, 255), self.screen, 500, 250)

            self.draw_text('Better Scrum next time...', self.font, (255, 255, 255), self.screen, 325, 400)

            self.handle_click()
    def createGameButton(self, rectX, rectY, rectW, rectH, text, textX, textY):
        button = pygame.Rect(rectX, rectY, rectW, rectH)
        pygame.draw.rect(self.screen, self.panelColor, button)
        self.draw_text(text, self.panelFont, self.textColor, self.screen, textX, textY)
        return button