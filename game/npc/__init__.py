from game.core import CollisionHandler
from ursina import Entity

class NPC(Entity):
	def __init__(self):
		super().__init__()
		self.collision_handler = CollisionHandler()

	def input(self):
		pass

	def update(self):
		pass

	def handle_collision(self, other_entity):
		self.collision_handler.handle_collision(self, other_entity)
