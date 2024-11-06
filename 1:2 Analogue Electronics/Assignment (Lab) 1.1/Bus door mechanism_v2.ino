//Code with two servo motors

#include <Servo.h>
#include <ezButton.h>


Servo servo1;  // create servo object to control a servo
Servo servo2;

const int buttonPin = 2;
int buttonState = 0;

const int ledPin = 13;

ezButton limitSwitch1(7);  
ezButton limitSwitch2(6);  


int pos = 0;    // variable to store the servo position

void setup() {

  Serial.begin(9600);

  limitSwitch1.setDebounceTime(50); 
  limitSwitch2.setDebounceTime(50);

  pinMode(ledPin, OUTPUT);

  pinMode(buttonPin, INPUT);

  servo1.attach(9);  
  servo2.attach(8);


  ////////////////////////////
  servo1.write(0);  
  servo2.write(0);
  delay(1000);

  servo1.write(20);  
  servo2.write(20);

  delay(1000);

  servo1.write(0);  
  servo2.write(0);

  delay(3000);
  
}

void loop() {




  limitSwitch1.loop();
  limitSwitch2.loop();

   limitSwitch1.loop();
  limitSwitch2.loop();
  
  // Check the state of limitSwitch1
  if(limitSwitch1.isPressed()) {
    Serial.println("Limit Switch 1: UNTOUCHED -> TOUCHED");
  }

  if(limitSwitch1.isReleased()) {
    Serial.println("Limit Switch 1: TOUCHED -> UNTOUCHED");
  }

  int state1 = limitSwitch1.getState();
  if(state1 == HIGH) {
    Serial.println("Limit Switch 1: CLOSED DOOR");
  } else {
    Serial.println("Limit Switch 1: OPEN DOOR");
  }

  // Check the state of limitSwitch2
  if(limitSwitch2.isPressed()) {
    Serial.println("Limit Switch 2: UNTOUCHED -> TOUCHED");
  }

  if(limitSwitch2.isReleased()) {
    Serial.println("Limit Switch 2: TOUCHED -> UNTOUCHED");
  }

  int state2 = limitSwitch2.getState();
  if(state2 == HIGH) {
    Serial.println("Limit Switch 2: CLOSED DOOR");
  } else {
    Serial.println("Limit Switch 2: OPEN DOOR");
  }

  buttonState = digitalRead(buttonPin);

  if(buttonState == HIGH){


    digitalWrite(ledPin, HIGH);

  
    for (pos = 0; pos <= 180; pos += 1) { // goes from 0 degrees to 180 degrees
      // in steps of 1 degree
      servo1.write(pos);              // tell servo to go to position in variable 'pos'
      servo2.write(pos);
      delay(15);                       // waits 15ms for the servo to reach the position
    }

    for (pos = 180; pos >= 0; pos -= 1) { // goes from 180 degrees to 0 degrees
      servo1.write(pos);              // tell servo to go to position in variable 'pos'
      servo2.write(pos);
      delay(15);                       // waits 15ms for the servo to reach the position
    }

  }

  else{
    
    for(int i =0; i<4; i++){

      digitalWrite(ledPin, HIGH);
      delay(100);
      digitalWrite(ledPin, LOW);
      delay(100);
    }
 
  }




}
