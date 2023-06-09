import logging
import logging.config
from functools import lru_cache
from pathlib import Path
from typing import Any

import yaml
from psychopy import logging as psy_logging

logger = logging.getLogger(__name__)


@lru_cache
def setup_logging(source: Path) -> None:
    """Setup logging config from logging.yml file.

    :param source: Project base directory.
    :type source: Path
    """
    psy_logging.console.setLevel(psy_logging.CRITICAL)
    logging_dir: Path = source / 'logging.yml'
    try:
        with logging_dir.open('r', encoding='utf-8') as logging_config:
            config: dict[str, Any] = yaml.safe_load(logging_config)
        logging.config.dictConfig(config)
        logger.info('Logging configuration successfully.')
    except IOError:
        logging.basicConfig(level=logging.INFO)
        logger.warning('Logging config file not found, using basic config...')
