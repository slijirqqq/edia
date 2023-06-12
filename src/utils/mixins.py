from psychopy.constants import NOT_STARTED


class ComponentMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.status = NOT_STARTED
        self._start_at: float | None = None
        self._start_refresh_at: float | None = None
        self._stop_at: float | None = None
        self._stop_refresh_at: float | None = None
        self._frame_start: float | None = None
        self._continue = True

    def auto_draw(self, mode: bool = False):
        if hasattr(self, 'setAutoDraw'):
            self.setAutoDraw(mode)

    @property
    def start_at(self):
        return self._start_at

    @start_at.setter
    def start_at(self, value: float):
        self._start_at = value

    @property
    def start_refresh_at(self):
        return self._start_refresh_at

    @start_refresh_at.setter
    def start_refresh_at(self, value: float):
        self._start_refresh_at = value

    @property
    def stop_at(self):
        return self._stop_at

    @stop_at.setter
    def stop_at(self, value: float):
        self._stop_at = value

    @property
    def stop_refresh_at(self):
        return self._stop_refresh_at

    @stop_refresh_at.setter
    def stop_refresh_at(self, value: float):
        self._stop_refresh_at = value

    @property
    def frame_start(self):
        return self._frame_start

    @frame_start.setter
    def frame_start(self, value: int):
        self._frame_start = value

    def check(self, time: float, frame: int, this_flip: float, global_flip: float) -> bool:
        return self._continue


class RunnerInstructionMixin:
    def _instruction_step(self):
        while self._continue:
            self._update_time()
            self._continue = self.check(self._instruction)
            self._continue = self.check(self._keyboard)

            self.flip()


class ImageComponentMixin:
    def disable(self):
        self.auto_draw(False)
        self.status = NOT_STARTED
