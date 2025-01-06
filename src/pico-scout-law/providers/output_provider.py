from providers.output_line import (OutputLine)

class OutputProvider:
    """Class that provides output line management.  Simplifies the process of adding / updating individual lines on the display."""
    _lines: list[OutputLine]

    def __init__(self, configuration):
        """Initializes a new instance of the OutputProvider class.
        :param configuration: The OutputConfiguration instance used to configure the provider behavior."""
        self._configuration = configuration
        self._lines = list()

    def clear_display(self):
        """Clears the contents of the display."""
        self._configuration.display().fill(0)

    def get_last_line(self):
        """Returns the current line that is highest in the buffer."""
        return len(self._lines) - 1

    def set_graphic_line(self, index: int):
        """Draws a horizontal line"""
        if self._line_exists(index):
            print("exists: " + str(index))

            for line in range(len(self._lines)):
                if line == index:
                    self._lines[index].graphic = (self._configuration.screen_resolution()[0], 1)
                    self._lines[index].text = ""
                    break
        else:
            if self._can_add_line(index):
                new_index = 0

                if len(self._lines) > 0:
                    new_index = len(self._lines)

                print(new_index)
                new_line = OutputLine(0, new_index*9, "", (self._configuration.screen_resolution()[0], 1))
                self._lines.append(new_line)
            else:
                print("Can't add")

    def show_text(self):
        """Displays the text lines on the display.  Use this method when you want to actually update what is displayed on screen."""
        for line in self._lines:
            if line.text == "":
                self._configuration.display().hline(line.x_pos, line.y_pos, line.graphic[0], line.graphic[1])
                print(line.graphic)
            else:
                self._configuration.display().text(line.text, line.x_pos, line.y_pos, 1)
        self._configuration.display().show()

    def _line_exists(self, index: int) -> bool:
        """For internal use; Determines whether the given index line exists in the provider cache.
        :param index: The index to check."""
        if index < 0:
            return False

        return index < len(self._lines)

    def _can_add_line(self, index: int) -> bool:
        """For internal use; Determines whether the given index can be added (has to be a positive integer).
        :param index: The index being checked for add."""
        return index >= 0

    def set_line(self, index: int, text: str):
        """Sets the value of a line but doesn't update the display itself.  Call the show_text() method to update what is shown on the display after calling set_line().
        :param index: The index of the message to update.
        :param text: The new text value for that line."""
        if self._line_exists(index):
            print("exists: " + str(index))

            for line in range(len(self._lines)):
                if line == index:
                    self._lines[index].text = text
                    #  TODO: This is clunky, we need a better abstraction for determining the difference between a text line and a graphic line / lines.
                    self._lines[index].graphic = (0, 0)
                    break
        else:
            if self._can_add_line(index):
                new_index = 0

                if len(self._lines) > 0:
                    new_index = len(self._lines)

                print (new_index)
                #  TODO: Calculate the new line height based on config and / or font
                new_line = OutputLine(0, (new_index * 9), text)
                self._lines.append(new_line)
            else:
                print("Can't add")
