from ursina import *
from ursina.shaders import lit_with_shadows_shader
from player import Player
import globals as g

sys.tracebacklimit = 1

class Game(Entity):

	def __init__(self):
		super().__init__(position=Vec3(0, 0, 0), ignore_paused=True)

		self.sun = DirectionalLight()
		self.sun.look_at(Vec3(1, -1, -1))
		self.sky = Sky(texture='skybox')
		self.ground = Entity(model='plane', collider='box', scale=128, texture='default', texture_scale=(32, 32))

		return

	def input(self, key):

		if key == 'escape':
			self.exit_application()

		return

	def update(self):
		return

	def exit_application(self):
		app.userExit()
		return


app = Ursina()

Entity.default_shader = lit_with_shadows_shader

g.GAME = Game()
g.PLAYERS = Player(position=Vec3(0, 1, 0))

app.run()
