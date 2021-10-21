import machine
import utime
onboard_led = machine.Pin(25, machine.Pin.OUT)
trigger = machine.Pin(27, machine.Pin.OUT)
echo = machine.Pin(22, machine.Pin.IN)
def ultra():
   trigger.low()
   onboard_led.value(1)
   utime.sleep_us(2)
   trigger.high()
   onboard_led.value(0)
   utime.sleep_us(5)
   trigger.low()
   while echo.value() == 0:
       signaloff = utime.ticks_us()
   while echo.value() == 1:
       signalon = utime.ticks_us()
   timepassed = signalon - signaloff
   distance = (timepassed * 0.0343) / 2
   
   #print("The distance from object is ",distance,"cm")
   return distance
if __name__ == '__main__':
   while True:
       ultra()
       utime.sleep(1)

