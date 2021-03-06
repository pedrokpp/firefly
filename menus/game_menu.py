from random import randint
from time import time
from PPlay.sprite import Sprite
from PPlay.window import Window
from PPlay.sound import Sound
from menus.menu import Menu
from state_manager import StateManager, State
from powerups.time_slower import TimeSlower
from timer.timer import Timer
from conquistas import Conquistas


class GameMenu(Menu):

    def __init__(self, window: Window, state_manager: StateManager) -> None:
        super().__init__(window)
        self.state_manager = state_manager
        self.mouse_clicked = False

        self.passive_speed = 1
        self.lume_speed = self.passive_speed * 4

        self.kb_mode = True

        self.frame = 1
        self.lume_timer = Timer()
        self.lumes = [Sprite(f'./assets/lume/lume-{frame}.png', 1) for frame in range(1, 4, 1)]
        for lume in self.lumes:
            lume.set_position(window.width / 2 - lume.width / 2, 480)

        self.nuvens = [Sprite('./assets/nuvem.png', 1) for _ in range(36)]
        for nuvem in self.nuvens:
            nuvem.y = 0 - nuvem.height - randint(0, 900)
            nuvem.x = randint(-nuvem.width, window.width)

        self.pickup_coin_sound = Sound('./sounds/pickup_coin.wav')
        self.lights = [Sprite('./assets/light.png', 1) for _ in range(4)]
        for light in self.lights:
            light.y = 0 - light.height - randint(0, 1000)
            light.x = randint(0, window.width - light.width)

        self.hurt_sound = Sound('./sounds/hurt.wav')
        self.heal_sound = Sound('./sounds/heal.wav')
        self.hearts = [Sprite('./assets/heart.png', 1) for _ in range(2)]
        for heart in self.hearts:
            heart.y = 0 - heart.height - randint(0, 2000)
            heart.x = randint(0, window.width - heart.width)

        self.empty_hps = [Sprite('./assets/empty_hp.png', 1) for _ in range(10)]
        self.full_hps = [Sprite('./assets/full_hp.png', 1) for _ in range(10)]
        for i, ehp in enumerate(self.empty_hps):
            fhp = self.full_hps[i]
            ehp.y = window.height - 30
            fhp.y = window.height - 30
            ehp.x = self.empty_hps[i - 1].x + ehp.width if i != 0 else 5
            fhp.x = self.full_hps[i - 1].x + fhp.width if i != 0 else 5

        self.powerup_sound = Sound('./sounds/powerup.wav')
        self.powerups = [TimeSlower()]
        for powerup in self.powerups:
            powerup.sprite.y = 0 - powerup.sprite.height - 90
            powerup.sprite.hide()

        self.game_over_sound = Sound('./sounds/game_over.wav')
        self.sound_flag = True

        self.main_timer = Timer()
        self.kb_timer = Timer()
        self.points = 0
        self.health_points = 10
        self.passive_speed = 1
        self.game_over = False
        self.powerup_flag = False

    def render(self):
        super().render()
        window = self.window
        kb = window.get_keyboard()
        mouse = window.get_mouse()
        curr_time = round(time() * 1000)
        lume = self.lumes[self.frame]
        window.set_background_color([126, 194, 246])

        if self.game_over or self.health_points == 0:
            window.draw_text("Game Over!", size=36, color="black", font_name="./assets/fonts/Minecraft.ttf",
                             file_path=True,
                             centered=True, screen_height=window.height, screen_width=window.width)
            window.update()

            if self.sound_flag:
                self.game_over_sound.play()
                self.sound_flag = False
            
            conquistas = Conquistas()
            highest_score = conquistas.get()
            if self.points > highest_score:
                conquistas.update(self.points)
            
            if self.main_timer.has_passed(4000):
                self.state_manager.state = State.MENU
                for l in self.lumes:
                    l.set_position(window.width / 2 - lume.width / 2, 480)
                self.game_over = False
                self.health_points = 10
                self.passive_speed = 1
                self.points = 0
                for light in self.lights:
                    light.hide()
                for heart in self.hearts:
                    heart.hide()
                for powerup in self.powerups:
                    powerup.sprite.hide()
                for nuvem in self.nuvens:
                    nuvem.y = 0 - nuvem.height - randint(0, 900)
                    nuvem.x = randint(-nuvem.width, window.width)
                self.sound_flag = True
            return

        if self.main_timer.has_passed(3000):
            self.passive_speed = round(1.08 * self.passive_speed, 2)
            if self.passive_speed >= 20:
                self.passive_speed = 20
            self.main_timer.reset_timer()

        for nuvem in self.nuvens:
            nuvem.draw()
            nuvem.y += self.passive_speed + 1
            if nuvem.y >= window.height:
                nuvem.y = 0 - nuvem.height - randint(0, 30)
                nuvem.x = randint(0, window.width - nuvem.width)

        for light in self.lights:
            light.draw()
            if lume.collided(light) and light.drawable:
                self.points += 1
                light.hide()
                self.pickup_coin_sound.play()
            light.y += self.passive_speed
            if light.y >= window.height:
                if light.drawable:
                    self.health_points -= 1
                    self.hurt_sound.play()
                light.unhide()
                light.y = 0 - light.height - randint(0, 500)
                light.x = randint(0, window.width - light.width)

        for heart in self.hearts:
            heart.draw()
            if lume.collided(heart) and heart.drawable:
                self.health_points += 1 if self.health_points < 10 else 0
                heart.hide()
                self.heal_sound.play()
            if self.health_points < 10:
                heart.y += self.passive_speed * 0.8
            elif heart.y > 0:
                heart.y += self.passive_speed * 0.8
            if heart.y >= window.height:
                heart.unhide()
                heart.y = 0 - heart.height - randint(200, 900)
                heart.x = randint(0, window.width - heart.width)

        window.draw_text(str(self.points), size=48, color="black", font_name="./assets/fonts/Minecraft.ttf",
                         file_path=True,
                         centered=True, screen_height=window.height, screen_width=window.width)
        
        lume.draw()

        for powerup in self.powerups:
            powerup.sprite.draw()
            if powerup.sprite.y == 0 - powerup.sprite.height - 90:
                if self.passive_speed >= 4 and randint(0, 100) <= 1 and powerup.has_time_passed(100_000):
                    powerup.sprite.y += self.passive_speed * 0.9
                    powerup.sprite.x = randint(0, window.width - powerup.sprite.width)
                    powerup.sprite.unhide()
                    powerup.reset_timer()
            else:
                powerup.sprite.y += self.passive_speed * 0.9
                if powerup.active:
                    if not self.powerup_flag:
                        self.passive_speed = round(0.5 * self.passive_speed, 2)
                        self.powerup_sound.play()
                        self.powerup_flag = True
                    if powerup.has_ended():
                        powerup.deactivate()
                        self.passive_speed = round(2 * self.passive_speed, 2)
                        powerup.sprite.y = 0 - powerup.sprite.height - 90
                        self.powerup_flag = False
                elif lume.collided(powerup.sprite) and powerup.sprite.drawable:
                    powerup.activate()
                    powerup.sprite.hide()


        for i, ehp in enumerate(self.empty_hps):
            ehp.draw()
            if i <= self.health_points - 1:
                fhp = self.full_hps[i]
                fhp.draw()

        if self.lume_timer.has_passed(200):
            self.frame = 0 if self.frame + 1 == len(self.lumes) else self.frame + 1
            self.last_time = curr_time
            self.mouse_clicked = False
            self.lume_timer.reset_timer()

        if kb.key_pressed("space") and self.kb_timer.has_passed(100):
            self.kb_mode = not self.kb_mode
            self.kb_timer.reset_timer()

        if self.kb_mode:
            if kb.key_pressed("left"):
                if lume.x - self.lume_speed >= 0:
                    for l in self.lumes:
                        l.move_x(-self.lume_speed)
            if kb.key_pressed("right"):
                if lume.x + lume.width + self.lume_speed <= window.width:
                    for l in self.lumes:
                        l.move_x(self.lume_speed + self.passive_speed)
            if kb.key_pressed("up"):
                if lume.y + lume.height - 10 - self.lume_speed >= 0:
                    for l in self.lumes:
                        l.move_y(-self.lume_speed)
            if kb.key_pressed("down"):
                if lume.y + lume.height + self.lume_speed <= window.height:
                    for l in self.lumes:
                        l.move_y(self.lume_speed - self.passive_speed)
            if not kb.key_pressed("up"):
                for l in self.lumes:
                    l.move_y(self.passive_speed)
        else:
            x, y = mouse.get_position()
            x -= lume.width / 2
            y -= lume.height / 2
            for l in self.lumes:
                l.set_position(x, y)

        if lume.y + lume.width - lume.height + 10 >= window.height:
            self.game_over = True

        window.update()
