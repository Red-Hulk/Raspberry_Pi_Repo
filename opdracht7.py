#Bibliotheken importen GPIO en Time en steppenmotor bibliotheek
import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib
import time

#pins voor steppenmotor, knoppen en stappen
BUTTON_PIN1 = 6
BUTTON_PIN2 = 19
gpioPins = [17, 27, 22, 10]

CCWStep = (0x01,0x02,0x04,0x08)
CWStep = (0x08,0x04,0x02,0x01)

# Laat het systeem weten welk model steppenmotor 28BYJ
motor = RpiMotorLib.BYJMotor("MijnMooieMotor", "28BYJ")

# setup code voor de knoppen en board
GPIO.setup(BUTTON_PIN1, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(BUTTON_PIN2, GPIO.IN, GPIO.PUD_UP)
GPIO.setmode(GPIO.BCM)

def setup():
    print ('Program is starting...')

   #setup code voor de steppenmotor pinnen
    for pin in gpioPins:
        GPIO.setup(pin,GPIO.OUT)

# methode om de steppenmotor te bewegen
def moveOnePeriod(direction,ms):
    for j in range(0,4,1):
        for i in range(0,4,1):  #pin van de steppenmotor aanwijzen
            if (direction == 1):#met de klok mee
                GPIO.output(gpioPins[i],((CCWStep[j] == 1<<i) and GPIO.HIGH or GPIO.LOW))
            else :              #tegen de klok in
                GPIO.output(gpioPins[i],((CWStep[j] == 1<<i) and GPIO.HIGH or GPIO.LOW))
        if(ms<3):       #vertraging van 3miliseconden
            ms = 3
        time.sleep(ms*0.001)

# methode om de steppenmotor te bewegen
def moveSteps(direction, ms, steps):
    for i in range(steps):
        moveOnePeriod(direction, ms)

# methode om de steppen motor te stoppen
def motorStop():
    for i in range(0,4,1):
        GPIO.output(gpioPins[i],GPIO.LOW)

# GPIO opruimen
def destroy():
    GPIO.cleanup()




while True:
    # statussen van de knoppen opvangen
    buttonState1 = GPIO.input(BUTTON_PIN1)
    buttonState2 = GPIO.input(BUTTON_PIN2)
    # variabel om te zorgen dat het systeem eerst reageert op beiden knoppen ingedrukt
    stock = False

    # setup methode oproepen
    setup()

    # als knop 1 en knop 2 is ingedrukt
    if buttonState2 == GPIO.LOW and buttonState1 == GPIO.LOW:
        stock = True
        try:
            moveSteps(1, 5, 512)
            time.sleep(2)
            moveSteps(0, 5, 512)
            time.sleep(0.5)

        except KeyboardInterrupt:
            destroy()

    # als knop 1 is ingedrukt en stock is true
    if buttonState1 == GPIO.LOW and stock == True:
        try:
            moveSteps(0, 5, 512)
            time.sleep(0.5)
        except KeyboardInterrupt:
            destroy()
    # als knop 2 is ingedrukt en stock is true
    if buttonState2 == GPIO.LOW and stock == True:
        try:
            moveSteps(1, 12, 512)
            time.sleep(0.5)
        except KeyboardInterrupt:
            destroy()



