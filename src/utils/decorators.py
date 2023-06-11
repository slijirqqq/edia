import functools
import logging
from typing import Callable

from psychopy import core

from src.constants import ESCAPE

logger = logging.getLogger(__name__)


def to_quit(func: Callable):
    @functools.wraps(func)
    def wrapper(instance, *args, **kwargs):
        if instance.getKeys(
                keyList=[ESCAPE],
                waitRelease=False
        ):
            logger.info(
                'Quit by %(button)s from %(keyboard)s',
                {
                    'button': ESCAPE,
                    'keyboard': instance.__class__.__name__,
                }
            )
            core.quit()
        return func(instance, *args, **kwargs)

    return wrapper
