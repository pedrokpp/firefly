from random import randint
from time import time
from PPlay.sprite import Sprite
from PPlay.window import Window
from menus.menu import Menu
from state_manager import StateManager, State


class GameMenu(Menu):
    
    def __init__(self, window: Window, state_manager: StateManager) -> None:
        super().__init__(window)
        self.state_manager = state_manager
        self.mouse_clicked = False
        
        self.passive_speed = 1
        self.lume_speed = self.passive_speed * 4
        
        self.frame = 1
        self.lumes = [Sprite(f'./assets/lume/lume-{frame}.png', 1) for frame in range(1, 4, 1)]
        for lume in self.lumes:
            lume.set_position(window.width / 2 - lume.width / 2, 480)
        
        self.nuvens = [Sprite('./assets/nuvem.png', 1) for _ in range(36)]
        for nuvem in self.nuvens:
            nuvem.y = 0 - nuvem.height - randint(0, 900)
            nuvem.x = randint(-nuvem.width, window.width)
        
        self.lights = [Sprite('./assets/light.png', 1) for _ in range(4)]
        for light in self.lights:
            light.y = 0 - light.height - randint(0, 1000)
            light.x = randint(0, window.width - light.width)
        
        self.init_time = round(time() * 1000)
        self.last_time = self.init_time
        self.points = 0
        
        self.game_over = False
    
    def render(self):
        window = self.window
        kb = window.get_keyboard()
        curr_time = round(time() * 1000)
        lume = self.lumes[self.frame]
        window.set_background_color([126, 194, 246])
        
        if self.game_over:
            window.draw_text("Game Over!", size=36, color="black", font_name="./assets/fonts/Minecraft.ttf", file_path=True, 
                centered=True, screen_height=window.height, screen_width=window.width)
            window.update()
            
            if curr_time - self.last_time >= 4000:
                self.state_manager.state = State.MENU
                for l in self.lumes:
                    l.set_position(window.width / 2 - lume.width / 2, 480)
                self.game_over = False
                
            return
        
        if curr_time - self.init_time % 5000 == 0:
            self.passive_speed *= 1.1
            print("dificuldade aumentada")
        
        for nuvem in self.nuvens:
            nuvem.draw()
            nuvem.y += self.passive_speed + 1
            if nuvem.y >= window.height:
                nuvem.y = 0 - nuvem.height - randint(0, 30)
                nuvem.x = randint(0, window.width - nuvem.width)
        
        for light in self.lights:
            light.draw()
            light.y += self.passive_speed
            if light.y >= window.height:
                light.unhide()
                light.y = 0 - light.height - randint(0, 100)
                light.x = randint(0, window.width - light.width)   
            
        window.draw_text(str(self.points), size=48, color="black", font_name="./assets/fonts/Minecraft.ttf", file_path=True, 
                         centered=True, screen_height=window.height, screen_width=window.width)
        lume.draw()
        
        if curr_time - self.last_time > 200:
            self.frame = 0 if self.frame + 1 == len(self.lumes) else self.frame + 1
            self.last_time = curr_time
            self.mouse_clicked = False
            
        if kb.key_pressed("left"):
            if lume.x - self.lume_speed >= 0:
                for l in self.lumes:
                    l.move_x(-self.lume_speed)
        if kb.key_pressed("right"):
            if lume.x + lume.width + self.lume_speed <= window.width:
                for l in self.lumes:
                    l.move_x(self.lume_speed+self.passive_speed)
        if kb.key_pressed("up"):
            if lume.y + lume.height - 10 - self.lume_speed >= 0:
                for l in self.lumes:
                    l.move_y(-self.lume_speed)
        if kb.key_pressed("down"):
            if lume.y + lume.height + self.lume_speed <= window.height:
                for l in self.lumes:
                    l.move_y(self.lume_speed-self.passive_speed)
        
        if not kb.key_pressed("up"):   
            for l in self.lumes:
                l.move_y(self.passive_speed)
        
        if lume.y + lume.width - lume.height + 10 >= window.height:
            self.game_over = True
        
        for light in self.lights:
            if lume.collided(light) and light.drawable:
                self.points += 1
                light.hide()
        
        window.update()
    
