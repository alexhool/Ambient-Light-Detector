void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);
  digitalWrite(13, LOW);
}

void loop() {
  if (Serial.available() > 0) {
    int incomingByte = Serial.read();
    if (incomingByte == 'H') {
      digitalWrite(13, HIGH);
    }
    if (incomingByte == 'L') {
      digitalWrite(13, LOW);
    }
  }
  if (digitalRead(13)) {
    Serial.write('1');
  } else {
    Serial.write('0');
  }
}