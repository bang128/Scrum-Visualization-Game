from pygame import mixer

class SoundEffects:
    def __init__(self):
        mixer.init()
        self.click = mixer.Sound("sounds/ui_click.mp3")
        self.click.set_volume(0.3)

    def play_music(self):
        mixer.music.load("sounds/menumusic.mp3")
        mixer.music.play(-1)

    def change_volume(self, vol):
        mixer.music.set_volume(vol)

    def pause_music(self):
        mixer.music.pause()

    def unpause_music(self):
        mixer.music.unpause()

    def get_music_status(self):
        return mixer.music.get_busy()

    def play_ui_click(self, playing_sfx):
        if playing_sfx:
            self.click.play()

    def change_sfx_volume(self, vol):
        mixer.music.set_volume(vol)