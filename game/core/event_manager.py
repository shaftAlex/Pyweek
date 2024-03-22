class EventManager:
	def __init__(self):
		self.listeners = {}

	def add_listener(self, event, callback):
		if event not in self.listeners:
			self.listeners[event] = []
		self.listeners[event].append(callback)

	def trigger_event(self, event, *args, **kwargs):
		if event in self.listeners:
			for callback in self.listeners[event]:
				callback(*args, **kwargs)
