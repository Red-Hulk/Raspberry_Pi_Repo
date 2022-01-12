#Bibliotheken importen serial en Time
import serial
import time


# Communiceren met de Arduino
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1.0)
# pauze om verbinding goed op te zetten
time.sleep(3)

# bufferrij waarin data van Arduino wordt gestopt
ser.reset_input_buffer()

print("Serial Ok")

try:
    while True:
        # gebruiker input wordt opgeslagen
        user_input = input("Select '1' or '2':")
        if user_input in ['1', '2']:
            # data opslaan van gebruiker
            str_to_send = user_input + "\n"

            # als de data 1 is
            if user_input == "1":
                # data versturen naar Arduino
                ser.write(str_to_send.encode('utf-8'))
            # als de data 2 is
            elif user_input == "2":
                # data versturen naar Arduino
                ser.write(str_to_send.encode('utf-8'))
            else:
                print("Not the right values")

# programma stoppen als er op keyboard wordt gedrukt
except KeyboardInterrupt:
    print("Close serial communication")
    ser.close()
