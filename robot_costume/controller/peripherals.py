import machine
import utime
class Peripherals:
    def __ini__(self):
        pass
    def pin_setup(self):
        # LEDs
        self.led_onboard = machine.Pin(25, machine.Pin.OUT)
        self.led_onboard.value(0)
        self.red_external = machine.Pin(15, machine.Pin.OUT)
        self.red_external.value(0)
        self.blue_external = machine.Pin(2, machine.Pin.OUT)
        self.blue_external.value(0)
        self.green_external = machine.Pin(14, machine.Pin.OUT)
        self.green_external.value(0)
        # Buttons
        self.green_button = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_DOWN)
        self.red_button = machine.Pin(6, machine.Pin.IN, machine.Pin.PULL_DOWN)
        self.fire_button = machine.Pin(28, machine.Pin.IN, machine.Pin.PULL_DOWN)
        self.blue_button = machine.Pin(5, machine.Pin.IN, machine.Pin.PULL_DOWN)
        # Buzzer
        self.buzzer = machine.Pin(10, machine.Pin.OUT)
        self.buzzer.value(0)
        # Distance Sensor
        self.trigger = machine.Pin(27, machine.Pin.OUT)
        self.echo = machine.Pin(22, machine.Pin.IN)
    def distance_sensor(self):
        '''to add distance sensor here'''
        
        self.trigger.low()
        utime.sleep_us(2)
        self.trigger.high()
        utime.sleep_us(5)
        self.trigger.low()
        while self.echo.value() == 0:
            signaloff = utime.ticks_us()
        while self.echo.value() == 1:
           signalon = utime.ticks_us()
        timepassed = signalon - signaloff
        distance = (timepassed * 0.0343) / 2
   
        #print("The distance from object is ",distance,"cm")
        return distance
    def exit_buttons(self):
        pass
