bool ledOn = false;

void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);
  digitalWrite(13, LOW);
}

void loop() {
  int value = analogRead(A1);
  Serial.println(value);
  if (Serial.available() > 0) {
    int incomingByte = Serial.read();
    if (incomingByte == 'H') {
      ledOn = true;
    }
    if (incomingByte == 'L') {
      ledOn = false;
    }
  }
  if (ledOn) { // max: 977.52 Hz
    digitalWrite(13, HIGH);
    delayMicroseconds(value);
    digitalWrite(13, LOW);
    delayMicroseconds(1023 - value);
  } else {
    digitalWrite(13, LOW);
    delayMicroseconds(1000);
  }
}