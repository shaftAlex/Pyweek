from ursina import *
from ursina.shaders import lit_with_shadows_shader
from junk import Junk
from food import Food
from treasure import Treasure
from player import Player
from dungeon import Dungeon

app = Ursina()

window.title = 'PyWeek - Tubes'
window.borderless = False
window.fullscreen = False
window.exit_button.visible = False
window.fps_counter.enabled = True

Entity.default_shader = lit_with_shadows_shader

player = Player(position = (0, 3, 0))

dungeon = Dungeon()

sun = DirectionalLight()
sun.look_at(Vec3(1, -1, -1))
sky = Sky(texture='assets/textures/skybox')
ground = Entity(model='plane', collider='box', position=(0, 0, 0), scale=24, texture='assets/textures/default', texture_scale=(6, 6))

# spawn some random junk
for i in range(10):
	junk = Junk(position=(random.uniform(-10, 10), 0, random.uniform(-10, 10)))
	player.ignore_list.append(junk)

# spawn some random food
for i in range(10):
	food = Food(position=(random.uniform(-10, 10), 0, random.uniform(-10, 10)))
	player.ignore_list.append(food)

# spawn some random treasure
for i in range(10):
	treasure = Treasure(position=(random.uniform(-10, 10), 0, random.uniform(-10, 10)))
	player.ignore_list.append(treasure)


# Pause handler
pause_overlay = Entity(model='quad', scale=100, color=color.black33, enabled=False, parent=camera.ui)
pause_text = Text('PAUSED', origin=(0,0), scale=2, enabled=False)

def pause_handler_input(key):
	if key == 'escape':
		application.paused = not application.paused # Pause/unpause the game.
		pause_text.enabled = application.paused 
		pause_overlay.enabled = application.paused
		mouse.locked = not application.paused
pause_handler = Entity(ignore_paused=True,input = pause_handler_input) # needs to be its own entity, so that i can set ignore_paused to True

editor_camera = EditorCamera(enabled=False)

def input(key):
	if key == 'f1':
		editor_camera.enabled = not editor_camera.enabled

app.run()
