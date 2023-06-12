import logging

from psychopy.constants import NOT_STARTED, STARTED
from psychopy.hardware import keyboard

from src.components import MainWindow
from src.constants import FRAME_TOLERANCE, LEFT, RIGHT, SPACE_BAR
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


class InstructionStepKeyboard(DefaultKeyboard):

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


class QuestionKeyboard(DefaultKeyboard):

    @to_quit
    def check(self, time: float, frame: int, this_flip: float, global_flip: float, keys: list[str]) -> bool:
        if self.status == NOT_STARTED and this_flip >= 0. - FRAME_TOLERANCE:
            self.status = STARTED
            self._window.callOnFlip(self.clock.reset)
            self._window.callOnFlip(self.clearEvents, eventType='keyboard')
        if self.status == STARTED:
            pressed = self.getKeys(
                keyList=keys,
                waitRelease=False,
            )
            if pressed:
                logger.info(
                    'Pressed %(button)s for exec handler to next step',
                    {
                        'button': pressed[-1].name,
                    },
                )
                self.keys = pressed[-1].name
                self.rt = pressed[-1].rt
                self._continue = False
        return super().check(time, frame, this_flip, global_flip)

    def disable(self):
        self.status = NOT_STARTED
        self._continue = True


class ImageChoiceKeyboard(DefaultKeyboard):

    @to_quit
    def check(self, time: float, frame: int, this_flip: float, global_flip: float, correct_answers) -> bool:
        if self.status == NOT_STARTED and this_flip >= 0. - FRAME_TOLERANCE:
            self.status = STARTED
            self._window.callOnFlip(self.clock.reset)
            self._window.callOnFlip(self.clearEvents, eventType='keyboard')
        if self.status == STARTED:
            pressed = self.getKeys(
                keyList=[LEFT, RIGHT],
                waitRelease=False,
            )
            if pressed:
                logger.info(
                    'Pressed %(button)s for exec handler to next step',
                    {
                        'button': pressed[-1].name,
                    },
                )
                self.keys = pressed[-1].name
                self.rt = pressed[-1].rt
                if self.keys == correct_answers:
                    self.corr = True
                else:
                    self.corr = False
                self._continue = False
        return super().check(time, frame, this_flip, global_flip)

    def disable(self):
        self.status = NOT_STARTED
        self._continue = True
