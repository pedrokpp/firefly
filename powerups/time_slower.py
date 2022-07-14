from powerups.powerup import Powerup


class TimeSlower(Powerup):

    def __init__(self):
        super().__init__('./assets/clock.png', 'time_slower', 5000)