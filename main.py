# from machine import Pin
# from neopixel import NeoPixel

import time
from rotary_irq_esp import RotaryIRQ

r = RotaryIRQ(pin_num_clk=2, 
              pin_num_dt=0, 
              min_val=0, 
              max_val=100, 
              reverse=False, 
              range_mode=RotaryIRQ.RANGE_WRAP)



val_old = r.value()
while True:
    val_new = r.value()
    
    if val_old != val_new:
        val_old = val_new
        print('result =', val_new)
        
    time.sleep_ms(50)





# NEOPIXEL
# pixelCount = 16
# pin = Pin(0, Pin.OUT)   # set GPIO0 to output to drive NeoPixels
# np = NeoPixel(pin, pixelCount)   # create NeoPixel driver on GPIO0 for 64 pixels


# def shiftIndex(i): # wenn das 0 Pixel nicht an der richtigen Stelle ist
#     offset = 8
#     if i + offset < pixelCount:
#         return i + offset
#     else:
#         return i + offset - pixelCount


# def initialFill():
#   for i in range(0, 16):
#     np[shiftIndex(i)]=(0,50,0)
#     np.write()
#     time.sleep_ms(20)    
    

# initialFill()


