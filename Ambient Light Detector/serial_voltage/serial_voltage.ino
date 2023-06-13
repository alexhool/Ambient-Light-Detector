bool ledOn = false;

void setup() {
  Serial.begin(115200);
  pinMode(13, OUTPUT);
  digitalWrite(13, LOW);
}

void loop() {
  int value = analogRead(A0);
  Serial.println(value);
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
  if (ledOn) { // 977.52 Hz
    int delay = map(value, 0, 1023, 0, 1023);
    digitalWrite(13, HIGH);
    delayMicroseconds(delay);
    digitalWrite(13, LOW);
    delayMicroseconds(1023 - delay);
  } else {
    digitalWrite(13, LOW);
    delayMicroseconds(1000);
  }
}