#Bibliotheken importen GPIO en Time en serial
import serial
import time
import RPi.GPIO as GPIO

# leds en knop verbinden aan pinnen
led1 = 19
led2 = 13
button = 6

# setup code voor board en leds en knoppen en waarschuwingen uitzetten
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(button, GPIO.IN, GPIO.PUD_UP)

# variablen om tijd in op te slaan
previousMillis1 = 0
previousMillis2 = 0
# variablen om statussen licht in op te slaan
LED_STATE1 = GPIO.LOW
LED_STATE2 = GPIO.LOW

#methode millis
def millis():
    return time.time() * 1000


# variablen om vertragingen in op te slaan
periodA = 1000
periodB = 3000

# variabel om data op te slaan die verstuurd is door de arduino
line = ""


# verbinden met Arduino
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1.0)
# vertraging voor goede verbinding
time.sleep(3)
# buffer rij om Arduino data te ontvangen
ser.reset_input_buffer()
print("Serial OK")

try:
    while True:
        # tijd starten
        currentMillis = millis()
        # staat van knop opvangen
        buttonState1 = GPIO.input(button)

        # als knop 1 is ingedrukt wissel statussen om
        if (buttonState1 == GPIO.LOW):
            led3 = led1
            led1 = led2
            led2 = led3


        time.sleep(0.01)
        # data opvangen van Arduino
        if ser.in_waiting > 0:
            # data lezen en ontcijferen
            line = ser.readline().decode('utf-8').rstrip()
            print(line)

        # als ontvangen data a is, 1 seconden aan en uit knipperen lichtje 1 en lichtje 2 op andere momenten
        if currentMillis - previousMillis1 > periodA and line == "a":
            GPIO.output(led1, GPIO.LOW)
            previousMillis1 = currentMillis
            if LED_STATE1 == GPIO.HIGH:
                GPIO.output(led1, GPIO.LOW)
                LED_STATE1 = GPIO.LOW
                GPIO.output(led2, GPIO.HIGH)
            else:
                GPIO.output(led1, GPIO.HIGH)
                LED_STATE1 = GPIO.HIGH
                GPIO.output(led2, GPIO.LOW)

        # als ontvangen data b is, 1 seconden lichtje 1 knipperen
        if currentMillis - previousMillis1 > periodA and line == "b":
            # turn down led 1
            GPIO.output(led1, GPIO.LOW)
            previousMillis1 = currentMillis
            if LED_STATE1 == GPIO.HIGH:
                GPIO.output(led1, GPIO.LOW)
                LED_STATE1 = GPIO.LOW
            else:
                GPIO.output(led1, GPIO.HIGH)
                LED_STATE1 = GPIO.HIGH
        # als ontvangen data b is, 3 seconden aan en 3 seconden uit
        if currentMillis - previousMillis2 > periodB and line == "b":
            # turn down led 1
            GPIO.output(led2, GPIO.LOW)
            previousMillis2 = currentMillis
            if LED_STATE2 == GPIO.HIGH:
                GPIO.output(led2, GPIO.LOW)
                LED_STATE2 = GPIO.LOW
            else:
                GPIO.output(led2, GPIO.HIGH)
                LED_STATE2 = GPIO.HIGH


# programma stoppen als keyboard wordt ingedrukt
except KeyboardInterrupt:
    print("Close Serial communication")
    GPIO.output(led1, GPIO.LOW)
    GPIO.output(led2, GPIO.LOW)
    ser.close()