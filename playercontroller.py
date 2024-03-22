from ursina import *

from input_controller import AxisId, getAxis

class PlayerController(Entity):
  def __init__(self, **kwargs):
    super().__init__()
    self.speed = 5
    self.height = 2
    self.camera_pivot = Entity(parent=self, y=self.height)

    self.camera_max_distance = 10

    camera.parent = self.camera_pivot
    camera.position = (0,0,-7)
    camera.rotation = (0,0,0)
    camera.fov = 90
    mouse.locked = True
    self.mouse_sensitivity = Vec2(40, 40)

    self.gravity = 1
    self.grounded = False
    self.jump_height = 2
    self.jump_up_duration = .5
    self.fall_after = .35 # will interrupt jump up
    self.jumping = False
    self.air_time = 0

    self.traverse_target = scene     # by default, it will collide with everything. change this to change the raycasts' traverse targets.
    self.ignore_list = [self, ]
    self.on_destroy = self.on_disable

    for key, value in kwargs.items():
      setattr(self, key ,value)

      # make sure we don't fall through the ground if we start inside it
      if self.gravity:
        ray = raycast(self.world_position+(0,self.height,0), self.down, traverse_target=self.traverse_target, ignore=self.ignore_list)
        if ray.hit:
          self.y = ray.world_point.y

  def update(self):
    self.rotation_y += mouse.velocity[0] * self.mouse_sensitivity[1]

    self.camera_pivot.rotation_x -= mouse.velocity[1] * self.mouse_sensitivity[0]
    self.camera_pivot.rotation_x = clamp(self.camera_pivot.rotation_x, -90, 90)

    # clamp camera distance so that we don't clip through walls
    distance = self.camera_max_distance

    # raycast from player towards camera position
    # TODO: ray goes wrong direction?
    ray = raycast(self.position, self.camera_pivot.back, distance=self.camera_max_distance, traverse_target=self.traverse_target, ignore=self.ignore_list)

    if ray.hit:
      distance = ray.distance
    self.camera_pivot.z = -distance

    # self.direction = Vec3(
    #   self.forward * (held_keys['w'] - held_keys['s'])
    #   + self.right * (held_keys['d'] - held_keys['a'])
    # ).normalized()

    self.direction = Vec3(
      getAxis(AxisId.HORIZONTAL),
      0,
      getAxis(AxisId.VERTICAL),
    ).normalized()

    feet_ray = raycast(self.position+Vec3(0,0.5,0), self.direction, traverse_target=self.traverse_target, ignore=self.ignore_list, distance=.5, debug=False)
    head_ray = raycast(self.position+Vec3(0,self.height-.1,0), self.direction, traverse_target=self.traverse_target, ignore=self.ignore_list, distance=.5, debug=False)
    if not feet_ray.hit and not head_ray.hit:
      move_amount = self.direction * time.dt * self.speed

      if raycast(self.position+Vec3(-.0,1,0), Vec3(1,0,0), distance=.5, traverse_target=self.traverse_target, ignore=self.ignore_list).hit:
        move_amount[0] = min(move_amount[0], 0)
      if raycast(self.position+Vec3(-.0,1,0), Vec3(-1,0,0), distance=.5, traverse_target=self.traverse_target, ignore=self.ignore_list).hit:
        move_amount[0] = max(move_amount[0], 0)
      if raycast(self.position+Vec3(-.0,1,0), Vec3(0,0,1), distance=.5, traverse_target=self.traverse_target, ignore=self.ignore_list).hit:
        move_amount[2] = min(move_amount[2], 0)
      if raycast(self.position+Vec3(-.0,1,0), Vec3(0,0,-1), distance=.5, traverse_target=self.traverse_target, ignore=self.ignore_list).hit:
        move_amount[2] = max(move_amount[2], 0)
      self.position += move_amount

    if self.gravity:
      # gravity
      ray = raycast(self.world_position+(0,self.height,0), self.down, traverse_target=self.traverse_target, ignore=self.ignore_list)

      if ray.distance <= self.height+.1:
        if not self.grounded:
          self.land()
        self.grounded = True
        # make sure it's not a wall and that the point is not too far up
        if ray.world_normal.y > .7 and ray.world_point.y - self.world_y < .5: # walk up slope
          self.y = ray.world_point[1]
        return
      else:
        self.grounded = False

      # if not on ground and not on way up in jump, fall
      self.y -= min(self.air_time, ray.distance-.05) * time.dt * 100
      self.air_time += time.dt * .25 * self.gravity


  def input(self, key):
    if key == 'space':
      self.jump()

  def jump(self):
    if not self.grounded:
      return

    self.grounded = False
    self.animate_y(self.y+self.jump_height, self.jump_up_duration, resolution=int(1//time.dt), curve=curve.out_expo)
    invoke(self.start_fall, delay=self.fall_after)

  def start_fall(self):
    self.y_animator.pause()
    self.jumping = False

  def land(self):
    self.air_time = 0
    self.grounded = True

  def on_enable(self):
    mouse.locked = True
    # restore parent and position/rotation from before disablem in case you moved the camera in the meantime.
    if hasattr(self, 'camera_pivot') and hasattr(self, '_original_camera_transform'):
      camera.parent = self.camera_pivot
      camera.transform = self._original_camera_transform

  def on_disable(self):
    mouse.locked = False
    self.cursor.enabled = False
    self._original_camera_transform = camera.transform  # store original position and rotation
    camera.world_parent = scene