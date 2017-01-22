from time import sleep
import os
import RPi.GPIO as GPIO

def include(filename):
    if os.path.exists(filename): 
        execfile(filename)
        

# define leds on GPIO
all = (03,05,07,11,13,15,19,21,23)
gpioPins = [03,05,07,11,13,15,19,21,23]

i = 0
a = 0
b = 1

# get the max number of leds
amount = len(gpioPins)

# get the middle of the led bar to start
middle = len(gpioPins) // 2
    
GPIO.setmode(GPIO.BOARD)
GPIO.setup(all, GPIO.OUT)
GPIO.output(all, False)

# ask user for light mode
print '\n\n======\n\033[1;32mMode\033[1;m\n======\n'
print '\033[1;31mC\033[1;mylon\n'
print 'C\033[1;31mh\033[1;marging\n'
print '\033[1;31mL\033[1;moading \n'
print '\033[1;31mK\033[1;mnight Rider\n'
print '\033[1;31mD\033[1;memo\n'
question = raw_input("Please select: ")

# handle different possible user ansers and set timings for lights                              
if question in ['c', 'C', 'cylon', 'Cylon']:
    mode = 'cylon'
elif question in ['l', 'L', 'loading' , 'Loading']:
    mode = 'loading'
elif question in ['k', 'K', 'knight rider' , 'Knight Rider']:
    mode = 'knightrider'
elif question in ['h', 'H', 'charging', 'Charging']:
    mode = 'charging'
elif question in ['d', 'D', 'demo', 'Demo']:
    mode = 'demo'
else:
    print 'Unkown option'
    exit()
 
try:
    if mode in ['cylon']:
        include('light_modes/cylon.py')
            
    elif mode in ['charging']:
        include('light_modes/charging.py')
            
    elif mode in ['loading']:
        include('light_modes/loading.py')

    elif mode in ['knightrider']:
        include('light_modes/knightrider.py')

    elif mode in ['demo']:
        include('light_modes/cylon.py')
        include('light_modes/charging.py')
        include('light_modes/loading.py')
        include('light_modes/knightrider.py')
    

except KeyboardInterrupt:
    GPIO.output(all, False)
    GPIO.cleanup()
