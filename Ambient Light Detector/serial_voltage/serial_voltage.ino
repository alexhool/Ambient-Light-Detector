bool ledOn = false;

void setup() {
  Serial.begin(9600);
  pinMode(2, OUTPUT);
  digitalWrite(2, LOW);
}

void loop() {
  int value = analogRead(A7);
  Serial.print(value);
  Serial.flush();
  Serial.print('|');
  Serial.flush();
  if (Serial.available() > 0) {
    int incomingByte = Serial.read();
    if (incomingByte == 'H') {
      ledOn = true;
    }
    if (incomingByte == 'L') {
      ledOn = false;
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
  } else {
    digitalWrite(2, LOW);
    delayMicroseconds(11465);
  }
}