class OutputLine:
    """Class used to store a line of text to display on an output."""

    def __init__(self, x_pos: int, y_pos: int, text: str = '', graphic: tuple[int, int] = (0, 0)):
        """Initializes a new instance of the OutputLine class."""
        self._x_pos = x_pos
        self._y_pos = y_pos
        self._text = text
        self._graphic = graphic

    @property
    def x_pos(self) -> int:
        """Gets the x position of the line."""
        return self._x_pos

    @property
    def y_pos(self) -> int:
        """Gets the y position of the line."""
        return self._y_pos

    @property
    def text(self) -> str:
        """Gets the text displayed on the line."""
        return self._text

    @text.setter
    def text(self, value: str):
        """Sets the text for the line."""
        self._text = value

    @property
    def graphic(self) -> tuple[int, int]:
        """Gets the graphic to show on the line"""
        return self._graphic

    @graphic.setter
    def graphic(self, value: tuple[int, int]):
        """Sets the graphic"""
        self._graphic = value
