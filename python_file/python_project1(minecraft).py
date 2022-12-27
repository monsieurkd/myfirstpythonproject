
from multiprocessing import parent_process
from string import whitespace
from turtle import position

from ursina import *

class Test_cube(Entity):
    def __init__(self):
        super().__init__(
            model = 'cube',
            color = color.white,
            texture = 'white_cube',
            rotation = Vec3(45,50,45)
        )
    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                print('button press')

app = Ursina()

def update():
    if held_keys['a']:
       test_square.x -= 4* time.dt 

class Test_button(Button):
    def __init__(self):
        super().__init__(
            parent = scene,
            model= 'cube',
            Texture = 'brick',
            color = color.red,
            highlight_color = color.blue,
            pressed_color = color.lime
        )

test_square = Entity(model = 'quad', color = color.red, scale = (1,4), position = (5,4))
sans_texture = load_texture('Downloads/309858442_2105370599664232_4202633748572807029_n.png')
sans = Entity(model = 'quad', Texture =sans_texture,position = (5,3))

test_cube = Test_button()


#chua hoc xong ve class, object va self, super 
#18/10 đã học xong chắc là hiểu :D



app.run()
