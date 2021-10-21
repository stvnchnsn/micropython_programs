import machine
import utime
import _thread

import distance_sensor
import modes
import peripherals

p = peripherals.Peripherals()
p.pin_setup()

party = modes.Party()
seekndestroy = modes.SeeknDestroy()
rest = modes.Rest()

while True:
    
    if p.green_button.value() == 1:
        party.activate()
    if p.red_button.value() == 1:
        seekndestroy.activate()
    if p.blue_button.value() == 1:
        rest.activate()
        
    





