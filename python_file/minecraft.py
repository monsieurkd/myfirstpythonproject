
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

grass_texture = load_texture('Downloads/grass.jpg')
stone_texture = load_texture('Downloads/stone.jpg')
brick_texture = load_texture('Downloads/brick.jpg')
dirt_texture = load_texture('Downloads/dirt.jpg')
block_pick = 1

def update():
    global block_pick
    if held_keys['1']: block_pick = 1
    if held_keys['2']: block_pick = 2
    if held_keys['3']: block_pick = 3
    if held_keys['4']: block_pick = 4
class Voxel(Button):
    def __init__(self, position = (0,0,0), texture = grass_texture):
        super().__init__(
            parent = scene,
            position= position,
            model = 'cube',
            origin_y = 0.5,
            
            Texture = texture,
            color = color.color(0,0,random.uniform(0.9,1)),
            highlight_color = color.lime)
    def input(self, key):
        if self.hovered:
            if key == 'left mouse down': 
                if key == '1': voxel = Voxel(position = self.position+ mouse.normal, texture = grass_texture)
                if key == '2': voxel = Voxel(position = self.position+ mouse.normal, texture = dirt_texture)
                if key == '3': voxel = Voxel(position = self.position+ mouse.normal, texture = stone_texture)
                if key == '4': voxel = Voxel(position = self.position+ mouse.normal, texture = brick_texture)
            if key == 'right mouse down':
                destroy(self)


#thứ tự rất quan trọng :v, không thể sử dụng biến rồi mới khai báo
for z in range(8):
    for x in range(8):
        voxel = Voxel(position= (x,0,z))

player = FirstPersonController()

app.run()