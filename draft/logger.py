"""
Logging configuration with colorama and logbook
"""

import sys
from typing import Dict

from colorama import Fore, Style, init
from logbook import Logger, LogRecord, StreamHandler

init()  # Initialize colorama


class ColoredFormatter:
    def __init__(self) -> None:
        self.colors: Dict[str, str] = {
            "DEBUG": Fore.CYAN,
            "INFO": Fore.GREEN,
            "WARNING": Fore.YELLOW,
            "ERROR": Fore.RED,
            "CRITICAL": Fore.MAGENTA,
        }

    def format(self, record: LogRecord) -> str:
        color = self.colors.get(record.level_name, "")
        return f"{record.time:%H:%M:%S} {color}[{record.level_name}]{Style.RESET_ALL} {record.message}"


# Create logger
log = Logger("XC8Wrapper")

# Setup handler with custom formatter
handler = StreamHandler(sys.stdout)
formatter = ColoredFormatter()
handler.formatter = lambda record, handler: formatter.format(record)
handler.push_application()
