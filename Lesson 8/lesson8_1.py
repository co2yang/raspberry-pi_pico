from machine import Pin
from time import sleep

led_pin = LED
led = Pin(led_pin, Pin.OUT)

while(True):
    led.toggle()
    sleep(0.5)
