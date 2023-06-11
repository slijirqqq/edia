from enum import Enum

ESCAPE = 'escape'
SPACE_BAR = 'space'

FRAME_TOLERANCE = 0.001


class TrialMethod(Enum):
    sequential = 'sequential'
    random = 'random'
