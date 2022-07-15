from PPlay.sprite import Sprite
from time import time


class Powerup:

    def __init__(self, path, name, duration_ms):
        self.name = name
        self.sprite = Sprite(path)
        self.duration_ms = duration_ms
        self.init_time = round(time() * 1000)
        self.active = False
        self.init_time_timer = round(time() * 1000)

    def has_ended(self):
        return round(time() * 1000) - self.init_time >= self.duration_ms

    def activate(self):
        self.active = True
        self.init_time = round(time() * 1000)
    
    def deactivate(self):
        self.active = False
    
    def has_time_passed(self, ms):
        return round(time() * 1000) - self.init_time_timer >= ms
    
    def reset_timer(self):
        self.init_time_timer = round(time() * 1000)
    