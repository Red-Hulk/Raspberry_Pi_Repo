#Bibliotheken importen GPIO en Time
import RPi.GPIO as GPIO
import time

#Led verbonden aan pin 9
LED_PIN = 9

#Setup code voor board en led
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

#methode voor knipper snelheid
def blinkSpeed(x, y):
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(x)
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(y)

while True:
    #1 seconde aan en 1sec uit
    blinkSpeed(1,1)

    #1 seconde aan en 2 seconden uit
    blinkSpeed(1, 2)

    #0.1seconden aan en 0.1seconden uit
    blinkSpeed(0.1, 0.1)

    # 5 seconden aan en 1.5 seconden uit
    blinkSpeed(5, 1.5)




