from psychopy import data

from src.exceptions import ObjectNotInitialized
from src.utils.meta import SingletonMeta


class ExperimentHandler(data.ExperimentHandler, metaclass=SingletonMeta):

    def __init__(self, name: str, version: str):
        super().__init__(
            name=name,
            version=version,
            autoLog=False,
        )

    @classmethod
    def get_handler(cls):
        if cls not in cls._instances:
            raise ObjectNotInitialized
        return cls._instances[cls]
