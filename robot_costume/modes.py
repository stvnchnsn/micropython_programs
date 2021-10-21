import machine
import utime
import distance_sensor
import peripherals

import led_show
import _thread


class Mode():
    def __init__(self):
        self.p = peripherals.Peripherals()
        self.p.pin_setup()
        pass
    def exit_buttons(self):
        exit_to_menu_buttons = [self.p.green_button.value(),self.p.red_button.value(),self.p.blue_button.value()]
        if sum(exit_to_menu_buttons)==1:
            #self.p.pin_setup()
            return True
class SeeknDestroy(Mode):
    def __init(self):
        super().__init__()
    def activate(self):
        self.p.pin_setup()
        while True:
            if self.exit_buttons() == 1: break
            if self.p.fire_button.value() == True:
                self.p.buzzer.value(1)
                self.p.red_external.value(1)
                self.p.green_external.value(0)
                self.p.blue_external.value(0)
                continue
            elif self.p.fire_button.value() == False:
                self.p.buzzer.value(0)
                self.p.red_external.value(0)
            distance = distance_sensor.ultra()
            # make beep noise constant in seek and destroy mode and increase inversely to distance
            if distance > 1200:
                continue
            if distance > 100:
                led_show.toggle_on_off(self.p.green_external, 0.20)
            if (distance >50) and (distance < 100):
                led_show.toggle_on_off(self.p.blue_external,0.20)
            if distance < 50:
                led_show.toggle_on_off(self.p.red_external,0.10)
                self.p.buzzer.value(1)
                utime.sleep(0.10)
                self.p.buzzer.value(0)
class Party(Mode):
    def __init__(self):
        super().__init__()
    def activate(self):
        i = 0.10 # pot controlled value?
        self.p.pin_setup()
        while True:
            if self.exit_buttons() == 1:
                break
            led_show.toggle_on_off(self.p.led_onboard,i)
            led_show.toggle_on_off(self.p.red_external,i)
            led_show.toggle_on_off(self.p.green_external,i)
            led_show.toggle_on_off(self.p.blue_external,i)

class Rest(Mode):
    def __init_(self):
        super().__init__()
    def activate(self):
        self.p.pin_setup()
        while True:
            if self.exit_buttons() == 1: break
            self.p.green_external.toggle()
            utime.sleep(.5)
        
    