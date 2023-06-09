import logging

from psychopy import core

from src.components import GreetingsDialog, MainWindow
from src.config import settings
from src.handlers import ExperimentHandler
from src.models import ExperimentData
from src.runners import (EndStageRunner, FirstStageRunner, SecondStageRunner,
                         ThirdStageRunner)

logger = logging.getLogger(__name__)


def init() -> tuple[core.Clock, core.CountdownTimer]:
    global_clock = core.Clock()
    routine_timer = core.CountdownTimer()
    ExperimentHandler(
        name=settings.EXPERIMENT_NAME,
        version=settings.EDIA_VERSION,
    )
    return global_clock, routine_timer


def main():
    dialog = GreetingsDialog(title=settings.EXPERIMENT_NAME)
    if not dialog.OK:
        logger.info(
            'Participant %(participant)s canceled from experiment',
            {
                'participant': dialog.data[0],
            },
        )
        core.quit()
    else:
        logger.info(
            'Participant %(participant)s starting the experiment',
            {
                'participant': dialog.data[0],
            },
        )
    global_clock, routine_timer = init()
    window = MainWindow()

    experiment_data = ExperimentData()

    FirstStageRunner(timer=routine_timer, clock=global_clock).run()
    SecondStageRunner(timer=routine_timer, clock=global_clock, data=experiment_data).run()
    ThirdStageRunner(timer=routine_timer, clock=global_clock, data=experiment_data).run()
    EndStageRunner(timer=routine_timer, clock=global_clock).run()
    experiment_data.to_csv(dialog.data[0])

    window.close()
    core.quit()


if __name__ == '__main__':
    main()
