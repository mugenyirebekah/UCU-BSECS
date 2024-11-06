#include <ezButton.h>

ezButton limitSwitch1(7);  
ezButton limitSwitch2(6);  

void setup() {
  Serial.begin(9600);
  
  // Set debounce time for both limit switches
  limitSwitch1.setDebounceTime(50); 
  limitSwitch2.setDebounceTime(50); 
}

void loop() {
  // Call the loop() method for both switches
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
    Serial.println("Limit Switch 1: UNTOUCHED");
  } else {
    Serial.println("Limit Switch 1: TOUCHED");
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
    Serial.println("Limit Switch 2: UNTOUCHED");
  } else {
    Serial.println("Limit Switch 2: TOUCHED");
  }

  delay(200); // Wait for 200ms before checking again
}
