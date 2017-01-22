time = 0.3

while i <= 1:
        print "Running loading mode loop:", i
        while a <= amount - 1:
                GPIO.output(gpioPins[a], True)
                sleep(time)
                GPIO.output(gpioPins[a], False)
                a = a +1
        a = 0
        i = i + 1
        GPIO.output(all, False)
        
