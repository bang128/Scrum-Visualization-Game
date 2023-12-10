from window import Window
import main_menu
import pygame

class Setting(Window):
    def __init__(self):
        super().__init__("Options")
        self.textColor = (0, 0, 0)
        self.music_playing = self.sound.get_music_status()
        self.sfx_playing = True
        # self.options()

    def options(self):
        running = True
        while running:
            self.screen.fill((0, 0, 0))
            mouseX, mouseY = pygame.mouse.get_pos()

            # setting background image
            self.setup_background()

            self.createReturnButton()

            # setting unmute and mute images
            unmute = pygame.image.load("images/unmute.png")
            unmute = pygame.transform.scale(unmute, (50,50))
            mute = pygame.image.load("images/mute.png")
            mute = pygame.transform.scale(mute, (50,50))

            musicButton = pygame.Rect(490, 200, 50, 50)
            sfxButton = pygame.Rect(490, 300, 50, 50)

            pygame.draw.rect(self.screen, (255, 253, 208), musicButton)
            pygame.draw.rect(self.screen, (255, 253, 208), sfxButton)

            if self.music_playing:
                self.screen.blit(unmute, (490, 200))
            else:
                self.screen.blit(mute, (490, 200))

            if self.sfx_playing:
                self.screen.blit(unmute, (490, 300))
            else:
                self.screen.blit(mute, (490, 300))

            # clicking on music button
            if musicButton.collidepoint((mouseX, mouseY)):
                if self.click:
                    self.sound.play_ui_click(self.sfx_playing)
                    if self.music_playing:
                        self.sound.pause_music()
                        self.music_playing = False
                    else:
                        self.sound.unpause_music()
                        self.music_playing = True

            # clicking on sfx button
            if sfxButton.collidepoint((mouseX, mouseY)):
                if self.click:
                    self.sound.play_ui_click(self.sfx_playing)
                    if self.sfx_playing:
                        self.sfx_playing = False
                    else:
                        self.sfx_playing = True

            # clicking on return button
            if self.returnButton.collidepoint((mouseX, mouseY)):
                if self.click:
                    self.sound.play_ui_click(self.sfx_playing)
                    running = False

            self.setup_text()
            self.handle_click()

    def setup_background(self):
        background = pygame.image.load("images/menubackground.jpg")
        background = pygame.transform.scale(background, (900, 750))
        self.screen.blit(background, (0, 0))

    def setup_text(self):
        self.draw_text('Setting', self.font, self.textColor, self.screen, 400, 20)
        self.draw_text('Music', self.font, self.textColor, self.screen, 405, 210)
        self.draw_text('SFX', self.font, self.textColor, self.screen, 405, 310)

    def get_sfx(self):
        return self.sfx_playing

    def set_sfx(self, isPlaying):
        self.sfx_playing = isPlaying
