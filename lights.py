from time import sleep
import os
import RPi.GPIO as GPIO
import sys

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
GPIO.setwarnings(False)
GPIO.setup(all, GPIO.OUT)
GPIO.output(all, False)
 
try:
    if sys.argv[1] in ['--c','--C','-c','-C','--cylon','--Cylon']:
        include('light_modes/cylon.py')
        
    elif sys.argv[1] in ['--g','--G','-g','-G','--charging','--Charging']:        
        include('light_modes/charging.py')
        
    elif sys.argv[1] in ['--l','--L','-l','-L','--loading','--Loading']:        
        include('light_modes/loading.py')

    elif sys.argv[1] in ['--k','--K','-k','-K','--knight-rider','--Knight-Rider']:
        include('light_modes/knightrider.py')

    elif sys.argv[1] in ['--w','--W','-w','-W','--warning','--Warning']:
        include('light_modes/warning.py')

    elif sys.argv[1] in ['--a','--A','-a','-A','--alert','--Alert']:
        include('light_modes/alert.py')
        
    elif sys.argv[1] in ['--d','--D','-d','-D','--demo','--Demo']:
        include('light_modes/cylon.py')
        include('light_modes/charging.py')
        include('light_modes/loading.py')
        include('light_modes/knightrider.py')
        include('light_modes/warning.py')
        include('light_modes/alert.py')
        
    elif sys.argv[1] in ['--h','--H','-h','-H','--help','--Help']:
        include('light_modes/help.py')
        
    else:
        print 'Unkown parameter. Please use --help for further instructions.'
        exit()
    

except KeyboardInterrupt:
    GPIO.output(all, False)
    GPIO.cleanup()
