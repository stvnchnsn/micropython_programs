import machine
import utime

import peripherals
p = peripherals.Peripherals()
p.pin_setup()

def toggle_on_off(led,i):
    led.toggle()
    utime.sleep(i)
    led.toggle()
i = 0.10
if __name__ == '__main__':
    while True:
        if p.green_button.value() == 1:
            while p.red_button.value() !=1:
                toggle_on_off(p.led_onboard,i)
                toggle_on_off(p.red_external,i)
                toggle_on_off(p.green_external,i)
                toggle_on_off(p.blue_external,i)
                #p.buzzer.value(1)
                utime.sleep(i)
                #p.buzzer.value(0)
