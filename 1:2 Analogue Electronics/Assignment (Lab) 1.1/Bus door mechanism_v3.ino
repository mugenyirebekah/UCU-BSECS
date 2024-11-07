#include <Servo.h>
#include <ezButton.h>

Servo servo1;
Servo servo2;

const int buttonPin = 2;     // Button pin
const int ledPin = 13;       // LED indicator pin
bool doorState = 0;          // 0 for closed, 1 for open

ezButton limitSwitchOpen(7);   // Limit switch for detecting door fully open
ezButton limitSwitchClose(6);  // Limit switch for detecting door fully closed

void setup() {
  Serial.begin(9600);

  limitSwitchOpen.setDebounceTime(50); 
  limitSwitchClose.setDebounceTime(50);

  pinMode(ledPin, OUTPUT);
  pinMode(buttonPin, INPUT);

  servo1.attach(9);
  servo2.attach(8);

  // Initialize servos to closed position
  servo1.write(0);  
  servo2.write(0);  
  delay(1000);
}

void loop() {
  limitSwitchOpen.loop();
  limitSwitchClose.loop();

  int buttonState = digitalRead(buttonPin);

  // Check if the button is held down
  if (buttonState == HIGH) {
    if (doorState == 0 && !limitSwitchOpen.getState()) {  // Door is closed, start opening
      digitalWrite(ledPin, HIGH);  // LED on, indicating motor is active

      // Move servos to open the door
      for (int pos = 0; pos <= 90; pos++) {
        servo1.write(pos);
        servo2.write(pos);
        delay(15);

        // Stop moving when open limit switch is reached
        if (limitSwitchOpen.isPressed()) {
          doorState = 1;  // Update state to open
          break;
        }
      }
      digitalWrite(ledPin, LOW);  // LED off once fully open
    }
    else if (doorState == 1 && !limitSwitchClose.getState()) {  // Door is open, start closing
      digitalWrite(ledPin, HIGH);  // LED on, indicating motor is active

      // Move servos to close the door
      for (int pos = 90; pos >= 0; pos--) {
        servo1.write(pos);
        servo2.write(pos);
        delay(15);

        // Stop moving when closed limit switch is reached
        if (limitSwitchClose.isPressed()) {
          doorState = 0;  // Update state to closed
          break;
        }
      }
      digitalWrite(ledPin, LOW);  // LED off once fully closed
    }
  }
}
