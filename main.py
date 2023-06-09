import logging

from psychopy import core

from src.components import MainWindow
from src.config import Settings
from src.handlers import ExperimentHandler

logger = logging.getLogger(__name__)


def main():
    settings = Settings()
    # dialog = GreetingsDialog(title=settings.EXPERIMENT_NAME)
    # if not dialog.OK:
    #     logger.info(
    #         'Participant %(participant)s canceled from experiment',
    #         {
    #             'participant': dialog.data[0],
    #         },
    #     )
    #     core.quit()
    # else:
    #     logger.info(
    #         'Participant %(participant)s starting the experiment',
    #         {
    #             'participant': dialog.data[0],
    #         },
    #     )
    clock = core.Clock()
    ExperimentHandler(
        name=settings.EXPERIMENT_NAME,
        version=settings.EDIA_VERSION,
    )
    window = MainWindow()
    window.close()
    core.quit()


if __name__ == '__main__':
    main()
