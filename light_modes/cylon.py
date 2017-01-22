time = 0.2

while i <= 2:
    print "Running Cylon mode loop:", i
    if a <= 0: 
        while a <= amount - 1:
            GPIO.output(gpioPins[a], True)
            GPIO.output(gpioPins[b], False)
            sleep(time)
            a = a + 1
            b = a - 1
    if a == amount:
        a = a - 1
        b = a - 1
        while a > 0:
            GPIO.output(gpioPins[a], False)
            GPIO.output(gpioPins[b], True)
            sleep(time)
            a = a - 1
            b = a - 1
    i = i +1
    GPIO.output(all, False)

