bool ledOn = false;
bool nightOn = false;
bool stateOn = false;

void setup() {
  Serial.begin(9600);
  pinMode(2, OUTPUT);
  digitalWrite(2, LOW);
}

void loop() {
  long int t1 = micros();
  int value = analogRead(A7);
  //Serial.print(value);
  //Serial.flush();
  //Serial.print('|');
  //Serial.flush();
  if (Serial.available() > 0) {
    int incomingByte = Serial.read();
    if (incomingByte == 'H') {
      ledOn = true;
    }
    if (incomingByte == 'L') {
      ledOn = false;
    }
    if (incomingByte == 'N') {
      nightOn = true;
    }
    if (incomingByte == 'D') {
      nightOn = false;
    }
  }
  if (ledOn) {
    if (value >= 1020) {
      digitalWrite(2, HIGH);
      delayMicroseconds(11465);
    } else if (value < 45) {
      digitalWrite(2, LOW);
      delayMicroseconds(11465);
    } else {
      int delay = round((unsigned long) value * value / 91.0);
      digitalWrite(2, HIGH);
      delayMicroseconds(delay);
      digitalWrite(2, LOW);
      delayMicroseconds(11410 - delay); 
    }
  } else if (nightOn) {
    if (value >= 206) {
      stateOn = false;
      digitalWrite(2, LOW);
    } else if (value <= 103) {
      stateOn = true;
      digitalWrite(2, HIGH);
    } else {
      if (stateOn) {
        digitalWrite(2, HIGH);
      } else {
        digitalWrite(2, LOW);
      }
    }
    delayMicroseconds(11463);
  } else {
    digitalWrite(2, LOW);
    delayMicroseconds(11465);
  }
  long int t2 = micros();
  Serial.println(t2-t1);
  Serial.flush();
}