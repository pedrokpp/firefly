from PPlay.window import Window
from PPlay.gameimage import GameImage
from PPlay.sprite import Sprite
from random import randint
from menus.main_menu import MainMenu
from state_manager import StateManager, State

WIDTH = 300 # em pixels
HEIGHT = 800 # em pixels

window = Window(WIDTH, HEIGHT)
window.set_title('Firefly')

state_manager = StateManager()
menu_inicial = MainMenu(window, state_manager)

while True:
    
    if state_manager.state == State.EM_JOGO:
        pass
    elif state_manager.state == State.CONQUISTAS:
        pass
    elif state_manager.state == State.MENU:
        menu_inicial.render()
    else:
        pass # panic
    
    window.delay(16) # delay de 16ms para deixar o fps estático em 60 FPS (1 frame a cada 16ms = 60 FPS)
