void setup() {
  Serial.begin(9600);
}

void loop() {
    delay(30);
    Serial.println(analogRead(A0));
}