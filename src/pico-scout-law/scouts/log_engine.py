from scouts import (ConsoleDisplayService)

class LogEngine:
    _display_service: ConsoleDisplayService

    def __init__(self, display_service: ConsoleDisplayService):
        self._display_service = display_service

    def info(self, contents: str):
        self._display_service.set_next(1, contents)

    def debug(self, contents: str):
        self._display_service.set_next(0, contents)

    def warn(self, contents: str):
        self._display_service.set_next(2, contents)

    def error(self, contents: str):
        self._display_service.set_next(3, contents)
