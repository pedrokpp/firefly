from time import time
from PPlay.sprite import Sprite
from PPlay.window import Window
from menus.menu import Menu
from state_manager import StateManager, State
from timer.timer import Timer

class MainMenu(Menu):
    
    def __init__(self, window: Window, state_manager: StateManager) -> None:
        super().__init__(window)
        self.state_manager = state_manager
        self.mouse_clicked = False
        
        self.frame = 1
        self.lumes = [Sprite(f'./assets/lume/lume-{frame}.png', 1) for frame in range(1, 4, 1)]
        for lume in self.lumes:
            lume.set_position(window.width / 2 - lume.width / 2, 280)
        
        self.title = Sprite('./assets/title.png')
        self.title.set_position(window.width / 2 - self.title.width / 2, 140)
        
        self.buttons = [('INICIAR', Sprite('./assets/buttons/iniciar.png')), ('SAIR', Sprite('./assets/buttons/sair.png')), 
                ('CONQUISTAS', Sprite('./assets/buttons/conquistas.png'))]
        for i, btn in enumerate(self.buttons):
            button = btn[1]
            button.set_position(window.width / 2 - button.width / 2, 430 + (i*button.height) + (i*30))
        
        self.clouds = Sprite('./assets/background_inicial.png')
        self.clouds.y = window.height - self.clouds.height
        
        self.timer = Timer()
    
    def render(self):
        super().render()
        window = self.window
        mouse = window.get_mouse()
        lume = self.lumes[self.frame]
        window.set_background_color([126, 194, 246])
        lume.draw()
        self.title.draw()
        self.clouds.draw()
        for btn in self.buttons:
            button = btn[1]
            button.draw()
        
        if self.timer.has_passed(200):
            self.frame = 0 if self.frame + 1 == len(self.lumes) else self.frame + 1
            self.mouse_clicked = False
            self.timer.reset_timer()
            
        
        if mouse.is_button_pressed(mouse.BUTTON_LEFT) and not self.mouse_clicked:
            for btn in self.buttons:
                if mouse.is_over_object(btn[1]):
                    if btn[0] == 'SAIR':
                        exit(0)
                    elif btn[0] == 'INICIAR':
                        self.state_manager.state = State.EM_JOGO
                    elif btn[0] == 'CONQUISTAS':
                        self.state_manager.state = State.CONQUISTAS
                    self.mouse_clicked = True
                    
        window.update()
    
