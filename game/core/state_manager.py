from game.level import dev
class StateManager:
	def __init__(self):
		super().__init__()
		self.current_scene = dev
		self.game_state = 'running'

	def switch_scene(self, new_scene):
		self.current_scene = new_scene

	def pause_game(self):
		self.game_state = 'paused'

	def resume_game(self):
		self.game_state = 'running'
