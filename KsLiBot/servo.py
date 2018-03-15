import RPi.GPIO as GPIO
from time import sleep

def main():
    # red wire into pin #2, the one coming off of the brown into pin #6, and the one coming out of the yellow wire into pin #3. 
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(03, GPIO.OUT)
    # Now setup PWM on pin #3 at 50Hz
    pwm=GPIO.PWM(03, 50)
    # Then start it with 0 duty cycle so it doesn't set any angles on startup
    pwm.start(0)
    SetAngle(90) 
    pwm.stop()
    GPIO.cleanup()

def SetAngle(angle):
	duty = angle / 18 + 2
	GPIO.output(03, True)
	pwm.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(03, False)
	pwm.ChangeDutyCycle(0)

if __name__ == '__main__':
    main()


# import RPi.GPIO as GPIO
# import time
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(17,GPIO.OUT)
# p=GPIO.PWM(17,50)
# p.start(7.5)
# try:
#         while True:
#                 p.ChangeDutyCycle(7.5)
#                 print "Left"
#                 time.sleep(1)
#                 p.ChangeDutyCycle(12.5)
#                 print "Center"
#                 time.sleep(1)
#                 p.ChangeDutyCycle(2.5)
#                 print "Right"
#                 time.sleep(1)
# except KeyboardInterrupt:
#         p.stop()
#         GPIO.cleanup()