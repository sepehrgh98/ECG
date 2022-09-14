const int analogInPin = A0;  // Analog input pin that the potentiometer is attached to

double sensorValue = 0;        // value read from the pot
       
void setup() {
  delay(100);
  Serial.begin(9600);
}

void loop() {
  sensorValue = analogRead(analogInPin);
  sensorValue =sensorValue*3.3/1024;
  sensorValue =20*sensorValue/3.3 - 16;
  Serial.println(sensorValue);
  delay(3);
}
