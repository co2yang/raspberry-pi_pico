from machine import Timer

timer = Timer(period=2000, callback=lambda t:print('Hello! Pico'))
