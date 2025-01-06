# Brings in the additional modules so MicroPython can find them

from machine import (Pin)
from drivers import (RP2040, I2CConfiguration)
from providers import (OutputProvider)
from power import (Battery)
from scouts import (DisplayEngine, StatusDisplayService, ConsoleDisplayService, LogEngine)
#  INFO: configure these values according to the specifics of your build.

def build_dependencies() -> tuple[RP2040, DisplayEngine, LogEngine]:
    """Builds all of the instances of types that control the behavior of the system.  Returns those that require immediate control by the main code as a tuple instance."""
    # Default implementation for Raspberry PI Pico.  You can create a new class that derives from RP2040 for a different micro-controller and use it here.
    pi = RP2040()

    # Use this to adjust the battery settings for your use.  Full charge, empty charge voltage, discharge rate, etc.. for working with power management.
    battery = Battery('Adafruit Industries', 'ICR18650')

    # Change this to SPI or a different hardware interface.  PINS below can be adjusted to your SDA / SCL pinouts / screen size
    status_output_config = I2CConfiguration(Pin(16), Pin(17), 128, 64)
    console_output_config = I2CConfiguration(Pin(15), Pin(14), 128, 64)

    # (Low-level) Swap this out if you need to change how contents are buffered to the display(s).
    status_output_provider = OutputProvider(status_output_config)
    console_output_provider = OutputProvider(console_output_config)

    # Service that handles scout-specific logic for driving the status screen, change to adjust what is shown.
    status_service = StatusDisplayService(status_output_provider, pi)
    console_service = ConsoleDisplayService(console_output_provider, pi)
    log_engine = LogEngine(console_service)

    # Can be swapped out to drive the two display's differently.
    display_engine = DisplayEngine(pi, battery, status_service, console_service)

    return (pi, display_engine, log_engine)