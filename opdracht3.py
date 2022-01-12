#Bibliotheken importen GPIO en Time
import RPi.GPIO as GPIO
import time

#Leds verbinden aan pin 9 en pin 10
LED_PIN1 = 9
LED_PIN2 = 10

#loop voor het herhalen van knipperen
loop = [1,2,3]

#Setup code voor board en leds
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN1, GPIO.OUT)
GPIO.setup(LED_PIN2, GPIO.OUT)

#led aan
def ledHigh(x):
    GPIO.output(x, GPIO.HIGH)

#led uit
def ledLow(x):
    GPIO.output(x, GPIO.LOW)

#pauze
def sleep(x):
    time.sleep(x)

#Niet knipperen op dezelfde momenten
def blinkNotAtTheSameTime():
    ledHigh(LED_PIN1)
    sleep(1)
    ledLow(LED_PIN1)
    sleep(1)

    ledHigh(LED_PIN2)
    sleep(1)
    ledLow(LED_PIN2)
    sleep(1)

#knipper methode
def blinkLed(led, x, y):
    GPIO.output(led, GPIO.HIGH)
    time.sleep(x)
    GPIO.output(led, GPIO.LOW)
    time.sleep(y)


while True:
    for x in loop:
        #Knipper voor 1sec en 1sec uit op hetzelfde moment, opdracht a
        ledHigh(LED_PIN1)
        ledHigh(LED_PIN2)
        sleep(1)
        ledLow(LED_PIN1)
        ledLow(LED_PIN2)
        sleep(1)

    for y in loop:
        #Knipper voor 1sec en 1sec uit op niet dezelfde momenten, opdracht a
        blinkNotAtTheSameTime()

    for z in loop:
        # Knipper eerste led voor 1.3 seconden en 0.7 seconden uit, opdracht c
        blinkLed(LED_PIN1, 1.3, 0.7)
        #Led 2 uitdoen
        GPIO.output(LED_PIN2, GPIO.LOW)

    for p in loop:
        # Knipper tweede led voor 0.8 seconden en 1.7 seconden uit, opdracht c
        blinkLed(LED_PIN2, 0.8, 1.7)
        #Led 1 uitdoen
        GPIO.output(LED_PIN1, GPIO.LOW)





