from game.core import CollisionHandler
from ursina import *

class Item(Entity):
	def __init__(self):
		super().__init__(position=Vec3(0, 0, 0), ignore_paused=True)
		self.collision_handler = CollisionHandler()

	def input(self):
		pass

	def update(self):
		pass

	def handle_collision(self, other_entity):
		self.collision_handler.handle_collision(self, other_entity)
