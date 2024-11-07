/*Code: click button - the doors open
        click again - doors close */

#include <Servo.h>
#include <ezButton.h>

Servo servo1;  // create servo object to control a servo
Servo servo2;

const int buttonPin = 2;
int buttonState = 0;
int lastButtonState = 0; // for detecting button state changes
bool doorOpen = false;   // state to keep track of door position

const int ledPin = 13;

int pos = 0;    // variable to store the servo position

void setup() {
  Serial.begin(9600);

  pinMode(ledPin, OUTPUT);
  pinMode(buttonPin, INPUT);

  servo1.attach(9);  
  servo2.attach(8);

  // Initialize servos to closed position
  servo1.write(0);  
  servo2.write(0);
}

void loop() {
  buttonState = digitalRead(buttonPin);

  // Check if the button is pressed (and handle toggle)
  if (buttonState != lastButtonState) { // if button state has changed
    if (buttonState == HIGH) {          // if button is now pressed
      doorOpen = !doorOpen;             // toggle door state
      
      if (doorOpen) {
        Serial.println("Door opening...");
        openDoors();
      } else {
        Serial.println("Door closing...");
        closeDoors();
      }
    }
    delay(50);  // simple debounce
  }

  lastButtonState = buttonState;
}

void openDoors() {
  digitalWrite(ledPin, HIGH);
  
  for (pos = 0; pos <= 180; pos += 1) { // goes from 0 degrees to 180 degrees
    servo1.write(pos);                  // tell servo to go to position in variable 'pos'
    servo2.write(pos);
    delay(15);                          // waits 15ms for the servo to reach the position
  }
}

void closeDoors() {
  digitalWrite(ledPin, LOW);
  
  for (pos = 180; pos >= 0; pos -= 1) { // goes from 180 degrees to 0 degrees
    servo1.write(pos);                  // tell servo to go to position in variable 'pos'
    servo2.write(pos);
    delay(15);                          // waits 15ms for the servo to reach the position
  }
}
