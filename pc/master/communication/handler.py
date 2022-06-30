import logging

from .config import Config
from .connection_handler import ConnectionHandler
from .program_handler import ProgramHandler


class Handler:
    def __init__(self):
        self.connection_handler = ConnectionHandler()
        self.program_handler = ProgramHandler()

    def exec(self, cmd, args):
        cmd = cmd.lower()

        # connection typed cmds
        if cmd in self.connection_handler.cmds:
            self.connection_handler.connect()
            if not self.connection_handler.connected:
                return False
            self.connection_handler.exec(cmd, args)
            return True

        # program handler typed cmds
        elif cmd in self.program_handler.cmds:
            return self.program_handler.exec(cmd, args)

        # unknown cmd
        else:
            logging.error("A wrong command was entered")
            return False
