import logging

from psychopy import core
from psychopy.constants import NOT_STARTED, STARTED, FINISHED
from psychopy.core import Clock

from src.components import MainWindow, InstructionComponent
from src.constants import FRAME_TOLERANCE, ESCAPE, SPACE_BAR
from src.keyboards import FirstStageKeyboard

logger = logging.getLogger(__name__)


class FirstStageRunner:

    def __init__(self):
        pass
