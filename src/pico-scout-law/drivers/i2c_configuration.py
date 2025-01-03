from output_configuration import (OutputConfiguration)
from machine import (SoftI2C, Pin)
from ssd1306 import (SSD1306_I2C)


class I2CConfiguration(OutputConfiguration):
    """A configuration class specific to an I2C display."""

    _sda_pin: Pin
    _scl_pin: Pin

    def __init__(self, sda_pin: Pin, scl_pin: Pin, width: int, height: int):
        """Initializes a new instance of the I2CConfiguration class.
        :param sda_pin: The pin instance used for SDA (Serial Data Line), the bidirectional line used to send and receive data.
        :param scl_pin: The pin instance used for SCL (Serial Clock Line), the line that ensures data is synchronized in the right sequence.
        :param width: The width (in pixels) of the display.
        :param height: The height (in pixels) of the display."""
        OutputConfiguration.__init__(self)
        self.set_size(width, height)
        self._sda_pin = sda_pin
        self._scl_pin = scl_pin
        self._create_display(100_000)

    def set_size(self, width: int, height: int):
        """Sets the size of the display.
        :param width: The width of the display (in pixels).
        :param height: The height of the display (in pixels)."""
        self._res_x = width
        self._res_y = height

    def _create_display(self, frequency: int):
        """Sets up a display instance using the SoftI2C class and modifies internal state for use by other methods.
        :param frequency: The maximum SCL frequency."""
        i2c = SoftI2C(scl=self._scl_pin, sda=self._sda_pin, freq=frequency)
        i2c.scan()
        resolution = self.screen_resolution()
        self._display = SSD1306_I2C(resolution[0], resolution[1], i2c)

    def display(self) -> SSD1306_I2C:
        """Returns the display instance for output manipulation."""
        return self._display
