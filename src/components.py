import uuid
from tkinter import Tk

from psychopy import gui, visual
from psychopy.constants import NOT_STARTED

from src.config import settings
from src.constants import FRAME_TOLERANCE
from src.models import QuestionChoice
from src.utils.meta import SingletonMeta
from src.utils.mixins import ComponentMixin, ImageComponentMixin


class MainWindow(visual.Window, metaclass=SingletonMeta):
    def __init__(self):
        root = Tk()
        size = (
            root.winfo_screenwidth() // 2,
            root.winfo_screenheight() // 2,
        )
        super().__init__(
            size=size,
            fullscr=True,
            screen=0,
            color=(0., 0., 0.),
            winType='pyglet',
            allowGUI=False,
            monitor='testMonitor',
            useFBO=True,
            units='height',
        )


class GreetingsDialog(gui.DlgFromDict):

    def __init__(self, title: str):
        super().__init__(
            dictionary={
                'participant': str(uuid.uuid4()),
                'session': '001',
            },
            title=title,
            sort_keys=False
        )


class DefaultComponent(ComponentMixin):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._window = MainWindow()

    def check(self, time: float, frame: int, this_flip: float, global_flip: float) -> bool:
        if self.status == NOT_STARTED and this_flip >= 0. - FRAME_TOLERANCE:
            self.frame_start = frame
            self.start_at = time
            self.start_refresh_at = global_flip
            self._window.timeOnFlip(self, 'start_refresh_at')
            self.auto_draw(True)
        return super().check(time, frame, this_flip, global_flip)


class InstructionComponent(DefaultComponent, visual.TextBox2):

    def __init__(self, text: str):
        super().__init__(
            win=MainWindow(),
            text=text,
            name='instruction',
            color='white',
            alignment='center',
        )


class ImageComponent(DefaultComponent, ImageComponentMixin, visual.ImageStim):

    def __init__(self):
        super().__init__(
            win=MainWindow(),
            image='sin',
            size=(0.5, 0.5),
            interpolate=True,
        )


class ChoiceQuestionComponent(DefaultComponent, visual.TextBox2):
    def __init__(self, text: str, choices: list[QuestionChoice]):
        super().__init__(
            win=MainWindow(),
            text=text,
            name='question',
            color='white',
            alignment='center',
        )
        self._choices = choices


class TextQuestionComponent(DefaultComponent, visual.TextBox2):

    def __init__(self, text: str):
        super().__init__(
            win=MainWindow(),
            text=text,
            name='question',
            color='white',
            alignment='center',
            anchor='bottom',
        )


class AnswerQuestionComponent(DefaultComponent, visual.TextBox2):
    def __init__(self):
        super().__init__(
            win=MainWindow(),
            text='',
            name='question',
            color='white',
            alignment='center',
            anchor='top',
            editable=True,
        )


class XImageComponent(DefaultComponent, ImageComponentMixin, visual.ImageStim):
    def __init__(self):
        super().__init__(
            win=MainWindow(),
            image=str(settings.STATIC_DIR / 'x.png'),
            size=(1.3, 1.3),
            interpolate=True,
            name='x-image',
        )


class RightImageComponent(DefaultComponent, ImageComponentMixin, visual.ImageStim):

    def __init__(self):
        super().__init__(
            win=MainWindow(),
            image='sin',
            pos=(0.4, 0.),
            interpolate=True,
            name='right-image',
        )


class LeftImageComponent(DefaultComponent, ImageComponentMixin, visual.ImageStim):

    def __init__(self):
        super().__init__(
            win=MainWindow(),
            image='sin',
            pos=(-0.4, 0.),
            interpolate=True,
            name='left-image',
        )
