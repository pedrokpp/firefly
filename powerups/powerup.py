from PPlay.sprite import Sprite
from timer.timer import Timer


class Powerup:

    def __init__(self, path, name, duration_ms):
        self.name = name
        self.sprite = Sprite(path)
        self.duration_ms = duration_ms
        self.duration_timer = Timer()
        self.cooldown_timer = Timer()
        self.active = False

    def has_ended(self):
        return self.duration_timer.has_passed(self.duration_ms)

    def activate(self):
        self.active = True
        self.duration_timer.reset_timer()
    
    def deactivate(self):
        self.active = False
    
    def has_time_passed(self, ms):
        return self.cooldown_timer.has_passed(ms)
    
    def reset_timer(self):
        self.cooldown_timer.reset_timer()
    