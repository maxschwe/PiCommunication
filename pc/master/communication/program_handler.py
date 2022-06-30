import json
import logging
import os
import traceback

from .config import Config


class ProgramHandler:
    def __init__(self):
        self.cmds = {"remember": self.remember,
                     "forget": self.forget,
                     "print": self.print}
        self.load_data()

    def exec(self, cmd, args):
        func = self.cmds[cmd]
        try:
            return func(*args)
        except TypeError:
            logging.error(
                f"Wrong amount of arguments specified ({len(args)} given/{func.__code__.co_argcount-1} needed)")
            return False
        except Exception:
            logging.error(traceback.format_exc())
            return False

    def load_data(self):
        if os.path.exists(Config.PATH_DATA):
            try:
                with open(Config.PATH_DATA) as f:
                    data = json.load(f)
                self.data = data
                return
            except Exception as e:
                logging.error(e.args)
        self.data = {"matched_names": {}}

    def save_data(self):
        with open(Config.PATH_DATA, "w") as f:
            json.dump(self.data, f)

    def remember(self, name, path):
        if not os.path.isdir(path):
            logging.info(f"Specified path {path} was not found")
            return False
        if name in self.data["matched_names"]:
            logging.warning(f"You have overwritten matched path for {name}.")
        self.data["matched_names"][name] = path
        self.save_data()
        return True

    def forget(self, name):
        if name not in self.data["matched_names"]:
            logging.warning(f"Specified name {name} was not found")
        else:
            self.data["matched_names"].pop(name)
            self.save_data()
        return True

    def print(self):
        for key, value in self.data.items():
            logging.info(f"{key}:")
            for k, v in value.items():
                logging.info(f"--- {k}: {v}")
        return True
