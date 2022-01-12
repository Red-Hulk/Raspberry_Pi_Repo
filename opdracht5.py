#Bibliotheken importen GPIO en Time
import RPi.GPIO as GPIO
import time


#Leds verbinden aan poort 5 en 13 en button aan 17
LED_PIN1 = 5
LED_PIN2 = 13
BUTTON_PIN1 = 22
BUTTON_PIN2 = 10

#setupcode voor board, leds, knoppen
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN1, GPIO.OUT)
GPIO.setup(LED_PIN2, GPIO.OUT)
GPIO.setup(BUTTON_PIN1, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(BUTTON_PIN2, GPIO.IN, GPIO.PUD_UP)

#tijd status variabelen
previousMillis1 = 0
previousMillis2 = 0
# Status van lichtjes bijhouden
LED_STATE1 = GPIO.LOW
LED_STATE2 = GPIO.LOW

#methode millis voor tijd
def millis():
    return time.time() * 1000


# variablen om de vertraging in op te slaan
periodA = 1000
periodB = 700
periodC = 1300

while True:

    # statussen van de twee knoppen opvangen
    buttonState1 = GPIO.input(BUTTON_PIN1)
    buttonState2 = GPIO.input(BUTTON_PIN2)

    # tijd starten
    currentMillis = millis()

    # als knop 1 is ingedrukt led 1, 1 seconden aan en 1 seconden uit
    if currentMillis - previousMillis1 > 1000 and buttonState1 == GPIO.LOW:
        #led 2 uitdoen
        GPIO.output(LED_PIN2, GPIO.LOW)
        previousMillis1 = currentMillis
        if LED_STATE1 == GPIO.HIGH:
            GPIO.output(LED_PIN1, GPIO.LOW)
            LED_STATE1 = GPIO.LOW
        else:
            GPIO.output(LED_PIN1, GPIO.HIGH)
            LED_STATE1 = GPIO.HIGH

    # als knop 1 niet is ingedrukt led 1, 1.3 seconden aan en 0.7 seconden uit
    if LED_STATE2 == GPIO.LOW:
        if currentMillis - previousMillis1 > 1300 and buttonState1 == GPIO.HIGH:
                previousMillis1 = currentMillis
                GPIO.output(LED_PIN1, GPIO.HIGH)
                LED_STATE1 = GPIO.HIGH

        if LED_STATE1 == GPIO.HIGH:
            if currentMillis - previousMillis1 > 700 and buttonState1 == GPIO.HIGH:
                previousMillis1 = currentMillis
                GPIO.output(LED_PIN1, GPIO.LOW)
                LED_STATE1 = GPIO.LOW

    #als knop twee is ingedrukt led 2, 0.7 seconden knipperen
    if buttonState2 == GPIO.LOW:
        # led 1 uitdoen
        GPIO.output(LED_PIN1, GPIO.LOW)
        if currentMillis - previousMillis2 > 700:
            previousMillis2 = currentMillis
            if LED_STATE2 == GPIO.HIGH:
                GPIO.output(LED_PIN2, GPIO.LOW)
                LED_STATE2 = GPIO.LOW
            else:
                GPIO.output(LED_PIN2, GPIO.HIGH)
                LED_STATE2 = GPIO.HIGH

    else:
        # led 2 uitdoen
        GPIO.output(LED_PIN2, GPIO.LOW)
        LED_STATE2 = GPIO.LOW

















