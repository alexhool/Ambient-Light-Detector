const int ledPin = 13;
int incomingByte;

void setup() {
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, LOW);
}

void loop() {
  if (Serial.available() > 0) {
    incomingByte = Serial.read();
    if (incomingByte == 'H') {
      digitalWrite(ledPin, HIGH);
    }
    if (incomingByte == 'L') {
      digitalWrite(ledPin, LOW);
    }
  }
  if (digitalRead(ledPin)) {
    Serial.write('1');
  } else {
    Serial.write('0');
  }
}