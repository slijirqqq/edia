from pathlib import Path

from psychopy import data
from pydantic import BaseSettings

from src.logging import setup_logging
from src.utils.version import get_version


class Settings(BaseSettings):
    BASE_DIR: Path = Path(__file__).resolve().parent.parent
    SOURCE_DIR: Path = BASE_DIR / 'src'
    STATIC_DIR: Path = SOURCE_DIR / 'dist'
    EXPERIMENT_NAME: str = 'EDIA'
    EDIA_VERSION: str = get_version(BASE_DIR)
    PSYCHOPY_VERSION: str
    DATE = data.getDateStr()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        setup_logging(self.SOURCE_DIR)

    class Config:
        env_file: tuple[str, str] = '.env', '.env.example'
        env_file_encoding: str = 'utf-8'


settings = Settings()
