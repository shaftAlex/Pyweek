from game.gui.main_menu import MainMenu
from game.gui.pause_menu import PauseMenu
from game.gui.settings_menu import SettingsMenu
from game.core import InputHandler

from ursina import Entity

class GUI(Entity):
	def __init__(self):
		super().__init__()
		self.input_handler = InputHandler

	def input(self, key):
		InputHandler(key)

	def update(self):
		pass
