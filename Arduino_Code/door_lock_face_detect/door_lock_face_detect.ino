#include <LiquidCrystal.h>

const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2, pin1 = 10, pin2 = 9;
String data;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

void setup() {
  Serial.begin(9600);
  pinMode(pin1, OUTPUT);
  pinMode(pin2, OUTPUT);
  lcd.begin(16, 2);
  lcd.print("...On"); lcd.setCursor(2,1); lcd.print("Standby...");
}

void openDoor(){
    analogWrite(pin1, 5);
    digitalWrite(pin2, LOW);  
}

void closeDoor(){
    digitalWrite(pin1, LOW);
    digitalWrite(pin2, LOW);
}

void getRecognizedFace(){
    if(Serial.available() > 0){
        data = Serial.readStringUntil('\n');
        if(data != "Unknown"){
            lcd.print(data);
            lcd.setCursor(2, 1);
            lcd.print("detected");
            openDoor();
        }
        else{
            lcd.print("Face");
            lcd.setCursor(2,1);
            lcd.print("not recognized");
        }
    }
}

void loop() {
  delay(3500);
  lcd.clear();
  closeDoor();
  getRecognizedFace();
}
