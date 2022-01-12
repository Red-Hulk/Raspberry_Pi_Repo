#Bibliotheken importen GPIO en Time
import RPi.GPIO as GPIO
import time

#Leds verbinden aan poort 5 en 13 en button aan 17
LED_PIN1 = 5
LED_PIN2 = 13
BUTTON_PIN = 17

#Setupcode voor board, leds en knop
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN1, GPIO.OUT)
GPIO.setup(LED_PIN2, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN, GPIO.PUD_UP)


while True:
    #knop staat opvangen
    buttonState = GPIO.input(BUTTON_PIN)

    # Als knop is ingedrukt led 1 knippert, opdracht a
    # if buttonState == GPIO.LOW:
    #     GPIO.output(LED_PIN1, GPIO.HIGH)
    # else:
    #     GPIO.output(LED_PIN1, GPIO.LOW)

    # Als knop is ingedrukt led 2 knippert voor 1 seconde aan en 1 seconde uit, opdracht b
    # if buttonState == GPIO.LOW:
    #     GPIO.output(LED_PIN1, GPIO.HIGH)
    #     time.sleep(1)
    #     GPIO.output(LED_PIN1, GPIO.LOW)
    #     time.sleep(1)
    # else:
    #     GPIO.output(LED_PIN1, GPIO.LOW)

    # Als knop is ingedrukt led 1 knippert voor 1.3 seconde aan en 0.7 seconde uit, en led 2 uit opdracht c
    if buttonState == GPIO.LOW:
        GPIO.output(LED_PIN1, GPIO.HIGH)
        time.sleep(1.3)
        GPIO.output(LED_PIN1, GPIO.LOW)
        time.sleep(0.7)
    else:
       GPIO.output(LED_PIN2, GPIO.HIGH)
