from machine import Pin, Timer
import time
from drivers import (RP2040)
from power import (Battery)
from scouts import (StatusDisplayService, ConsoleDisplayService)


class DisplayEngine:
    """Engine that controls the main logic for display for the scout law project."""

    _battery: Battery
    _display_timer: Timer
    _status_display_service: StatusDisplayService
    _console_display_service: ConsoleDisplayService
    _pico: RP2040
    _charging_pin: Pin | None
    _last_power_state: bool

    def __init__(self, pico: RP2040, battery: Battery, status_display_service: StatusDisplayService, console_display_service: ConsoleDisplayService):
        self._battery = battery
        self._display_timer = Timer()
        self._charging_pin = None #  TODO: This should not be hard-coded here and the variable shouldn't even be known in the display engine.  Need some kind of abstraction for this.
        self._pico = pico
        self._status_display_service = status_display_service
        self._console_display_service = console_display_service
        self._last_power_state = False

    def __init_charging_pin(self):
        """Initializes the charging pin."""
        if (self._charging_pin is None):
            self._charging_pin = Pin(24, Pin.IN)

    def start_render(self):
        self._status_display_service.initialize()
        self._console_display_service.initialize()
        
        self._display_timer.init(period=1000, callback=lambda t:self.render())

    def pause_render(self):
        self._display_timer.deinit()

    def render(self):
        self.__init_charging_pin()

        assert self._charging_pin is not None
        is_charging = self._charging_pin.value() == 1

        self._status_display_service.update_power(is_charging, self._battery)
        self._status_display_service.update_temperature(self._pico.read_temperature())
        self._status_display_service.update_tick()
        self._status_display_service.update_system_info()

        if (is_charging != self._last_power_state):
            message = "Plugged-in"

            if (not is_charging):
                message = "Unplugged"
            
            self._console_display_service.set_next(1, message)
        
        self._status_display_service.refresh()
        self._console_display_service.refresh()
        self._last_power_state = is_charging

charge_status_char = "̅"

    #display_provider.set_line(0, 'Pico Scout Law')

    #charging = Pin(24, Pin.IN)          # reading GP24 tells us whether or not USB power is connected
    #temp = ADC(4)
    #conversion_factor = 3 * 3.3 / 65535

    #full_battery = 4.2                  # these are our reference voltages for a full/empty battery, in volts
    #empty_battery = 3.0                 # the values could vary by battery size/manufacturer so you might need to adjust them
    #display_provider.clear_display()

    #while True:
        #display_provider.clear_display()
        # convert the raw ADC read into a voltage, and then a percentage
        #voltage = vsys.read_u16() * conversion_factor
        #display_provider.text(str(voltage))
        #percentage = 100 * ((voltage - empty_battery) / (full_battery - empty_battery))
        #if percentage > 100:
            #percentage = 100.00
        #display_provider.set_line(1, 'STATUS')
        #display_provider.set_graphic_line(2)
        #if charging.value() == 1:         # if it's plugged into USB power...
            #display_provider.set_line(3, "charging")
        #else:                             # if not, display the battery stats
            #display_provider.set_line(3, (str(voltage) + "v" ))
            #display_provider.set_line(3, ('{:.0f}%'.format(percentage)))

        #display_provider.show_text()
        #display.update()
        #time.sleep(0.5)
        #display_provider.set_line(4, "PWR: " + ('{:.2f}'.format(voltage) + "v-" + ('{:.0f}%'.format(percentage))))
        #display_provider.set_line(5, "TMP: " + str(read_temperature()) + "°F")
        #break


    #display_provider.clear_display()
    #display_provider.show_text()

#
#pix_res_x  = 128 # SSD1306 horizontal resolution
#pix_res_y = 64   # SSD1306 vertical resolution

#i2c_dev = SoftI2C(scl=Pin(17),sda=Pin(16),freq=100_000)  # start I2C on I2C1 (GPIO 26/27)
#i2c_dev.scan()
#i2c_addr = [hex(ii) for ii in i2c_dev.scan()] # get I2C address in hex format
#if i2c_addr==[]:
#    print('No I2C Display Found') 
#    sys.exit() # exit routine if no dev found
#else:
#    print("I2C Address      : {}".format(i2c_addr[0])) # I2C device address
#    print("I2C Configuration: {}".format(i2c_dev)) # print I2C params


#oled = SSD1306_I2C(pix_res_x, pix_res_y, i2c_dev) # oled controller

#oled.write_cmd(0xc0) # flip display to place 0,0 at lower-left corner
#adc_2 = machine.ADC(2) # ADC channel 2 for input
#while True:
#    oled.fill(0) # clear the display
#    for jj in range(pix_res_x): # loop through horizontal display resolution
#        adc_pt = adc_2.read_u16() # read adc and get 16-bit data point
#        plot_pt = (adc_pt/((2**16)-1))*(pix_res_y-1) # convert to OLED pixels
#        oled.text('.',jj,int(plot_pt)) # update x=jj with data point
#    oled.show() # show the new text and image

#data = 'A scout is'
#timer = 2

#oled.text(data, 0, 0, 20)
#oled.invert(1)
#oled.show()
#for t in range(timer):
#    help(oled)
#    oled.scroll(t*-1,0)
#    oled.show()
#    time.sleep(.25)
