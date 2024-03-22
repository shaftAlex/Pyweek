from ursina import *
from game.level import Level

class DevLevel(Level):
	def __init__(self):
		super().__init__()

		self.sun = DirectionalLight()
		self.sun.look_at(Vec3(1, -1, -1))
		self.sky = Sky(texture='skybox')
		self.ground = Entity(model='plane', collider='box', scale=128, texture='default', texture_scale=(32, 32))
