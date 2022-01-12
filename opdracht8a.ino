//pins waar de leds en de knop zijn op aangesloten
int led1 = 7;
int led2 = 6;
int buttonPin = 3;

//de statussen eerst op LOW en 0 zetten
int ledState1 = LOW;
int ledState2 = LOW;
int buttonState = 0;

//Variabelen om tijd in op te slaan
long previous1 = 0;
long previous2 = 0;
long previous3 = 0;

//Variabelen waar de vertraging is opgeslagen
long interval1 = 1000;
long interval2 = 3000;

//bepaal welke led moet knipperen
bool oneSec = false;
bool twoSec = false;

//Setup code van de leds en knop
void setup() {
  Serial.begin(9600);
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(buttonPin, INPUT);
}

void loop() {
  //De staat van de knop opvangen
 buttonState = digitalRead(buttonPin);

  //tijd aftrappen
 unsigned long currentMillis = millis();

 //Check of er data is binnengekomen van de Raspberry
 if(Serial.available() >0){
  String cmd = Serial.readStringUntil('\n');
    if(cmd == "1"){
      oneSec = true;
      twoSec = false;
    }
    else if(cmd == "2"){
      twoSec = true;
      oneSec = false;
    }
    else{
      oneSec = false;
      twoSec = false;
    }
  }

  //Verandere van status van de leds als er op de knop is gedrukt
  if(buttonState == HIGH){
      int ledState3 = LOW;
      ledState3 = ledState1;
      ledState1 = ledState2;
      ledState2 = ledState3;
      Serial.print("Hallos");
      
    }

  //Om de buurt 1 sec aan en 1 sec uit
  if(oneSec == true){

    //One second each
    if(currentMillis - previous1 > interval1){
    previous1 = currentMillis; 
    

     if(ledState1 == LOW){
        ledState1 = HIGH;
        ledState2 = LOW;
      }
     else{
        ledState1 = LOW;
        ledState2 = HIGH;
      }

      digitalWrite(led1, ledState1);
      digitalWrite(led2, ledState2);
    }

  }

  if(twoSec == true){

    //Een seconde knipperen led 1
    if(currentMillis - previous2 > interval1){
    previous2 = currentMillis; 
    

     if(ledState1 == LOW){
        ledState1 = HIGH;  
      }
     else{
        ledState1 = LOW;
      }

      digitalWrite(led1, ledState1);      
    }

    //3 seconden knipperen led 2
    if(currentMillis - previous3 > interval2){
    previous3 = currentMillis; 
    

     if(ledState2 == LOW){
        ledState2 = HIGH;
      }
     else{
        ledState2 = LOW;
      }

      digitalWrite(led2, ledState2);
    }

  }
}
