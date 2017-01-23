time = 0.8

while i <= 3:
    print "Running warning mode loop:", i
    while a < amount:
        GPIO.output(gpioPins[a], True)
        GPIO.output(gpioPins[b], False)
        b = a + 1
        a = a + 2
    sleep(time)
    a = 0
    b = 1
    while a < amount:
        GPIO.output(gpioPins[a], False)
        GPIO.output(gpioPins[b], True)
        b = a + 1
        a = a + 2
    sleep(time)
    a = 0
    b = 1
    i = i + 1
GPIO.output(all, False)
