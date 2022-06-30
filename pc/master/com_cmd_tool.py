import sys
import logging
from logging.handlers import RotatingFileHandler
import os

from config import Config
from communication import Handler


def setup_logging():
    if Config.SHOULD_LOG_IN_FILE:
        os.makedirs(Config.LOG_DIR, exist_ok=True)
        logging.basicConfig(
            format=Config.LOG_FORMAT,
            level=Config.LOG_LEVEL,
            handlers=[
                RotatingFileHandler(filename=os.path.join(Config.LOG_DIR, f"{__file__.split('/')[-1]}.log"),
                                    mode=Config.LOG_FILE_MODE,
                                    maxBytes=Config.LOG_MAX_BYTES,  # 5MB
                                    backupCount=Config.LOG_BACKUP_COUNT,
                                    encoding=Config.LOG_ENCRYPTION_TYPE,
                                    delay=0),
                logging.StreamHandler()
            ]
        )
    else:
        logging.basicConfig(format=Config.LOG_FORMAT, level=Config.LOG_LEVEL)


# change cwd to scripts location
os.chdir(os.path.dirname(os.path.abspath(__file__)))

setup_logging()

argv = sys.argv[1:]
if len(argv) < 1:
    logging.error("Falsche Eingabe (Richtiges Format: Befehl Arg1 Arg2 ...)")
    exit(1)

cmd, *args = argv
handler = Handler()
success = handler.exec(cmd, args)

if not success:
    logging.error("Failed to execute the command. Check the errors above.")
