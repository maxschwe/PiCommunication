import os
import logging


class Config:
    # ==================================================================
    # LOG configuration
    # ==================================================================
    LOG_DIR = "log"
    LOG_LEVEL = logging.INFO
    LOG_FORMAT = '%(asctime)s: [%(levelname)s] %(message)s'
    LOG_ENCRYPTION_TYPE = "utf-8"
    SHOULD_LOG_IN_FILE = True
    LOG_FILE_MODE = "w"
    LOG_MAX_BYTES = 5_000_000
    LOG_BACKUP_COUNT = 2
