class OutputConfiguration:
    """A basic class used to store configuration options for an output display.  Allows for general configuration for multiple display sizes / types."""

    def __init__(self, screen_type:str="ssd1306", control_type:str="i2c", line_height:int=8):
        """Initializes a new instance of the OutputConfiguration class.
        :param screen_type: The type of screen, for example ssd1306.
        :param control_type: The interface for controlling the display (i2c, spi, etc.).
        :param line_height: A default line height in pixels for text / display lines on a display where lines are used.  Defaults to 8px."""
        self._type = screen_type
        self._control_type = control_type
        self._res_x = 128
        self._res_y = 64
        self._line_height_px = line_height

    def screen_type(self) -> str:
        """Returns the screen type."""
        return self._type

    def control_type(self) -> str:
        """Returns the type of control interface used for the display."""
        return self._control_type

    def screen_resolution(self) -> tuple[int, int]:
        """Returns a tuple with the width x height resolution of the display."""
        return (self._res_x, self._res_y)

    def line_height_px(self) -> int:
        """Returns the line height for the display."""
        return self._line_height_px
