#Bibliotheken importen GPIO en Time en serial
import serial
import time
import RPi.GPIO as GPIO

# leds en knop verbinden aan pinnen
led1 = 13
led2 = 19
led3 = 5
led4 = 11

# variabel om data van Arduino in te stoppen
line=""

# setup code voor board en leds en waarschuwingen uitzetten
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)
GPIO.setup(led4, GPIO.OUT)

# variabelen om tijd in op te slaan
previousMillis1 = 0
previousMillis2 = 0
previousMillis3 = 0
previousMillis4 = 0

# de initiele led statussen
LED_STATE1 = GPIO.LOW
LED_STATE2 = GPIO.LOW
LED_STATE3 = GPIO.LOW
LED_STATE4 = GPIO.LOW

# variabelen om de vertraging in op te slaan
periodA = 1000
periodB = 700
periodC = 500
periodD = 300

# variabelen om te bepalen welk lichtjes er moeten branden
staat1 = 0
staat2 = 0
staat3 = 0
staat4 = 0

# snelheid van het knipperen opslaan
snelheid1 = 0
snelheid2 = 0
snelheid3 = 0
snelheid4 = 0

# variabelen om te gebruiken in millis methode
test1 = 0
test2 = 0
test3 = 0
test4 = 0

# variabelen om led in op te slaan
testlicht1 = 0
testlicht2 = 0
testlicht3 = 0
testlicht4 = 0

# counter om ervoor te zorgen dat statussen 1 keer op nul worden gezet
blink = 0

# methode millis voor tijd
def millis():
    return time.time() * 1000

# methode om alle leds uit te zetten
def ledoff():
    GPIO.output(led1, GPIO.LOW)
    GPIO.output(led2, GPIO.LOW)
    GPIO.output(led3, GPIO.LOW)
    GPIO.output(led4, GPIO.LOW)



# verbinding maken met de Arduino
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1.0)
# vertraging zodat de data van de Arduino goed kunnen worden ontvangen
time.sleep(3)
# een buffer waar de data van de Arduino terecht komt
ser.reset_input_buffer()
print("Serial OK")

try:
    while True:
        # tijd aftrappen
        currentMillis = millis()


        time.sleep(0.01)
        # check of er data van Arduino is ontvangen
        if ser.in_waiting > 0:
            # decode de data van de Arduino
            line = ser.readline().decode('utf-8').rstrip()
            print(line)

        # verander variabelen naderhand van welke data er is gestuurd
        if line == "Knop1":
            staat1 = 1
        if line == "Knop2":
            staat2 = 2
        if line == "Knop3":
            staat3 = 3
        if line == "Knop4":
            staat4 = 4

        # verander variabelen snelheid naderhand van welke data er is gestuurd
        if line == "snelheid1":
            snelheid1 = 1
        if line == "snelheid2":
            snelheid2 = 2
        if line == "snelheid3":
            snelheid3 = 3
        if line == "snelheid4":
            snelheid4 = 4


        if staat1 == 1:
            # zet alles weer op nul
            if blink == 0:
                staat2 = 0
                staat3 = 0
                staat4 = 0
                snelheid1 =0
                snelheid2 = 0
                snelheid3 = 0
                snelheid4 = 0
                blink = blink + 1

            # andere leds uitdoen
            GPIO.output(led2, GPIO.LOW)
            GPIO.output(led3, GPIO.LOW)

            if snelheid1 == 1:
                test1 = periodA
                testlicht1 = led1

            if snelheid2 == 2:
                test1 = periodB
                testlicht1 = led1


            if snelheid3 == 3:
                test1 = periodC
                testlicht1 = led1


            if snelheid4 == 4:
                test1 = periodD
                testlicht1 = led1


            if test1 > 0:

                if currentMillis - previousMillis1 > test1:
                    previousMillis1 = currentMillis
                    if LED_STATE1 == GPIO.HIGH:
                        GPIO.output(testlicht1, GPIO.LOW)
                        LED_STATE1 = GPIO.LOW
                        GPIO.output(led4, GPIO.LOW)
                    else:
                        GPIO.output(testlicht1, GPIO.HIGH)
                        LED_STATE1 = GPIO.HIGH
                        GPIO.output(led4, GPIO.HIGH)



        if staat2 == 2:
            # zet alles weer op nul
            if blink == 1:
                staat1 = 0
                staat3 = 0
                staat4 = 0
                snelheid1 = 0
                snelheid2 = 0
                snelheid3 = 0
                snelheid4 = 0
                blink = blink + 1

            GPIO.output(led1, GPIO.LOW)
            GPIO.output(led3, GPIO.LOW)

            if snelheid1 == 1:
                test2 = periodA
                testlicht2 = led2

            if snelheid2 == 2:
                test2 = periodB
                testlicht2 = led2

            if snelheid3 == 3:
                test2 = periodC
                testlicht2 = led2

            if snelheid4 == 4:
                test2 = periodD
                testlicht2 = led2

            if test2 > 0:
                if currentMillis - previousMillis1 > test1:
                    previousMillis1 = currentMillis
                    if LED_STATE1 == GPIO.HIGH:
                        GPIO.output(testlicht2, GPIO.LOW)
                        LED_STATE1 = GPIO.LOW
                        GPIO.output(led4, GPIO.LOW)

                    else:
                        GPIO.output(testlicht2, GPIO.HIGH)
                        LED_STATE1 = GPIO.HIGH
                        GPIO.output(led4, GPIO.HIGH)



        if staat3 == 3:
            if blink == 2:
                staat1 = 0
                staat2 = 0
                staat4 = 0
                snelheid1 = 0
                snelheid2 = 0
                snelheid3 = 0
                snelheid4 = 0
                blink = blink + 1

            GPIO.output(led1, GPIO.LOW)
            GPIO.output(led2, GPIO.LOW)

            if snelheid1 == 1:
                test3 = periodA
                testlicht3 = led3

            if snelheid2 == 2:
                test3 = periodB
                testlicht3 = led3

            if snelheid3 == 3:
                test3 = periodC
                testlicht3 = led3

            if snelheid4 == 4:
                test3 = periodD
                testlicht3 = led3

            if test3 > 0:
                if currentMillis - previousMillis1 > test1:
                    previousMillis1 = currentMillis
                    if LED_STATE1 == GPIO.HIGH:
                        GPIO.output(testlicht3, GPIO.LOW)
                        LED_STATE1 = GPIO.LOW
                        GPIO.output(led4, GPIO.LOW)

                    else:
                        GPIO.output(testlicht3, GPIO.HIGH)
                        LED_STATE1 = GPIO.HIGH
                        GPIO.output(led4, GPIO.HIGH)



        if staat4 == 4:
            # zet alles weer op nul
            if blink == 3:
                staat1 = 0
                staat2 = 0
                staat3 = 0
                snelheid1 = 0
                snelheid2 = 0
                snelheid3 = 0
                snelheid4 = 0
                blink = blink + 1

            GPIO.output(led1, GPIO.LOW)
            GPIO.output(led3, GPIO.LOW)

            if snelheid1 == 1:
                test4 = periodA
                testlicht4 = led4

            if snelheid2 == 2:
                test4 = periodB
                testlicht4 = led4

            if snelheid3 == 3:
                test4 = periodC
                testlicht4 = led4

            if snelheid4 == 4:
                test4 = periodD
                testlicht4 = led4

            if test4 > 0:
                if currentMillis - previousMillis1 > test1:
                    previousMillis1 = currentMillis
                    if LED_STATE1 == GPIO.HIGH:
                        GPIO.output(testlicht4, GPIO.LOW)
                        LED_STATE1 = GPIO.LOW
                        GPIO.output(led2, GPIO.LOW)

                    else:
                        GPIO.output(testlicht4, GPIO.HIGH)
                        LED_STATE1 = GPIO.HIGH
                        GPIO.output(led2, GPIO.HIGH)





# programma stoppen als er op de keyboard wordt gedrukt
except KeyboardInterrupt:
    print("Close Serial communication")
    GPIO.output(led1, GPIO.LOW)
    GPIO.output(led2, GPIO.LOW)
    GPIO.output(led3, GPIO.LOW)
    GPIO.output(led4, GPIO.LOW)
    ser.close()