import machine
import utime
button = machine.Pin(21, machine.Pin.IN, machine.Pin.PULL_DOWN)
print(button.value())