time = 1

while i <= 1:
        print "Running charging mode loop:", i
        while a <= amount - 1:
                GPIO.output(gpioPins[a], True)
                sleep(time)
                a = a + 1
        a = 0
        GPIO.output(all, False)
        sleep(time)
        i = i +1
