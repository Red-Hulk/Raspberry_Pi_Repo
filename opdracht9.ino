//Importen van bibliotheek IRremote
#include <IRremote.h>

//Pin waar de ontvanger is aangesloten
const int RECV_PIN = 7;


//Variabel waarin de data wordt opgeslagen van de remote
unsigned long key_value = 0; 

//counter variabel led
int amountClick = 0;
//counter variabel snelheid
int buttonClick = 0;





//setupcode voor de remote ontvanger en Serial
void setup() {
  Serial.begin(9600); // begin serial communication with a baud rate of 9600
  IrReceiver.begin(RECV_PIN,ENABLE_LED_FEEDBACK);
  
}

void loop() {

  //Data decoden die binnenkomt nadat er op de afstandsbediening is gedrukt
  if (IrReceiver.decode()) {
    key_value = (IrReceiver.decodedIRData.decodedRawData);
    
    delay(500);
    //Naar het volgende signaal gaan
    IrReceiver.resume();

    switch(key_value){
        case 4077715200:
          
          amountClick = amountClick + 1;
          if(amountClick == 1){

            //verstuur Knop1 naar raspberry
              Serial.println("Knop1");
         
            }
          
          if(amountClick == 2){
            buttonClick = 1;
            }
          break;
        case 3877175040:
          
          amountClick = amountClick + 1;
          if(amountClick == 1){
            //verstuur Knop2 naar raspberry
            Serial.println("Knop2");
            }
          
          if(amountClick == 2){
            buttonClick = 2;
            }
          break;
        case 2707357440:
          
          amountClick = amountClick + 1;
          if(amountClick == 1){
            //verstuur Knop3 naar raspberry
            Serial.println("Knop3");
            }
          
          if(amountClick == 2){
            buttonClick = 3;
            }
          break;
        case 4144561920:
          
          amountClick = amountClick + 1;
          if(amountClick == 1){
            //verstuur Knop4 naar raspberry
            Serial.println("Knop4");
            }
          if(amountClick == 2){
            buttonClick = 4;
            }
          
          break;
      }

    if(amountClick == 2){
      switch(buttonClick){
        case 1:
        //verstuur snelheid1 naar raspberry
        Serial.println("snelheid1");
        break;

        case 2:
        //verstuur snelheid2 naar raspberry
        Serial.println("snelheid2");
        break;

        case 3:
        //verstuur snelheid3 naar raspberry
        Serial.println("snelheid3");
        break;

        case 4:
        //verstuur snelheid4 naar raspberry
        Serial.println("snelheid4");
        break;
        }
      }
    if(amountClick == 2){
      amountClick = 0;
      buttonClick = 0;
      }
  }
  
}
