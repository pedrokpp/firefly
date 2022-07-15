from PPlay.sprite import Sprite
from PPlay.window import Window
from menus.menu import Menu
from state_manager import StateManager, State
from conquistas import Conquistas


class ConquistasMenu(Menu):
    
    def __init__(self, window: Window, state_manager: StateManager) -> None:
        super().__init__(window)
        self.state_manager = state_manager
        self.mouse_clicked = False
        
        self.title = Sprite('./assets/title.png')
        self.title.set_position(window.width / 2 - self.title.width / 2, 140)
        
        self.back_button = Sprite('./assets/buttons/sair.png')
        self.back_button.set_position(window.width / 2 - self.back_button.width / 2, 460)
        
        self.clouds = Sprite('./assets/background_inicial.png')
        self.clouds.y = window.height - self.clouds.height
    
    def render(self):
        window = self.window
        mouse = window.get_mouse()
        window.set_background_color([126, 194, 246])
        self.title.draw()
        self.clouds.draw()
        self.back_button.draw()
        window.draw_text(f"Seu maior score foi {Conquistas().get()}", size=24, color="black", font_name="./assets/fonts/Minecraft.ttf",
            file_path=True, centered=True, screen_height=window.height, screen_width=window.width, bold=True)
        
        if mouse.is_over_object(self.back_button) and mouse.is_button_pressed(mouse.BUTTON_LEFT) and not self.mouse_clicked or window.keyboard.key_pressed('esc'):
            self.state_manager.state = State.MENU
                    
        window.update()
    
