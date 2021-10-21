import machine

class Peripherals:
    def __ini__(self):
        pass
    def pin_setup(self):
        self.led_onboard = machine.Pin(25, machine.Pin.OUT)
        self.led_onboard.value(0)
        self.red_external = machine.Pin(15, machine.Pin.OUT)
        self.red_external.value(0)
        self.blue_external = machine.Pin(2, machine.Pin.OUT)
        self.blue_external.value(0)
        self.green_external = machine.Pin(14, machine.Pin.OUT)
        self.green_external.value(0)
        
        self.green_button = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_DOWN)
        self.red_button = machine.Pin(6, machine.Pin.IN, machine.Pin.PULL_DOWN)
        self.fire_button = machine.Pin(28, machine.Pin.IN, machine.Pin.PULL_DOWN)
        self.blue_button = machine.Pin(21, machine.Pin.IN, machine.Pin.PULL_DOWN)
        
        self.buzzer = machine.Pin(10, machine.Pin.OUT)
        self.buzzer.value(0)
    def distance_sensor(self):
        '''to add distance sensor here'''
        pass
    def exit_buttons(self):
        pass
