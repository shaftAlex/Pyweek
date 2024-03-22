from ursina import *
from enum import Enum

class ButtonId(Enum):
  JUMP = 1
  ACCEPT = 2
  BACK = 3

class AxisId(Enum):
  VERTICAL = 1
  HORIZONTAL = 2

def getButton(id: ButtonId) -> bool:
  if id == ButtonId.JUMP:
    return held_keys['space']
  elif id == ButtonId.ACCEPT:
    return held_keys['c']
  elif id == ButtonId.BACK:
    return held_keys['x']
  else:
    raise("Invalid ButtonId")

def getAxis(id: AxisId) -> float:
  # WASD input for now
  if id == AxisId.VERTICAL:
    if held_keys['w']:
      return 1
    elif held_keys['s']:
      return -1
    else:
      return 0
  elif id == AxisId.HORIZONTAL:
    if held_keys['d']:
      return 1
    elif held_keys['a']:
      return -1
    else:
      return 0
  else:
    raise("Invalid AxisId")