import socket
import logging
import time

from .config import Config


class ConnectionHandler:
    def __init__(self):
        self.connected = False
        self.cmds = {"sync": self.sync,
                     "exec": self.exec,
                     "sync_exec": self.sync_exec,
                     "rm": self.remove}

    def connect(self):
        # Try to connect until timeout reached
        start_time = time.time()
        self.connected = False

        while time.time() - start_time < Config.TIMEOUT_RECONNECTING:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.settimeout(2)
            try:
                logging.info(
                    f"Trying to connect to {Config.SERVER}:{Config.PORT}...")
                self.socket.connect((Config.SERVER, Config.PORT))
                self.connected = True
                break
            except Exception as e:
                logging.error(f"{e.args}")
            time.sleep(Config.DELAY_RETRY_CONNECTING)
        if self.connected:
            logging.info(f"Connected to {Config.SERVER}:{Config.PORT}")
        else:
            logging.info(
                f"Could not connect within {Config.TIMEOUT_RECONNECTING}s")

    def exec(self, cmd, args):
        return self.cmds[cmd](args)

    def sync(self, args):
        pass

    def exec(self, args):
        pass

    def sync_exec(self, args):
        pass

    def remove(self, args):
        pass
