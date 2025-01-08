import shared


class Battery:
    """Used to represent the battery characteristics for the system."""
    _manufacturer: str
    _model: str
    _c_rate_charge: float
    _full_v: float
    _empty_v: float
    _c_rate_discharge: float

    def __init__(self, manufacturer: str = '', model: str = '', charge_rate: float = 0.56, full_v: float = 4, empty_v: float = 3, discharge_rate: float = 0.2):
        self._manufacturer = manufacturer
        self._model = model
        self._c_rate_charge = charge_rate
        self._full_v = full_v
        self._empty_v = empty_v
        self._c_rate_discharge = discharge_rate

    @staticmethod
    def _conversion_factor() -> float:
        """Calculates the conversion factor of the voltage"""
        return 3 * 3.3 / shared.constants.MAX_ADC

    @staticmethod
    def convert_voltage(raw_voltage: float) -> float:
        """Calculates the voltage in decimal using a conversion factor.
        :param raw_voltage: The raw voltage reading to convert."""
        return raw_voltage * Battery._conversion_factor()

    def remaining_charge_percent(self, raw_voltage: float) -> float:
        """Calculates the remaining charge of the battery based on the given raw voltage.
        :param raw_voltage: The raw voltage of the battery used in the calculation."""
        return_value = 100 * ((Battery.convert_voltage(raw_voltage) - self._empty_v) / (self._full_v - self._empty_v))

        if return_value > 100:
            return_value = 100.00

        return return_value
