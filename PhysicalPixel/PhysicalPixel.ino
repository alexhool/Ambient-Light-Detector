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
      Serial.write('1');
    }
    if (incomingByte == 'L') {
      digitalWrite(ledPin, LOW);
      Serial.write('0');
    }
  }
}