from psychopy import data

from src.config import settings
from src.constants import TrialMethod
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


class FirstStageTrial(data.TrialHandler):

    def __init__(self):
        super().__init__(
            nReps=1.,
            method=TrialMethod.sequential.value,
            originPath=-1,
            trialList=data.importConditions(
                str(settings.STATIC_DIR / 'trial' / 'first_stage.xlsx')
            ),
            name='first_stage_trials',
        )
