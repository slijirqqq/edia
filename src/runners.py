import logging

from psychopy import core
from psychopy.visual import Window

from src.components import MainWindow, InstructionComponent, ImageComponent
from src.handlers import ExperimentHandler, FirstStageTrial
from src.keyboards import FirstStageKeyboard, DefaultKeyboard

logger = logging.getLogger(__name__)


class DefaultRunner:

    def __init__(self, timer: core.CountdownTimer, clock: core.Clock):
        self._experiment: ExperimentHandler = ExperimentHandler.get_handler()
        self._window: Window = MainWindow()
        self._timer: core.CountdownTimer = timer
        self._global_clock: core.Clock = clock
        self._reset()

    def flip(self):
        if self._continue:
            self._window.flip()

    @staticmethod
    def _disable_auto_draw(*components):
        for component in components:
            component.auto_draw(False)

    def _reset(self):
        self._timer.reset()
        self._continue: bool = True
        self._time: float = 0.
        self._frame: int = -1


class FirstStageRunner(DefaultRunner):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._clock = core.Clock()
        self._keyboard = FirstStageKeyboard()
        self._default_keyboard = DefaultKeyboard()
        self._instruction = InstructionComponent(
            text='Сейчас перед Вами будут появляться фотографии, внимательно рассмотртите их.\n\n'
                 'Для продолжения нажмите "пробел"',
        )
        self._image = ImageComponent()
        self._trials = FirstStageTrial()
        self._continue = True

    def run(self):
        self._preprocessing_stage()

        self._instruction_flow()

        self._disable_auto_draw(self._instruction)
        self._reset()

        self._continue = True
        self._experiment.addLoop(self._trials)
        self._trial_flow()

    def _instruction_flow(self):
        while self._continue:
            self._update()
            self._continue = self.check(self._instruction)
            self._continue = self.check(self._keyboard)

            self.flip()

    def _trial_flow(self):
        while self._continue:
            self._timer.addTime(5.)
            self._time = 0.
            self._frame = -1
            self._clock.reset(
                -self._window.getFutureFlipTime(clock='now')
            )
            try:
                image: dict = self._trials.next()
                self._image.setImage(image.get('imagefile'))
                while self._timer.getTime() > 0.:
                    self._update()
                    self._continue = self.check(self._image)
                    self._continue = self.check(self._default_keyboard)
                    self.flip()
                self._image.disable()
                self._timer.addTime(15.)
                while self._timer.getTime() > 0.:
                    self._update()
                    self._continue = self.check(self._default_keyboard)
                    self.flip()
            except StopIteration:
                self._continue = False

    def _preprocessing_stage(self):
        self._clock.reset(
            -self._window.getFutureFlipTime(clock='now')
        )

    def _update(self):
        self._time = self._clock.getTime()
        self._this_flip = self._window.getFutureFlipTime(clock=self._clock)
        self._global_flip = self._window.getFutureFlipTime(clock=None)
        self._frame += 1

    def check(self, component) -> bool:
        return component.check(
            self._time,
            self._frame,
            self._this_flip,
            self._global_flip,
        )
