
//Setupcode 
void setup() {
  // put your setup code here, to run once:
  //Begin Serial verbindi
  Serial.begin(9600);
  delay(1000);

  //Dit wordt verstuurd naar de raspberrypi
  Serial.println("Type a or b");
  
  
}

void loop() {

  //vertraging zodat de raspberry genoeg tijd heeft om signaal te ontvangen
  delay(10000);
  // Stuur a naar raspberry
  Serial.println("a");

  delay(20000);
  //Stuur b naar raspberry
  Serial.println("b");
  
}
