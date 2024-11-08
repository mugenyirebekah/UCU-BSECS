//The LED on the arduino board was used to help trouble shoot.

//Code with two servo motors

#include <Servo.h>

Servo servo1;  // create servo object to control a servo
Servo servo2;

const int buttonPin = 2;
int buttonState = 0;

const int ledPin = 13;


int pos = 0;    // variable to store the servo position

void setup() {

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
      delay(500);
      digitalWrite(ledPin, LOW);
      delay(500);
    }

  }




}
