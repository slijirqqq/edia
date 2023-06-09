from psychopy.constants import NOT_STARTED


class ComponentMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.status = NOT_STARTED
