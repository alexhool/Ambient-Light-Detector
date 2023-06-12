void setup() {
  Serial.begin(115200);
  pinMode(13, OUTPUT);
  digitalWrite(13, LOW);
}

void loop() {
    delay(20);
    Serial.println(analogRead(A0));
    if (Serial.available() > 0) {
      int incomingByte = Serial.read();
      if (incomingByte == 'H') {
        digitalWrite(13, HIGH);
      }
      if (incomingByte == 'L') {
        digitalWrite(13, LOW);
      }
    }
}