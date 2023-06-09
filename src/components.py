import uuid
from tkinter import Tk

from psychopy import gui, visual

from src.utils.meta import SingletonMeta
from src.utils.mixins import ComponentMixin


class MainWindow(visual.Window, metaclass=SingletonMeta):
    def __init__(self):
        root = Tk()
        size = (
            root.winfo_screenwidth() // 2,
            root.winfo_screenheight() // 2,
        )
        super().__init__(
            size=size,
            # fullscr=True,
            screen=0,
            color=(0, 0.502, 0.502),
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


class InstructionComponent(visual.TextBox2, ComponentMixin):

    def __init__(self, text: str):
        super().__init__(
            win=MainWindow(),
            text=text,
            name='instruction',
            color='white',
            alignment='center',
        )
