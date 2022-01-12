#Bibliotheken importen GPIO en Time
import RPi.GPIO as GPIO
import time

#knoppen verbinden aan poort 5 en 6 en button aan 17
BUTTON_PIN1 = 5
BUTTON_PIN2 = 6
servoPIN = 17

#setupcode voor board, servo, knoppen
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
GPIO.setup(BUTTON_PIN1, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(BUTTON_PIN2, GPIO.IN, GPIO.PUD_UP)

#GPIO PWM op 50Hz instellen
p = GPIO.PWM(servoPIN, 50)
# start van de servo
p.start(0)


# Methode om de hoek van de servo te berekenen
def SetAngle(angle, sleep):
    duty = angle / 18 + 2
    GPIO.output(servoPIN, True)
    p.ChangeDutyCycle(duty)
    time.sleep(sleep)
    GPIO.output(servoPIN, False)
    p.ChangeDutyCycle(0)

try:
  while True:

    # statussen van de knoppen opvangen
    buttonState1 = GPIO.input(BUTTON_PIN1)
    buttonState2 = GPIO.input(BUTTON_PIN2)

    #counter om te zorgen dat de servo weer terugdraait als hij hoek bereikt heeft
    counter = 0

    # als knop 1 is ingedrukt en knop 2 is ingedrukt
    if buttonState1 == GPIO.LOW and buttonState2 == GPIO.LOW:
        SetAngle(120, 1)
        time.sleep(2)
        SetAngle(0, 1)

    # als knop 1 is ingedrukt tot 90 graden gaan
    elif buttonState1 == GPIO.LOW and counter < 90:
      SetAngle(90, 1)
      counter = counter + 90

    #Hoek 90 graden bereikt ga terug
      if buttonState1 == GPIO.LOW and counter == 90:
            SetAngle(0, 1)
            counter = counter - 90

    # als knop 2 is ingedrukt tot hoek 120 graden
    elif buttonState2 == GPIO.LOW and counter < 120:
        SetAngle(120, 0.5)
        counter = counter + 120
    #als de hoek 120 graden is ga terug
        if buttonState2 == GPIO.LOW and counter == 120:
            SetAngle(0, 0.5)
            counter = counter - 120



# programma stoppen als er op keyboard wordt gedrukt
except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()