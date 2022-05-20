from PPlay.window import Window
from PPlay.gameimage import GameImage
from PPlay.sprite import Sprite
from random import randint

WIDTH = 300 # em pixels
HEIGHT = 800 # em pixels

pontos = 0

window = Window(WIDTH, HEIGHT)
window.set_title('Firefly')
keyboard = window.get_keyboard()

background1 = GameImage('./assets/background_inicial.png')
background1.y = (HEIGHT - background1.height) + 30

lume = Sprite('./assets/lume-static.png', frames=1)
lume.x = (WIDTH / 2 - lume.width / 2)
lume.y = background1.y

bird1 = Sprite('./assets/bird1.png', frames=1)
bird1.x = randint(0, WIDTH - bird1.width)
bird1.y = randint(60, 300)

hearts = GameImage('./assets/hearts/hearts.png')

while True: # game loop
    window.set_background_color([136, 194, 246])
    background1.draw()
    window.draw_text(f'{pontos}', 0, 0, size=54 ,font_name='./assets/fonts/Minecraft.ttf', file_path=True, centered=True, screen_width=WIDTH, screen_height=HEIGHT)
    lume.draw()
    hearts.draw()
    bird1.draw()
    window.update()
    window.delay(16) # delay de 16ms para deixar o fps estático em 60 FPS (1 frame a cada 16ms = 60 FPS)
