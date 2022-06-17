from enum import Enum

class State(Enum):
    MENU = 0
    EM_JOGO = 1
    CONQUISTAS = 2

class StateManager():
    
    def __init__(self) -> None:
        self.state = State.MENU
        