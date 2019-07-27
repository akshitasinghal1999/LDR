#11 = LED
#21 = LDR

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setwarnings(False)

try:  
    while True:
        
        def LDR1():
            GPIO.setup(21,GPIO.OUT)
            GPIO.output(21,0)
            time.sleep(0.1)
            
            GPIO.setup(21,GPIO.IN)
            c=0
            while GPIO.input(21)==0:
                c+=1
            while GPIO.input(21)==1:
                return c
        
        x = LDR1()
        print(x)

        if x<10000:
            GPIO.output(11,0)
            time.sleep(0.4)
            print("Light")
        else:
            GPIO.output(11,1)
            time.sleep(0.4)
            GPIO.output(11,0)
            print("Dark")
            
except:
    print("Error")
    
finally:
    GPIO.cleanup((11,21))


