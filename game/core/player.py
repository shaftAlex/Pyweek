from ursina import Entity

class Player(Entity):
	def __init__(self):
		super().__init__()
		self.inventory = Inventory()

	def pickup_item(self, item):
		self.inventory.add_item(item)

class Inventory:
	def __init__(self):
		self.items = []

	def add_item(self, item):
		self.items.append(item)
