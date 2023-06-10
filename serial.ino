#include <AFMotor.h>

AF_DCMotor motor1(1);
AF_DCMotor motor4(4);

int data = 0;
String val = "";

int dist_covered_in_1s = 5; // should calculate this value in cms
int cur = (int)'0'; // Pos can be -1, 0, 1 denoting left, centre and right

void forward(int d = 400) {
  motor1.run(FORWARD);
  motor4.run(BACKWARD);
  delay(d);
}

void release() {
  motor1.run(RELEASE);
  motor4.run(RELEASE);
  delay(1000);
}

void backward (int d = 400) {
  motor1.run(BACKWARD);
  motor4.run(FORWARD);
  delay(d);
}

void setup() {
  
  Serial.begin(115200);

  motor1.setSpeed(255);
  // motor2.setSpeed(255);
  // motor3.setSpeed(255);
  motor4.setSpeed(255);

}

void loop() {

  while (Serial.available()) {
    data = Serial.read();
  }

  int pos = data;

  if (cur != pos) {
    if (cur == '0') {
      if (pos == '1') {
        forward();
        release();
        cur = pos;
      }
      
      else {
        backward();
        release();
        cur = pos;
      }
    }

    else if (cur == '-1') {
      if (pos == '0') {
        forward();
        release();
        cur = pos;
      }
      else {
        forward();
        release();
        forward();
        release();
        cur = pos;
      }
    }

    else {
      if (pos == '0') {
        backward();
        release();
        cur = pos;
      }
      else {
        backward();
        release();
        backward();
        release();
        cur = pos;
      }
    }
  }
}
