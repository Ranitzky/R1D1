time = 0.3

while i <= 8:
        print "Running alert mode loop:", i
        GPIO.output(all, True)
        sleep(time)
        GPIO.output(all, False)
        sleep(time)
        i = i +1
