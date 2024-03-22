from ursina import *

class Food(Entity):
  def __init__(self, position: Vec3):
    super().__init__()

    self.model = 'cube'
    self.color = color.green
    self.position = position
    self.scale = Vec3(0.5, 0.5, 0.5)
    self.collider = SphereCollider(self, center=Vec3(0, 0, 0), radius=0.5)

  def update(self):
    self.rotation_y += 1

    # player pickup
    hit_info = self.intersects()
    if hit_info.hit:
      if hit_info.entity.name == 'player':
        # play sound
        sound = Audio('assets/sounds/item_pickup.wav', autoplay=True, auto_destroy=True)
        hit_info.entity.food += 1
        self.disable()