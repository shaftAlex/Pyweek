from ursina import *

import globals as g

from game.core import CollisionHandler, EventManager, InputHandler, Player, StateManager


class Game(Entity):
	def __init__(self):
		super().__init__(position=Vec3(0, 0, 0), ignore_paused=True)

		g.EVENT_MANAGER = EventManager
		g.STATE_MANAGER = StateManager
		g.INPUT_HANDLER = InputHandler

		return

	def input(self, key):
		InputHandler(key)

	def update(self):
		pass


def main():
	g.APP = Ursina()

	g.GAME = Game()
	g.PLAYER = Player()

	g.APP.run()


if __name__ == '__main__':
	main()
