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
  return False

def getAxis(id: AxisId) -> float:
  return 0