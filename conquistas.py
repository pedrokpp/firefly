import os


class Conquistas:
    
    def __init__(self) -> None:
        pass
    
    def update(self, points):
        local = os.environ.get("APPDATA") + "\\FireFly\\" if os.name == "nt" else os.environ.get("HOME") + "/.firefly/"
        if not os.path.exists(local):
            os.makedirs(local)
        with open(local + "highscore.txt", "w") as f:
            f.write(str(points))
        return points

    def get(self) -> int:
        local = os.environ.get("APPDATA") + "\\FireFly\\" if os.name == "nt" else os.environ.get("HOME") + "/.firefly/"
        if not os.path.exists(local):
            return 0
        with open(local + "highscore.txt", "r") as f:
            return int(f.read())
