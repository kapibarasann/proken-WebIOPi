import webiopi
GPIO = webiopi.GPIO

IN1 = 2
IN2 = 3
IN3 = 4
IN4 = 17

left = [IN2, IN1]
right = [IN3, IN4]

def setup():
	GPIO.setFunction(IN1, GPIO.OUT)
	GPIO.setFunction(IN2, GPIO.OUT)
	GPIO.setFunction(IN3, GPIO.OUT)
	GPIO.setFunction(IN4, GPIO.OUT)

def loop():
	webiopi.sleep(0.1)

def destroy():
	GPIO.digitalWrite(IN1, GPIO.LOW)
	GPIO.digitalWrite(IN2, GPIO.LOW)
	GPIO.digitalWrite(IN3, GPIO.LOW)
	GPIO.digitalWrite(IN4, GPIO.LOW)

@webiopi.macro
def stop():
	GPIO.digitalWrite(left[0], GPIO.LOW)
	GPIO.digitalWrite(left[1], GPIO.LOW)
	GPIO.digitalWrite(right[0], GPIO.LOW)
	GPIO.digitalWrite(right[1], GPIO.LOW)

@webiopi.macro
def forward():
	GPIO.digitalWrite(left[0], GPIO.HIGH)
	GPIO.digitalWrite(left[1], GPIO.LOW)
	GPIO.digitalWrite(right[0], GPIO.HIGH)
	GPIO.digitalWrite(right[1], GPIO.LOW)

@webiopi.macro
def back():
	GPIO.digitalWrite(left[0], GPIO.LOW)
	GPIO.digitalWrite(left[1], GPIO.HIGH)
	GPIO.digitalWrite(right[0], GPIO.LOW)
	GPIO.digitalWrite(right[1], GPIO.HIGH)

@webiopi.macro
def left_rot():
	GPIO.digitalWrite(left[0], GPIO.LOW)
	GPIO.digitalWrite(left[1], GPIO.HIGH)
	GPIO.digitalWrite(right[0], GPIO.HIGH)
	GPIO.digitalWrite(right[1], GPIO.LOW)

@webiopi.macro
def right_rot():
	GPIO.digitalWrite(left[0], GPIO.HIGH)
	GPIO.digitalWrite(left[1], GPIO.LOW)
	GPIO.digitalWrite(right[0], GPIO.LOW)
	GPIO.digitalWrite(right[1], GPIO.HIGH)

