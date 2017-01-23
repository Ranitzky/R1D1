time = 0.3
a = middle
b = middle

while i <= 2:
        print "Running Knight Rider mode loop:", i
        if a == 0:
                GPIO.output(gpioPins[a], True)
                GPIO.output(gpioPins[b], True)
                while a < middle:
                        GPIO.output(gpioPins[a], False)
                        GPIO.output(gpioPins[b], False)
                        a = a + 1
                        b = b - 1
                        GPIO.output(gpioPins[a], True)
                        GPIO.output(gpioPins[b], True)
                        sleep(time)
                        
        if a == middle:
                GPIO.output(gpioPins[a], True)
                sleep(time)
                while a > 0:
                        GPIO.output(gpioPins[a], False)
                        GPIO.output(gpioPins[b], False)
                        a = a - 1
                        b = b + 1
                        GPIO.output(gpioPins[a], True)
                        GPIO.output(gpioPins[b], True)
                        sleep(time)

        else:
              GPIO.output(all, False)  
                        
        i = i + 1
        GPIO.output(all, False)
