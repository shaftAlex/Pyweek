from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import globals as g

class Player(FirstPersonController):

	def __init__(self, position: Vec3):
		super().__init__(position=position, jump_height=2.5, jump_duration=0.4, origin_y=-0.5, collider='box')

		self.speed = 7

		self.collider = BoxCollider(self, center=Vec3(0, 1.25, 0), size=Vec3(1, 2.5, 1.25))

		return

	def update(self):
		super().update()
		return

	def input(self, key):
		if key == 'left mouse down':
			print('left click')
		if key == 'right mouse down':
			print('right click')
		super().input(key)
		return
