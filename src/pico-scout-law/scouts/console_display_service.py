from providers import (OutputProvider)
from drivers import (RP2040)
import machine


class ConsoleDisplayService:
    """Service class with logic specific to rendering / managing the console / debug display."""

    _output_provider: OutputProvider
    _is_charging: bool
    _controller: RP2040
    _last_log_line: int

    def __init__(self, output_provider: OutputProvider, controller: RP2040):
        """Initializes a new instance of the ConsoleDisplayService class.
        :param output_provider: The output provider that handles low-level display management.
        :param controller: The RP2040 instance used for system functions."""
        self._output_provider = output_provider
        self._is_charging = False
        self._controller = controller
        self._last_log_line = 2

    def initialize(self):
        """Initializes the default setup for the screen / formatting."""
        self._output_provider.set_line(0, 'Debug')
        self._output_provider.set_graphic_line(1)

    def refresh(self):
        """Refreshes the content of the display."""
        self._output_provider.clear_display()
        self._output_provider.show_text()

    def _get_level_text(self, level: int) -> str:
        if (level == 0):
            return "DBG"
        if (level == 1):
            return "INF"
        if (level == 2):
            return "WRN"
        if (level == 3):
            return "ERR"
        return "UNK"

    def set_next(self, level: int, contents: str):
        if (self._last_log_line >= 8):
            self._last_log_line = 2
        
        self._output_provider.set_line(self._last_log_line + 1, "[" + self._get_level_text(level) + "] " + contents)
        self._last_log_line += 1

