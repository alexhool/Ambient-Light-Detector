bool ledOn = false;

void setup() {
  Serial.begin(2400);
  pinMode(13, OUTPUT);
  digitalWrite(13, LOW);
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
    int delay = round((unsigned long) value * value / 235.97);
    digitalWrite(13, HIGH);
    delayMicroseconds(delay);
    digitalWrite(13, LOW);
    delayMicroseconds(4435 - delay);
  } else {
    digitalWrite(13, LOW);
    delayMicroseconds(4435);
  }
}