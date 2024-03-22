from pathlib import Path
from ursina import *

segments = []

class Tube(Entity):
	def __init__(self, name: str):
		super().__init__(active=False)

		self.name = name
		self.model = name
		self.scale_setter(6)
		self.double_sided_setter(True)
		self.collider_setter('mesh')
		# self.texture = texture_name
		self.disable()

class Dungeon(Entity):
	def __init__(self):
		super().__init__()

		self.prepare()
		self.start()

	def prepare(self):
		directory = Path('assets') / 'dungeon' / 'segments'

		for file in directory.iterdir():
			if file.is_file():
				var = file.stem
				var = Tube(str(var))
				segments.append(var)

		print(segments)

	def start(self):
		sewer_start = Tube('sewer_start_1')
		sewer_start.enable()

	def update(self):
		pass

if __name__ == '__main__':
	# definitions()
	pass
