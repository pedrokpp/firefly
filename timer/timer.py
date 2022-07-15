from time import time


class Timer:
    
    def __init__(self) -> None:
        self.init_time = round(time() * 1000)
    
    def has_passed(self, ms):
        return round(time() * 1000) - self.init_time >= ms
    
    def reset_timer(self):
        self.init_time = round(time() * 1000)
    