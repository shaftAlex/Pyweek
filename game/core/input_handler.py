import globals as g
from ursina import Entity

class InputHandler(Entity):
    def __init__(self, key):
        super().__init__(key)
        pass

    def update(key):
        if key == 'escape':
            g.APP.userExit()

        return
