from PPlay.window import Window
from PPlay.sound import Sound

class Menu():
    
    def __init__(self, window: Window) -> None:
        self.window = window
        self.main_song = Sound('./sounds/main_song.wav')
        self.main_song.set_repeat(True)
        self.main_song.set_volume(5)
        
    def render(self):
        if not self.main_song.is_playing():
            self.main_song.play()
    
        