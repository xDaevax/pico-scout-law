from providers import (OutputProvider)
from power import (Battery)
from drivers import (RP2040)
import machine


class StatusDisplayService:
    """Service class with logic specific to rendering / managing the status display."""

    _output_provider: OutputProvider
    _is_charging: bool
    _controller: RP2040

    def __init__(self, output_provider: OutputProvider, controller: RP2040):
        """Initializes a new instance of the StatusDisplayService class.
        :param output_provider: The output provider that handles low-level display management.
        :param controller: The RP2040 instance used for system functions."""
        self._output_provider = output_provider
        self._is_charging = False
        self._controller = controller

    def initialize(self):
        """Initializes the default setup for the screen / formatting."""
        self._output_provider.set_line(0, 'Pico Scout Law')
        self._output_provider.set_line(1, 'Status')
        self._output_provider.set_graphic_line(2)

    def refresh(self):
        """Refreshes the content of the display."""
        self._output_provider.clear_display()
        self._output_provider.show_text()

    def update_battery(self, battery_status: Battery):
        """Updates the battery display on the screen.
        :param battery_status: The battery information used to display status."""
        self._output_provider.set_line(3, "PWR: " + ('{:.2f}'.format(battery_status.convert_voltage(self._controller.read_input_voltage())) + "v-" + ('{:.0f}%'.format(battery_status.remaining_charge_percent(self._controller.read_input_voltage())))))

    def update_charging(self, battery_status: Battery):
        """Updates the charging display on the screen.
        :param battery_status: The battery information used to display status."""
        self._output_provider.set_line(3, "PWR: " + ('{:.2f}'.format(battery_status.convert_voltage(self._controller.read_input_voltage())) + "v- chg"))

    def update_power(self, is_charging: bool, battery_status: Battery):
        """Updates the display of the power information.
        :param is_charging: True to indicate the battery is charging / running on external power.
        :param battery_status: The Battery instance for displaying battery / internal power information."""
        
        if is_charging:
            self.update_charging(battery_status)
        else:
            self.update_battery(battery_status)

    def update_temperature(self, temp_value: float):
        """Updates the temperature display with the given value.
        :param temp_value: The RP2040 temperature reading (expects fahrenheit)."""
        self._output_provider.set_line(4, "TMP: " + str(temp_value) + "°F")

    def _zero_prefix(self, value: int) -> str:
        """Prefixes the given integer with a zero IF only a single digit is present.
        :param value: The integer to zero-prefix."""
        if (len(str(value)) >= 2):
            return str(value)[-2:]
        else:
            return (str("0") + str(value))

    def _format_time(self, hour: int, minute: int, second: int) -> str:
        """Returns the formatted, normalized time with zero-prefixes.
        :param hour: The hour value of the time.
        :param minute: The minute value of the time.
        :param second: The second value of the time."""
        return ":".join([self._zero_prefix(hour), self._zero_prefix(minute), self._zero_prefix(second)])

    def update_tick(self):
        """Updates the time since start (or if an RTC is equipped, uses the current time)."""
        #  TODO: Would be nice to abstract this away
        local_time = machine.RTC().datetime()
        self._output_provider.set_line(5, self._format_time(local_time[4], local_time[5], local_time[6]))

    def update_system_info(self):
        """Updates the basic system information."""
        system_info = self._controller.read_system_info()

        self._output_provider.set_line(6, ", ".join([system_info[0], system_info[1]]))