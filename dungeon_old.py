from ursina import *

class Node:
	def __init__(self, active: bool, form: str, position: (float, float, float), rotation: (float, float)):
		self.active = active
		self.form = form  # Options: s, m, l
		self.position = Vec3(position[0], position[1], position[2])
		self.rotation = Vec2(rotation[0], rotation[1])

class Tube:
	def __init__(self, model: str, texture: str, nodes: [Node]):
		self.model: str = model
		self.texture: str = texture
		self.nodes = nodes

class Segments:
	def __init__(self):

		self.array = []

		self.pipe_straight = Tube(model='pipe_straight', texture='default', nodes=[
			Node(active=True, form='s', position=(0, 0, 0), rotation=(0, 0)),
			Node(active=True, form='s', position=(3, 0, 0), rotation=(0, 0))
		])

pipe_straight = Tube(model='pipe_straight', texture='default', nodes=[
			Node(active=True, form='s', position=(0, 0, 0), rotation=(0, 0)),
			Node(active=True, form='s', position=(3, 0, 0), rotation=(0, 0))])

class Dungeon(Entity):
	def __init__(self):
		super().__init__()
		# Initialize variables and things the generator needs

		print('Dungeon initializing...')


	def update(self):
		# Generation algorithm occurs here, running every tick:
		# print('Dungeon updating...')

		pass


dungeon = Dungeon()
