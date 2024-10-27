// Include the Stepper library:
#include "Stepper.h"

//limit switches
const int x1_limit = 2;
const int x2_limit = 3;
const int y_limit = 4;
// Define number of steps per revolution:
const int stepsPerRevolution = 200;

// Initialize the stepper library on pins 8 through 11:
Stepper x_stepper = Stepper(stepsPerRevolution, 5, 6, 7, 8);
Stepper y_stepper = Stepper(stepsPerRevolution, 9, 10, 11, 12);
int nextStep;
int x1_pos = 0;
int x2_pos = 0;
int y_pos = 0;
void setup() {
  // Set the motor speed (RPMs):
  x_stepper.setSpeed(200);
  pinMode(x1_limit, INPUT_PULLUP); 
  pinMode(x2_limit, INPUT_PULLUP); 
  pinMode(y_limit, INPUT_PULLUP);

  //set 0 point
  //zero_x();
  //zero_y();
}

void loop() {
  /*
  // Step one revolution in one direction:
  x_stepper.step(800);


  // Step on revolution in the other direction:
  x_stepper.step(-800);

  delay(4000);
  */
  if (digitalRead(x1_limit) == LOW) { // Check if the limit switch is activated
    x1_pos = 0; // Reset the current position to zero
    Serial.println("Limit switch x1 hit, position reset to zero");
  }
  if (digitalRead(x2_limit) == LOW) { // Check if the limit switch is activated
    x2_pos = 0; // Reset the current position to zero
    Serial.println("Limit switch x2 hit, position reset to zero");
  }
  if (digitalRead(y_limit) == LOW) { // Check if the limit switch is activated
    y_pos = 0; // Reset the current position to zero
    Serial.println("Limit switch y hit, position reset to zero");
  }
  
  if (Serial.available() > 0) {
    int steps = Serial.parseInt(); // Read an integer from the serial monitor
    if (steps != 0) {
      if(x1_pos+steps <= 30000 ){//&& x1_pos+steps >= 0){
        x_stepper.step(steps); // Move the stepper motor by the specified number of steps
        x1_pos += steps;
      }
      else
        Serial.println("New position will be out of bounds");
    }
    /*
    else if(steps == 0){
      x1_pos = 0;
    }
    */
    Serial.print("x1: ");
    Serial.println(x1_pos);
  }// move based on serial


  
  
}
// Functions to reset 0 location of x1, x2, and y
void zero_x(){
  while(digitalRead(x1_limit) == HIGH && digitalRead(x2_limit) == HIGH ){
    x_stepper.step(-100);
  }
  x1_pos = 0;
  x2_pos = 0;
}
void zero_y(){
  while(digitalRead(y_limit) == HIGH ){
    y_stepper.step(-100);
  }
  y_pos = 0;
}