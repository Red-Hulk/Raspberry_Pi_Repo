//variables off pins
int led1 = 7;
int led2 = 6;
int buttonPin = 3;

//led states
int ledState1 = LOW;
int ledState2 = LOW;
int buttonState = 0;

//Store previous time
long previous1 = 0;
long previous2 = 0;
long previous3 = 0;

//delays
long interval1 = 1000;
long interval2 = 3000;

//determine which to blink
bool oneSec = false;
bool twoSec = false;

void setup() {
  Serial.begin(9600);
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(buttonPin, INPUT);
}

void loop() {

  buttonState = digitalRead(buttonPin);

 unsigned long currentMillis = millis();
  
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

//  if(buttonState == HIGH){
//      int ledState3 = LOW;
//      ledState3 = ledState1;
//      ledState1 = ledState2;
//      ledState2 = ledState3;
//      Serial.print("Hallos");
//      
//    }

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

    //One second each
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

    //One second each
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
