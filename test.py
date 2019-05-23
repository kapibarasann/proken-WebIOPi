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
 
# loop function is repeatedly called by WebIOPi 
def loop():
	webiopi.sleep(0.1)

@webiopi.macro
def stop():
	GPIO.digitalWrite(IN1, GPIO.LOW)
	GPIO.digitalWrite(IN2, GPIO.LOW)

@webiopi.macro
def forward():
        GPIO.digitalWrite(IN1, GPIO.HIGH)
        GPIO.digitalWrite(IN2, GPIO.LOW)
 
# destroy function is called at WebIOPi shutdown
def destroy():
	GPIO.digitalWrite(IN1, GPIO.LOW)
	GPIO.digitalWrite(IN2, GPIO.LOW)
