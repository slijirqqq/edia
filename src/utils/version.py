import logging
from pathlib import Path

logger = logging.getLogger(__name__)

_DEFAULT_VERSION: str = 'develop'


def get_version(root_dir: Path) -> str:
    """Get current API version."""
    version_file_path: Path = root_dir / 'version.txt'
    try:
        with version_file_path.open('r', encoding='utf-8') as file:
            version: str = ''.join(file.readlines()).strip()
    except FileNotFoundError:
        logger.exception('version.txt not found.')
        return _DEFAULT_VERSION
    return version
