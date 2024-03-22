from ursina import *
from input_controller import AxisId, getAxis
from ursina.prefabs.first_person_controller import FirstPersonController

class Player(FirstPersonController):

	def __init__(self, position: Vec3):
		super().__init__(position=position, jump_height=2.5, jump_duration=0.4, origin_y=-0.5)

		self.ignore_list = [self]

		self.model = 'assets/models/rat.glb'
		self.collider = MeshCollider(self, mesh=self.model)

		self.treasure = 0
		self.junk = 0
		self.food = 0

		self.health = 3

		#	TODO: make camera actually in a nice position, and maybe not just static
		camera.z = -12
		camera.y = 1.5

		self.speed = 7
		self.collider = BoxCollider(self, center=Vec3(0, 1.25, 0), size=Vec3(1, 2.5, 1.25))

		# player HUD

		# health icons, in the top left corner, 3 hearts
		self.health_icon1 = Entity(model='quad', texture='assets/textures/heart.png', scale=0.05, x=-0.45, y=0.45, parent=camera.ui)
		self.health_icon2 = Entity(model='quad', texture='assets/textures/heart.png', scale=0.05, x=-0.4, y=0.45, parent=camera.ui)
		self.health_icon3 = Entity(model='quad', texture='assets/textures/heart.png', scale=0.05, x=-0.35, y=0.45, parent=camera.ui)

		# inventory icons: type icon then number

		self.food_icon = Entity(model='quad', texture='assets/textures/food.png', scale=0.05, x=0.45, y=0.45, parent=camera.ui)
		self.food_text = Text(str(self.food), origin=(0, 0), scale=2, x=0.5, y=0.45, parent=camera.ui)

		self.junk_icon = Entity(model='quad', texture='assets/textures/junk.png', scale=0.05, x=0.45, y=0.4, parent=camera.ui)
		self.junk_text = Text(str(self.junk), origin=(0, 0), scale=2, x=0.5, y=0.4, parent=camera.ui)

		self.treasure_icon = Entity(model='quad', texture='assets/textures/treasure.png', scale=0.05, x=0.45, y=0.35, parent=camera.ui)
		self.treasure_text = Text(str(self.treasure), origin=(0, 0), scale=2, x=0.5, y=0.35, parent=camera.ui)

		return

	def update(self):
		# FIXME: uses builtin controls
		super().update()

		# player HUD

		# health
		if self.health == 3:
			self.health_icon1.enabled = True
			self.health_icon2.enabled = True
			self.health_icon3.enabled = True
		elif self.health == 2:
			self.health_icon1.enabled = True
			self.health_icon2.enabled = True
			self.health_icon3.enabled = False
		elif self.health == 1:
			self.health_icon1.enabled = True
			self.health_icon2.enabled = False
			self.health_icon3.enabled = False
		elif self.health == 0:
			self.health_icon1.enabled = False
			self.health_icon2.enabled = False
			self.health_icon3.enabled = False

		self.treasure_text.text = str(self.treasure)
		self.junk_text.text = str(self.junk)
		self.food_text.text = str(self.food)

		return

	def input(self, key):
		if key == 'left mouse down':
			print('left click')
		if key == 'right mouse down':
			print('right click')
		super().input(key)
		return
