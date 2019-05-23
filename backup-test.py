import webiopi
import datetime
 
GPIO = webiopi.GPIO
 
IN1 = 4 # GPIO pin using BCM numbering
IN2 = 17

HOUR_ON  = 8  # Turn Light ON at 08:00
HOUR_OFF = 18 # Turn Light OFF at 18:00
 
# setup function is automatically called at WebIOPi startup
def setup():
    # set the GPIO used by the light to output
	GPIO.setFunction(IN1, GPIO.OUT)
	GPIO.setFunction(IN2, GPIO.OUT)
 
    # retrieve current datetime
    #now = datetime.datetime.now()
 
    # test if we are between ON time and turn the light ON
	#if ((now.hour >= HOUR_ON) and (now.hour < HOUR_OFF)):
	GPIO.digitalWrite(IN1, GPIO.HIGH)
	GPIO.digitalWrite(IN2, GPIO.HIGH)
 
# loop function is repeatedly called by WebIOPi 
def loop():
    # retrieve current datetime
    #now = datetime.datetime.now()
 
    # toggle light ON all days at the correct time
    #if ((now.hour == HOUR_ON) and (now.minute == 0) and (now.second == 0)):
	if (GPIO.digitalRead(IN1) == GPIO.LOW):
		GPIO.digitalWrite(IN1, GPIO.HIGH)
		GPIO.digitalWrite(IN2, GPIO.LOW)
 
    # toggle light OFF
    #if ((now.hour == HOUR_OFF) and (now.minute == 0) and (now.second == 0)):
	if (GPIO.digitalRead(IN1) == GPIO.HIGH):
		GPIO.digitalWrite(IN1, GPIO.LOW)
		GPIO.digitalWrite(IN2, GPIO.HIGH)
 
    # gives CPU some time before looping again
	webiopi.sleep(1)
 
# destroy function is called at WebIOPi shutdown
def destroy():
	GPIO.digitalWrite(IN1, GPIO.LOW)
	GPIO.digitalWrite(IN2, GPIO.LOW)
