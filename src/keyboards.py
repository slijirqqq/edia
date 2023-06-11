import logging

from psychopy.constants import NOT_STARTED, STARTED
from psychopy.hardware import keyboard

from src.components import MainWindow
from src.constants import SPACE_BAR, FRAME_TOLERANCE
from src.utils.decorators import to_quit
from src.utils.mixins import ComponentMixin

logger = logging.getLogger(__name__)


class DefaultKeyboard(ComponentMixin, keyboard.Keyboard):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._window = MainWindow()

    @to_quit
    def check(self, time: float, frame: int, this_flip: float, global_flip: float) -> bool:
        return super().check(time, frame, this_flip, global_flip)


class FirstStageKeyboard(DefaultKeyboard):

    @to_quit
    def check(self, time: float, frame: int, this_flip: float, global_flip: float) -> bool:
        if self.status == NOT_STARTED and this_flip >= 0. - FRAME_TOLERANCE:
            self.status = STARTED
            self._window.callOnFlip(self.clock.reset)
            self._window.callOnFlip(self.clearEvents, eventType='keyboard')
        if self.status == STARTED:
            pressed = self.getKeys(
                keyList=[SPACE_BAR],
                waitRelease=False,
            )
            if pressed:
                logger.info(
                    'Pressed %(button)s for exec handler to next step',
                    {
                        'button': SPACE_BAR,
                    },
                )
                self.keys = pressed[-1].name
                self.rt = pressed[-1].rt
                self._continue = False
        return super().check(time, frame, this_flip, global_flip)
